# space_facts_bot
This is a little twitterbot tells you the distance from earth to Voyager I &amp; II and other cool facts like nearby NEOs (near-earth-objects).
**Link**: https://twitter.com/space_facts_bot

![alt text](https://img.shields.io/badge/build-passing-brightgreen.svg)
![alt text](https://img.shields.io/badge/license-MIT-blue.svg)

--- 

## Source of information
Near-Earth objects data from the NASA/JPL SBDB Close Approach Data API: https://ssd-api.jpl.nasa.gov/doc/cad.html

Voyager Distance data from: https://theskylive.com/voyager1-tracker / https://theskylive.com/voyager2-tracker

NASA's Astronomical Picture of the Day (APOD): https://api.nasa.gov/api.html#apod

## Examples

- Voyager I is now 20,858,510,826 km from Earth. Voyager II is now 17,163,741,991 km from Earth. #bot #space #voyager
- Today's NEO: Object: 2017 QQ1 at 18:57. Estimated diameter: 0.0297 - 0.0665 km. #bot #NEO #asteroids

- APOD: 2nd september 2017: 
<img src="https://apod.nasa.gov/apod/image/1709/voyager_modern_poster.jpg" alt="APOD: 2nd september 2017" height="400"/>


## Project Structure

- bot.py is the main file from where the tweets are send. 

- voyager_distance.py, NEO_flyby.py and nasa_data.py are the files resonsible for accessing the APIs and scraping the data.

- The individual scripts are written in a way that no error might interrupt the process. Instead no tweet will be send regarding that data.

## TODO

- Add more information, possibly trough more APIs
- clean up code and be DRYer
- ~more explicit file and extension handling in nasa_data.py (e.g youtube video as APOD)~
- ~Allow .gif formats, but only up to 3MB (Twitter limitation)~


