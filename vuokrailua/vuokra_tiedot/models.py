# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


# This file governs the models that would be used with SQL database,
# below is one example of such datamodel.

class Kohde_tiedot(models.Model):
    def __unicode__(self):
        return self.osoite  
#
#    osoite = models.CharField(max_length=200)
#    neliot = models.CharField(max_length=200)
#    vuokra = models.CharField(max_length=200)
#    tyyppi = models.CharField(max_length=200)
#    lat = models.CharField(max_length=200)
#    lng = models.CharField(max_length=200)
