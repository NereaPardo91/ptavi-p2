#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
    def plus(op1, op2):
        """ Function to sum the operands """
        return op1 + op2


    def minus(op1, op2):
        """ Function to substract the operands """
        return op1 - op2

class CalculadoraHija(Calculadora):
    def multiply(op1, op2):
        """ Function to multiply the operands """
        return op1 * op2


    def division(op1, op2):
        """ Function to division the operands """
	try:
            op1 / op2	
        except ZeroDivisionError:
            sys.exit("Error: Division by zero is not allowed")

    if __name__ == "__main__":
        try:
            operando1 = int(sys.argv[1])
            operando2 = int(sys.argv[3])
        except ValueError:
            sys.exit("Error: Non numerical parameters")

        if sys.argv[2] == "suma":
            result = plus(operando1, operando2)
        elif sys.argv[2] == "resta":
            result = minus(operando1, operando2)
	elif sys.argv[2] == "multiplica":
            result = multiply(operando1, operando2)
	elif sys.argv[2] == "divide":
            result = division(operando1, operando2)
        else:
            sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')

        print(result)
