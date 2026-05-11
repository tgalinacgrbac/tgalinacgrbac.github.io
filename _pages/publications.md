---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
My publications list can be found on [Google Scholar](https://scholar.google.com/citations?user=ZC5pz7UAAAAJ&hl=en).

Below are a few of my recent publications. 


{% include base_path %}

{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
{% endfor %}
