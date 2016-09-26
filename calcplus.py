#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

if __name__ == "__main__":
	
	#fichero = sys.argv[1]
	with open('fichero.csv') as fichero:
		lineas = csv.reader(fichero)
		c = calcoohija.CalculadoraHija()
				
		for linea in fichero:
			operador = linea.split(',')[0]
			sumandos = linea.split(',')[1:]
			print(linea)
			
			##for palabra in linea:

				##sumandos = []
				##sumandos = next(lineas)
				##print(sumandos)
			
				##if sumandos[1] =
