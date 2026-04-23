lista=[] #creamos la lista donde se guardarán los números enteros

for i in range(8):   #creamos un bucle que se repetirá 8 veces, pidiendo en cada uno que el usuario agregue un número 
    while True:#hacemos un bucle para chequear que lo que escriba el usuario sea un número entero
        numero=input("ingrese un número: ")
        if numero.isdigit():#chequeo si es un número entero
            numero= int(numero)#cambiamos el formato del número ingresado de STR a INT
            lista.append(numero)#agregamos el número a la lista
            break#rompemos el ciclo, haciendo que siga al siguiente iteración del FOR
        else:
            print("ingreso inválido, por favor solo ingrese números")


print("La lista original es: \n",lista)#imprimimos la lista común
print("la lista, ordenada de menor a mayor, es: \n", sorted(lista))#imprimimos la lista ordenada de menor a mayor

print("La lista, ordenada de mayor a menor, es: \n", (sorted(lista, reverse=True)))#ordenamos la lista de mayor a menor usando reverse