---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Download full CV (PDF): [Galinac_Grbac_Tihana_CVen_May_2024.pdf](/files/Galinac_Grbac_Tihana_CVen_May_2024.pdf)

<div style="display:none;">

## Curriculum Vitae

The CV page is currently being updated.

## Selected Publications

<ul>{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

## Talks

<ul>{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html  %}
{% endfor %}</ul>

## Teaching

<ul>{% for post in site.teaching reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

</div>
