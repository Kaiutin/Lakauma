# -*- coding: utf-8 -*-
# @author: Samuel Uusi-Makela
# @version: 9.4.2013
#
# Lakauman vuokrakämppien esittely-ohjelman kontrolliluokka
# TODO:
# - tietokannan päivitys
# - scraperien/webdriverien käyttö/ajo
# - karttakuvan piirtopyyntö piirturiluokalle
# - Kaikkea kivaa.

# Ajaa scraperit
def aja_scraperit():
    return "Tietokantaan sopiva taulukko"

# Nouda tiedot scrapereilta ja päivitä kanta
def päivitä_tietokanta():
    puske_tieto_kantaan(aja_scraperit())

# Tunkee tiedot tietokantaan.
def puske_tieto_kantaan(jokin_taulukko):
    tietokanta_kontrolli.työnnä_kantaan(jokin_taulukko)    
    pass

def tietokanta_haku(sijainti, hinta, vuokra, tyyppi):
    return "Kaksiulotteinen taulukko kohteita."
    
def piirrä_kartta():
    return "Karttaobjekti johon piirrettynä täpit"



