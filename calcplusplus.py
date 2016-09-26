#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

if __name__ == "__main__":
	
	with open('fichero.csv') as fichero:
		fich = csv.reader(fichero)

		c = calcoohija.CalculadoraHija()
				
		for linea in fichero:
			operador = linea.split(',')[0]
			sumandos = linea.split(',')[1:]
			solucion = int(sumandos[0])

			if operador == "suma":
				for i in sumandos[1:]:
					solucion = c.plus(solucion, int(i))
				print(solucion)
					
			elif operador == "resta":
				for i in sumandos[1:]:
					solucion = c.minus(solucion, int(i))
				print(solucion)

			elif operador == "multiplica":
				for i in sumandos[1:]:
					solucion = c.multiply(solucion, int(i))
				print(solucion)

			elif operador == "divide":
				for i in sumandos[1:]:
					solucion = c.division(solucion, int(i))
				print(solucion)

			else:
				sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')
			
