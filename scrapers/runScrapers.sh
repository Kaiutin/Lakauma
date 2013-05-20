# This file is part of Loukku, an application to display available rental apartments on Google Maps map.
# Copyright (C) 2013  Anton Laurila, Jari-Matti Kankaanpää, Samuel Uusi-Mäkelä
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# For more information, please refer to LICENCE file found in /Lakauma,
# or <http://www.gnu.org/licenses/> and GNU Affero General Public License

# script must be run from /Lakauma/scrapers/
scrapy crawl sato -o sato_json.json -t json
scrapy crawl koas -o koas_json.json -t json
python xpath_soppa.py
cd ./scrapers/spiders/crawlersAndDrivers/
python ovv_webdriver.py
cd ../../../

python merge_json.py

mongoimport --collection asunnot --file ./all_together.json --jsonArray

