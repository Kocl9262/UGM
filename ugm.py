# -*- coding: utf-8 -*-

import random
from drzave import ugm


odg = "egrgwrfgw"
tocke = 0
poskus = 3


def r_high_score():
    high_score_fi = open("high_score.txt", "r")
    high_score = int(high_score_fi.read())
    high_score_fi.close()
    return high_score


print("Trenutni rekord je %s" % r_high_score())
print("%sx lahko odgovoriš narobe." % poskus)

while odg != "ne":
    if poskus <= 0:
        print("Game Over!")
        break

    else:
        drzava = random.choice(ugm.keys())
        odg = raw_input("Želiš uganiti glavno mesto države? (da/ne) ")
        if odg == "da":
            odg2 = raw_input(drzava + ": ").lower()
            if odg2 == ugm[drzava].lower():
                tocke += 1
                print("Obvladaš glavna mesta, odgovor je pravilen!")
                print("Vaš rezultat je %s." % tocke)

            else:
                tocke -= 1
                poskus -= 1
                print("Odgovor je " + ugm[drzava])
                print("Vaš rezultat je %s. Imate še %s poskusov" % (tocke, poskus))

        else:
            print("Hvala za igranje!")
            break

print("--------------------------------------")
print("Vaš končni rezultat je %s." % tocke)

if tocke > r_high_score():
    n_high_score = tocke
    high_score_f = open("high_score.txt", "w")
    high_score_f.write(str(n_high_score))
    high_score_f.close()
    print("Nov rekord!")
