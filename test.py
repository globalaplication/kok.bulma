#!/usr/bin/env python
#-*-coding:utf-8-*-

import os

def derece():
	return int(input("Kök'ün Derecesini Giriniz:"))
	
while True:
	print("Kök Bulma Programı")
	a = int(input("Bir Sayi Giriniz:"))
	c = derece()
	while c is 0:
		print ("derecesi 0 olamaz!")
		c = derece()
	b = a ** (1/c)
	os.system("clear")
	print("Sonuc:",b, "\n", "-------------------")
