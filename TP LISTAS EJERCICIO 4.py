datos=[1,3,5,3,7,1,9,5,3]
lista_sin_repetir=[] #creamos una lista donde pondremos los items sin repetir

for i in datos: #creamos un bucle el cual pasa por todos los items en la lista datos
    if i not in lista_sin_repetir:#chequea si el item el cual estamos pasando actualmente en el bucle  no esta en la lista sin repetir
        lista_sin_repetir.append(i)#si el item no esta en la lista, lo agregamos
    else:
        continue#si el item que estamos pasando ESTA EN LA LISTA sin repetir, lo ignoramos
print(datos)
print(lista_sin_repetir) #mostramos la lista con los items sin repetir

