import random # importamos random para poder hacer el programa indicado

#creamos las listas las cuales irán los números en el futuro
lista_numeros=[]
lista_pares=[]
lista_impares=[]

for i in range(15): #empezamos el bucle para generar números aleatorios, se repite 15 veces
    numero=random.randint(1,100) #esta variable genera un número al azar del 1 al 100
    lista_numeros.append(numero)#agregamos el número generado

print("los 15 números son: ",sorted(lista_numeros)) #mostramos la lista completa de números generados, ordenados de menor a mayor

for i in lista_numeros:#creamos un bucle el cual recorre la lista de números completa
    if i %2==0:
        lista_pares.append(i)#si el número es par, lo agregamos a la lista de pares
    else:
        lista_impares.append(i)#si es impar, lo agregamos a la de impares

#ahora imprimimos los datos pedidos en el ejercicio, la lista de los números pares e impares, y cuántos hay en cada uno

print("los números pares son: ", sorted(lista_pares),  ". son un total de ", len(lista_pares), "numeros")

print("los números pares son: ", sorted(lista_impares),  ". son un total de ", len(lista_impares), "numeros")