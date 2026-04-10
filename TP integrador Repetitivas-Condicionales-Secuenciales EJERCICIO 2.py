#ALUMNO: LAUTARO BUSTILLO
usuario= "alumno"
contraseña= "python123"

intentos= 1#con esto chequeamos la cantidad de veces que intentaron entrar al campus

while intentos<4:
    print("Intento número ", intentos, "/3")
    intento_usuario= input("ingrese su usuario: ")
    intento_contraseña= input("ingrese su contraseña: ")

    if intento_usuario == usuario and intento_contraseña==contraseña: #si ingresó el usuario y contraseña de manera correcta, termina el bucle
        print("Bienvenido")
        break
    else:
        print("Usuario o contraseña incorrectos")
        intentos +=1
        if intentos==4:
            print("Demasiados intentos erróneos, terminal bloqueada") #si los intentos no cinciden con usuario y contraseña, y lo intentan 3 veces, se rompe el bucle y el siguiente no empieza
            break


if intento_usuario == usuario and intento_contraseña==contraseña: #de esta manera nos aseguramos que entran al menú solo si lograron ingresar de manera correcta
    while True:
        print("Bienvenido al campus")
        menu=input("opciones: " \
        "1) Ver estado de inscripción " \
        "2) Cambiar clave " \
        "3)Mostrar un mensaje inspiracional " \
        "4)salir " \
        "")
        if  not menu.isdigit()  or menu  not in ["1", "2", "3", "4"]: #chequeamos que el usuario haya ingresado un caracter numérico y que esté dentro del rango del menú (1 al 4)
            print("por favor, elija una opción válida")
            continue
        
            
        if menu=="1":
            print("Usted esta inscripto")
        elif menu=="2":
            while True:
                    #hacemos dos variables nuevas, una para la nueva contraseña y la otra para el chequeo
                    nueva_contraseña=input("ingrese la nueva contraseña: ")
                    intento_nueva_contraseña=input("ingrese nuevamente la contraseña: ")
                    if len(nueva_contraseña) < 6:
                        print("Elija una contraseña de mínimo 6 caracteres")
                    elif nueva_contraseña != intento_nueva_contraseña:
                        print("las contraseñas no coinciden")
                    elif nueva_contraseña==intento_nueva_contraseña and len(nueva_contraseña) >= 6: #una vez que las contraseñas coincidan y sea de mas de 6 caracteres, cambiamos la contraseña y terminamos el bucle
                        print("contraseña cambiada de manera exitosa")
                        contraseña=nueva_contraseña #con esto cambiamos la contraseña original
                        break
        elif menu=="3":
                print("imaginate que se me ocurrió una frase motivadora para decirte ahora") #nada que escribir aquí, no se me ocurrió algo, disculpen
        elif menu=="4":
                print("nos vemos")
                break

