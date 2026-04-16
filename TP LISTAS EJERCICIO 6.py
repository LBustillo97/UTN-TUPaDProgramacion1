lista=[]#hacemos la lista que va a tener los 7 números
lista_2=[]#hacemos la lista la cual usaremos para invertir la anterior



for i in range(7):#creamos un bucle que se repite 7 veces
    while True: #empezamos un bucle para corroborar que lo que ingrese el usuario sea un número
        numero=input("ingrese un número a la lista: ")#creamos una variable para que el usuario ingrese un número
        if numero.isdigit():#si lo ingresado es un número, lo convertiomos en formato número y lo agregamos a la lista
            numero=int(numero)
            lista.append(numero)
            break
        else:
            print("ingrese un numero nomas")

for i in lista[::-1]:#creamos un bucle el cual recorre la lista de manera invertida
    lista_2.append(i)#agregamos a la lista el item el cual estamos pasando actualmente, y como estamos yendo del ultimo al primero, creamos una lista nueva la cual invierte el orden de la primera lista

lista_3=lista[::-1]#otra manera de invertir la lista es esta
print(lista_2)
print(lista_3)
