lista_alumnos=["Pepito", "Pepita", "Fulano", "Fulana", "Mengano", ",Mengana", "Micho", "Coqui"] #esta es la lista de alumnos



while True: #empezamos el bucle para el menu de opciones
    print("Actualmente la lista de alumnos es: ", lista_alumnos)#cada vez que reinicia el bucle le mostramos al usuario la lista actual
    menu=input("1)Agregar un nuevo Alumno \n 2)Eliminar a un alumno de la lista \n 3)Salir \n")
    if menu.isalnum() and menu in ["1", "2", "3"]:#con esto chequeamos que lo que haya elegido el usuario se una opción válida
        if menu=="1":#opción: agregar un nuevo nombre a la lista
            while True:
                nombre=input("Ingrese el nombre que quiere agregar: ").capitalize()#con capitalize nos aseguramos que no importa lo que escriba el usuario, la primer letra siempre va a ser mayusculay las otras minusculas
                if nombre in lista_alumnos:#si el nombre ya esta en la lista, no lo agregaremos
                    print("Ese nombre ya esta en la lista")
                elif nombre.isalpha() and nombre not in lista_alumnos:#chequeamos que el nombre sea uno válido y que no esté en la lista
                    lista_alumnos.append(nombre)#agregamos el nombre y terminamos el bucle de la opción 1
                    break
                else:
                    print("Por favor, escriba el nombre solo y sin números")
        elif menu=="3":
            print("Perfecto, adios")#rompemos el bucle del menu principal y consecuentemente terminamos el programa
            break
        elif menu=="2":#opcion: sacar un nombre de la lista. es practicamente igual a la opcion 1, pero en luggar de append usamos remove
            while True: #mismo bucle que en opcion 1
                nombre=input("Ingrese el nombre que quiere eliminar: ").capitalize()
                if nombre  not in lista_alumnos:
                    print("Ese nombre no esta en la lista")
                elif nombre.isalpha() and nombre in lista_alumnos:
                    lista_alumnos.remove(nombre)
                    print("Nombre eliminado")
                    break
                else:
                    print("Por favor, escriba el nombre solo y sin números")
    else:
        print("por favor elija una de las opciones correctas")           


