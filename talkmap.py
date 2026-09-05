# Leaflet cluster map of talk locations
#
# Run this from the _talks/ directory, which contains .md files of all your
# talks. This scrapes the location YAML field from each .md file, geolocates it
# with geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# #talkmap Jupyter notebook.
import frontmatter
import glob
import getorg
import json
import os
import time
from types import SimpleNamespace
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

# Set the default timeout, in seconds
TIMEOUT = 5
REQUEST_DELAY_SECONDS = 1.1
MAX_RETRIES = 4
CACHE_PATH = "talkmap/geocode-cache.json"
FALLBACK_COORDS = {
    "Dusseldorf, Germany": {"lat": 51.2254018, "lon": 6.7763137},
    "Bansko, Bulgaria": {"lat": 41.8344086, "lon": 23.4841698},
    "Larnaca, Cyprus": {"lat": 34.9236095, "lon": 33.6236184},
}


def load_cache(cache_path):
    if not os.path.exists(cache_path):
        return {}

    try:
        with open(cache_path, "r", encoding="utf-8") as cache_file:
            return json.load(cache_file)
    except Exception as ex:
        print(f"Warning: failed to load geocode cache from {cache_path}: {ex}")
        return {}


def save_cache(cache_path, cache_data):
    try:
        with open(cache_path, "w", encoding="utf-8") as cache_file:
            json.dump(cache_data, cache_file, indent=2)
    except Exception as ex:
        print(f"Warning: failed to save geocode cache to {cache_path}: {ex}")


def geocode_with_retries(geocoder, location_text):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            time.sleep(REQUEST_DELAY_SECONDS)
            result = geocoder.geocode(location_text, timeout=TIMEOUT)
            return result
        except GeocoderTimedOut as ex:
            print(
                f"Retry {attempt}/{MAX_RETRIES} "
                f"for {location_text}: timeout ({ex})"
            )
        except Exception as ex:
            # Nominatim commonly returns HTTP 429
            # when requests are too frequent.
            message = str(ex)
            if "429" in message and attempt < MAX_RETRIES:
                backoff = attempt * 2
                print(
                    f"Retry {attempt}/{MAX_RETRIES} "
                    f"for {location_text}: rate-limited "
                    f"(HTTP 429), waiting {backoff}s"
                )
                time.sleep(backoff)
                continue

            print(
                "An unhandled exception occurred while processing "
                f"input {location_text} with message {ex}"
            )
            return None

    return None


# Collect the Markdown files
g = sorted(glob.glob("_talks/*.md"))

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
location = ""
permalink = ""
title = ""
geocode_cache = load_cache(CACHE_PATH)
talk_records = []

# Collect talk records
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    if 'location' not in data:
        continue

    # Prepare the description
    title = data['title'].strip()
    venue = data['venue'].strip()
    location = data['location'].strip()
    description = f"{title}<br />{venue}; {location}"
    talk_records.append({"description": description, "location": location})

# Geocode unique locations (with caching)
unique_locations = sorted({record["location"] for record in talk_records})
for location in unique_locations:
    if location in geocode_cache:
        continue

    # Geocode the location and report the status.
    try:
        geocoded = geocode_with_retries(geocoder, location)
        if geocoded is None:
            if location in FALLBACK_COORDS:
                geocode_cache[location] = FALLBACK_COORDS[location]
                print(f"Using fallback coordinates for {location}")
            else:
                print(f"Skipping {location}: no coordinates resolved")
            continue

        geocode_cache[location] = {
            "lat": geocoded.latitude,
            "lon": geocoded.longitude,
        }
        print(location, geocoded)
    except ValueError as ex:
        print(f"Error: geocode failed on input {location} with message {ex}")

# Build map points for all talks whose location was resolved.
for record in talk_records:
    location = record["location"]
    description = record["description"]
    if location not in geocode_cache:
        print(f"Skipping talk due to unresolved location: {description}")
        continue

    cached = geocode_cache[location]
    location_dict[description] = SimpleNamespace(
        latitude=cached["lat"],
        longitude=cached["lon"],
    )
    print(f"Mapped: {description}")

# Save the map
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(
    location_dict,
    folder_name="talkmap",
    hashed_usernames=False,
)
save_cache(CACHE_PATH, geocode_cache)
