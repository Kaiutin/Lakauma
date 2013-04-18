# Change working directory to the projects directory
# which contains the testdata, items.json
cd /your/path/to/Lakauma/vuokrailua/vuokra_tiedot/

# Start up mongodb, change path to where you want the database to be located
sudo mongod --dbpath ~/where/you/want/your/database/ --smallfiles

# Finally import the contents of the items.json file to the databse.
mongoimport --collection asunnot --file items.json --jsonArray

