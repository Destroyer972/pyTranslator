import random as rd

from translator import *

LANG = "es"

ts = Translator(LANG,"en","langs")

print("====={}=====".format(ts.get_element("global/title")))
nb_tire = rd.randint(0,100)
nb_choisi = 101
print(nb_tire)
while nb_choisi != nb_tire : 
	nb_choisi = int(input(ts.get_element("game/choose_number")))
	if nb_choisi > nb_tire :
		print(ts.get_element("game/less"))
	elif nb_choisi < nb_tire:
		print(ts.get_element("game/more"))
	else:
		print(ts.get_element("game/won"))
