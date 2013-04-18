Lakauma
=======

This projects aim is to create an application to help visualize the locations of rental 
apartments in Jyväskylä region. After this version is complete we will be releasing more general
version of the application. The application is accessed via browser, and the default 
url (assuming you are running the server locally) is "http://127.0.0.1:8000/vuokra_tiedot/".
The application should present a Google maps map, with different search-matching apartments marked. 
Clicking a marker will open a small infowindow for that apartment, which contains basic information 
about the apartment and a link to the original housing agency that owns the apartment. 

################

Requirements and running:

To run the application you need:
* pip (extremely useful python package manager, makes installing rest of the requirements a breeze)
* Python 2.7 (3.0, or older python versions compatability not tested)
* Django 1.5 => 
* mongodb 2.4.1 =>
* pymongo 
* cron (or similar scheduling system)
* scrapy

Additionally you will need to have mongodb running. Assuming you have installed mongodb, 
for running it and importing necessary files please refer to /docs/mongoStart.txt for instructions.

Running the server is done simply by changing the working directory to /vuokrailua/,
and running "python manage.py runserver". Assuming that requirements are correctly installed,
you should find the application running at "http://127.0.0.1:8000/vuokra_tiedot/", with the test apartments found in 
items.json file displayed on map.

Daily database updates will be implemented later.

This guide is updated regularly as the project advances, so above requirements and instructions are not quaranteed to 
be comrehensive. If you have trouble running the application please wait for a few days for the list to update, 
and if the problem persists, please contact us at kaiutindev(at)gmail.com
