

"""
print("hola mundo!")

"""ejercicio 2"""

nombre = input("ingrese su nombre")

print("hola", nombre)


"""ejercicio 3"""

nombre = input("ingrese su nombre: ")

apellido= input("ingrese su apellido: ")

edad= input("ingrese su edad: ")

residencia= input("ingrese el pais donde vive: ")

print("mi nombre es ", nombre, " ", apellido, ", tengo ", edad, " años y vivo en ", residencia )

"""ejercicio 4"""
import math


radio= int(input("ingrese el radio del círculo: "))

area= math.pi * radio**2
perimetro= math.pi*2*radio

print("el area del circulo es ", area, " y el perimetro es ", perimetro)


"""ejercicio 5"""


segundos= int(input("ingrese la cantidad de segundos que quiera: "))

horas= segundos/3600

print("esa cantidad de segundos equivale a ", horas,"horas")"""

"""ejercicio 6"""

numero= int(input("por favor ingrese un número: "))

for i in numero(10):
    print(numero*i)