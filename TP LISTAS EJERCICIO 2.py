
lista_productos=[] #creamos la lista la cual guardaremos los productos, empieza vacía

for i in range(5): #empezamos un bucle para ingresar los productos, el cual se repetirá 5 veces
    print("ingrese el producto número ", i+1, ": ")
    while True: #hacemos un bucle para autentificar que el usuario no agregue un string vacío
        producto=input()
        if producto != "": #aqui validamos que el producto no sea un string vacío
            lista_productos.append(producto)#agregamos el producto a la lista
            break
        else: #si ES un string vacío, le hacemos intentar de nuevo
            print("por favor, ingrese un producto: ")


print("la lista ordenada queda asi:", sorted(lista_productos)) #le mostramos la lista ordenada de manera alfabética al usuario. para ahorrarnos hacer una variable solo para ordenar toda la lista hago el comando directo en el print
while True: #empezamos el bucle para borrar items de la lista
    confirmar_borrar=input("¿Quiere eliminar un producto? S/N: ").lower()#empezamos pidiendole al usuario si quiere borrar o no. pasamos lo escrito a minúscula para que, su input sea válido, no importa si usó mayusculas o no.
    if confirmar_borrar== "n":
        print("Perfecto, nos vemos")
        break#si elige no, terminamos el bucle y consecuentemente, el programa
    elif lista_productos==[]:#chequea si la lista está vacía
        print("Actualmente su lista esta vacía, nos vemos")
        break#si la lista esta vacía, no hay motivo para seguir borrando, terminamos el bucle
    elif confirmar_borrar=="s": 
        print("Perfecto, le recuerdo que la lista actualmente contiene: ",sorted(lista_productos))#recordatorio al usuario para que pueda chequear cómo escribió los items, así puede ingresarlos de manera correcta para borrarlos
        while True:  #empezamos un bucle para validar si el item que escribe está dentro de la lista
            palabra_borrada=input("ingrese el producto que quiere eliminar, respetando las mayúsculas, minúsculas y espacios: ")
            if palabra_borrada in lista_productos:#chequea si lo que ingresó el usuario está en la lista
                print("Perfecto, sacaremos de la lista ", palabra_borrada)
                lista_productos.remove(palabra_borrada)#eliminamos el item
                print("La lista actualmente contiene a: ",sorted(lista_productos))#mostramos los cambios hechos en la lista
                break#una vez borrado el item, rompemos el bucle
            else:#al cubrir la opción si el item está en la lista, solo queda la opción si no está, la cual cubrimos en esta parte imprimiendo la notificación y un nuevo recordatorio de la lista
                print("mmm, no encuentro el producto que escribió, por favor vuelva a intentarlo: ")
                print("Perfecto, le recuerdo que la lista actualmente contiene: ", sorted(lista_productos))

    else:#dentro del menú de si se quiere eliminar un item, si el usuario escribe una letra que no corresponde a las indicadas, le hacemos volver a intentarlo
        print("Por favor, elija una opción válida")

    
    