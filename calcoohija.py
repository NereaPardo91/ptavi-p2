#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):
	def multiply(self, op1, op2):
		""" Function to multiply the operands """
		return op1 * op2


	def division(self, op1, op2):
		""" Function to division the operands """
		try:
			cociente = op1 / op2	
		except ZeroDivisionError:
			sys.exit("Error: Division by zero is not allowed")
			return cociente

if __name__ == "__main__":
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	if sys.argv[2] == "suma":
		result = CalculadoraHija.plus(operando1, operando2)
	elif sys.argv[2] == "resta":
		result = CalculadoraHija.minus(operando1, operando2)
	elif sys.argv[2] == "multiplica":
		result = CalculadoraHija.multiply(operando1, operando2)
	elif sys.argv[2] == "divide":
		result = CalculadoraHija.division(operando1, operando2)
	else:
		sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')

	print(result)
