# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Kohde_tiedot(models.Model):
    def __unicode__(self):
        return self.osoite + " " + "neliot:" + self.neliot + " " + " FUCK YEAH" 

    osoite = models.CharField(max_length=200)
    neliot = models.CharField(max_length=200)
    vuokra = models.CharField(max_length=200)
    tyyppi = models.CharField(max_length=200)


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text

