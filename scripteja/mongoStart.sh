cd ~/Documents/lakauma/Lakauma/vuokrailua/vuokra_tiedot/

sudo mongod --dbpath ~/Documents/lakauma/ --smallfiles

mongoimport --collection asunnot --file items.json --jsonArray

