#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":
	
	fichero1 = sys.argv[1]
	fichero = open(fichero1, 'r')
	datos = fichero.readlines()

	c = calcoohija.CalculadoraHija()
				
		for linea in datos:
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
