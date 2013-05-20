# @author: Samuel Uusi-Makela
# @version: 7.5.2013
# This file is part of Loukku, an application to display available rental apartments on Google Maps map.
# Copyright (C) 2013  Anton Laurila, Jari-Matti Kankaanpää, Samuel Uusi-Mäkelä
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# For more information, please refer to LICENCE file found in /Lakauma,
# or <http://www.gnu.org/licenses/> and GNU Affero General Public License
# Merge_json

from StringIO import StringIO
import sys
import json

class Mergeri():
    complete = []

    def read_and_add(self,tiedosto):
        tied = open(tiedosto, 'r')
        self.complete = self.complete + json.load(StringIO(str(tied.read())))
        tied.close()

kasa = Mergeri()
kasa.complete = []

kasa.read_and_add("sato_json.json")
kasa.read_and_add("koas_json.json")
kasa.read_and_add("kortepohja_json.json")
kasa.read_and_add("ovv_json.json")

complete_file = open("all_together.json", 'w')
print json.dumps(kasa.complete)
complete_file.write(json.dumps(kasa.complete, sort_keys = False, indent = 4))
