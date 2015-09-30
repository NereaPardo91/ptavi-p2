#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":
    leer = open(sys.argv[1],"r")
    lineas = leer.readlines()
    calcu= calcoohija.CalculadoraHija()
    for linea in (lineas):
        #print(linea[:-1])
        palabra = linea.split(",")
        #print (palabra) 
        operador=palabra[0]
       
        print(operador)
       
        if operador == "suma":
            sum1=0
            for operaciones in palabra[1:]:
                sum1=calcu.suma (sum1, int(operaciones))
            print(sum1)
            
        if operador == "resta":
            rest1= calcu.resta(int(palabra[1]), int(palabra[2]))
            for operaciones in palabra[3:]:
                rest1=calcu.resta(rest1, int(operaciones))
            print(rest1)
        
        if operador == "multiplica":
            mult=1
            for operaciones in palabra[1:]:
                print(mult)
                mult=calcu.multiplica(mult, int(operaciones))
                print(mult)
            print(mult)

        #else:
         #   sys.exit("MAL")
           
        #print(resultado)
     
