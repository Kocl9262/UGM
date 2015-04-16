# -*- coding: utf-8 -*-

import random

ugm = {"Slovenija": "Ljubljana",
       "Hrvaška": "Zagreb",
       "Avstrija": "Dunaj",
       "Nemčija": "Berlin",
       "Finska": "Helsinki",
       "Irska": "Dublin",
       "Švica": "Bern",
       "Portugalska": "Lizbona",
       "Ukrajina": "Kijev",
       "Španija": "Madrid",
       "Norveška": "Oslo",
       "Italija": "Rim",
       "BiH": "Sarajevo",
       "Nizozemska": "Amsterdam",
       "Slovaška": "Bratislava",
       "Belgija": "Bruselj",
       "Madžarska": "Budimpešta",
       "Romunija": "Bukarešta",
       "Belorusija": "Minsk",
       "Makedonija": "Skopje",
       "Srbija": "Beograd",
       "Turčija": "Ankara",
       "Moldavija": "Kišinjev",
       "Švedska": "Stockholm",
       }

odg = "egrgwrfgw"

while odg != "ne":
    drzava = random.choice(ugm.keys())
    odg = raw_input("Želiš uganiti glavno mesto države? (da/ne) ")
    if odg == "da":
        odg2 = raw_input(drzava + ": ")
        if odg2 == ugm[drzava]:
            print("Obvladaš glavna mesta, odgovor je pravilen!")

        else:
            print("Odgovor je " + ugm[drzava])

    else:
        print("Hvala za igranje!")
