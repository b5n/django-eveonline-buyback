# Django EVE Online Buyback

A simple Django extension providing an easy way to appraise buyback items in bulk.

# Installation

1. Add `django_eveonline_buyback` to your INSTALLED_APPS
2. Include the `django_eveonline_buyback` URLs in your urls.py
3. Run `python3 manage.py migrate` to create the django_eveonline_timerboard models

# Provided URLs
| URL Name | Descripion |
| -------------- | -------------- |
| django-eveonline-buyback submit-buyback | Submit a buyback inventory list for appraisal |
| django-eveonline-buyback view-buyback | View raw buyback data |
| django-eveonline-buyback update-blueloot-base | Modify blue loot base prices |
