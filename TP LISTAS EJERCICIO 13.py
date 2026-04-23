puntajes = [450, 1200, 875, 990, 300, 1500, 640]#creamos la lista tal y como nos pide el ejercicio
puntajes_ordenados= sorted(puntajes, reverse=True)#creamos una lista que contenga los puntajes ordenados de mayor a menor
print("Mejores 7 puntajes:")
for i in puntajes_ordenados:#hacemos un bucle que recorrerá toda la lista nueva que creamos
    print("Puesto ", (puntajes_ordenados.index(i))+1, ":", i)#imprime el puesto correspondiente de la iteración actual
#en los siguientes buscamos el maximo y el minimo en los puntajes. no hace falta usar la lista nueva ya que MAX y MIN ya es suficiente
print("Mejor puntaje: ", max(puntajes))
print("peor puntaje: ", min(puntajes))

while True:#se me ocurrió que, en lugar de buscar sólo el 990 como pide el ejercicio, hacer un menú que deje buscar cualquier puntaje. aqui abrimos el bucle del menú
    menu=input("Opciones: \n1)Buscar Puntaje \n2)Salir \n")
    if menu=="1":#opción de buscador de puntaje
        while True: #abrimos un while para autentificar que el usuario ingrese un número y no otra cosa
            puntaje=(input("Ingrese el puntaje que quiera buscar: "))
            if puntaje.isdigit():
               puntaje=int(puntaje)#convertimos lo ingresado por el usuario a INT para poder usar el número para el buscador sin romper algo
               break
            else:
                 print("ingrese solo números")
             

        
        if puntaje in puntajes_ordenados:#si el número escrito por el usuario (variable puntaje) está en la lista de puntajes, imprimimos el mensaje con el puesto que está
                print("El puntaje ", puntaje, " está en el puesto número ", puntajes_ordenados.index(int(puntaje))+1)
        else:
             print("Ese puntaje no está en la lista, le recuerdo los números que estan: ", puntajes)        
    elif menu=="2":#opción 2. simplemente terminamos el menu y por ende, el programa
         print("Adios")
         break
    else:
         print("Por favor, elija una opción válida.")