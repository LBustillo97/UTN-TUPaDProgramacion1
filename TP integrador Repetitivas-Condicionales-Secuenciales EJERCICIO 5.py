#ALUMNO: LAUTARO BUSTILLO
import random
#Vidas del jugador y del enemigo
vida_usuario= 100 
vida_enemigo=100
#pociones disponibles para cada uno
pociones_vida_usuario=3 #cada poción de vida les dará 30 de vida
pociones_vida_enemigo=3
pociones_armadura_usuario=2 #cada pocion de armadura les subirá el valor de armadura en 1. Podría haber agregado una pocion de ataque también, pero me quedé sin tiempo.
pociones_armadura_enemigo=2
daño_usuario=15
daño_enemigo=12
armadura_usuario=1 #Se me ocurrió agregar un sistema de armadura parecido al Pixel Dungeon (que a su vez lo saca de Rogue). al momento de conectar un golpe, al daño base se le resta la cantidad de armadura que tiene cada uno. Mas adelante veremos la fórmula
armadura_enemigo=2 #mientras el usuario tiene mas ataque, el enemigo tiene mas defensa.
turno_usuario= True



while True:
    usuario=input("Bienvenido a la arena, gladiador. Ingrese su nombre: ")
    if usuario.isalpha():
        break           #De esta manera, si el nombre no esta compuesto por caracteres alfabéticos repetirá la función hasta que sea verdadero.
    else:
        print("ingrese un nombre válido")
print(usuario,", buen nombre.\n Te enfrentarás al gran Tigre del Quequén. Te daremos una espada, 3 pociones de vida y 2 de armadura. Buena suerte")




while vida_usuario>0 and vida_enemigo>0:                    #de esta manera, cuando una de las dos vidas llegue a 0 o menos, termina el bucle de batalla 
    if turno_usuario==True:                                    #cada ataque o acción cambia el estado del turno del usuario a FALSE, pasando al turno del enemigo en el siguiente ELIF
        print("Vida actual: ", vida_usuario,", pociones de vida restantes: ", pociones_vida_usuario, ", pociones de armadura restantes: ", pociones_armadura_usuario ,"\n", "Vida actual del enemigo: ", vida_enemigo, )
        menu=input("¡Es tu turno de actuar! ¿Cuál es tu movimiento? \n 1) ataque pesado \n 2) ataques ráfaga(3 ataques seguidos) \n 3) Beber poción de vida \n 4) Beber poción de armadura ")
        if  not menu.isdigit()  or menu  not in ["1", "2", "3", "4"]:                   #Al igual que con el nombre, chequeamos que hayan elegido un número válido para continuar
            print("por favor, elija una opción válida")
            continue
        elif menu=="1":
            if vida_enemigo < 20:                           #en este IF se chequea la vida del enemigo para confirmar un golpe crítico.
                chance=random.randint(1,4)                  #en cada ocasión de ataque agregué un sistema de chances, parecido a Pokemon. cada vez que entra en el IF correspondiente pide un número del 1 al 4 para el usuario y 1 al 3 para el enemigo.
                if chance != 4:                             #haciendo que todos los números menos el 4 entren, le damos al jugador una chance de golpear de un 75%
                    vida_enemigo-= (daño_usuario*1.5-armadura_enemigo)          # aquí vemos el cálculo que se hace para el daño, nada mas que en esta ocasión se agrega el multiplicador del daño crítico (1.5)
                    print("¡Golpe crítico!")
                    turno_usuario=False                     #como dije anteriormente, cambiar la bandera a False en cada acción hace que cambie al turno del enemigo.
                else:
                    print("Has fallado el golpe")
                    turno_usuario=False
            else:
                chance=random.randint(1,4) #este ELSE es para los golpes normales no críticos
                if chance != 4:
                    vida_enemigo-= (daño_usuario-armadura_enemigo) 
                    print("Has conectado el golpe")
                    turno_usuario=False
                else:
                    print("Has fallado el golpe") #ELSE que cubre el caso en el que el número de la variable CHANCE diera 4, el ataque falla y termina el turno
                    turno_usuario= False
        elif menu=="2": #estos son los ataques ligeros, que hace tres seguidos
            for i in range(3): #con el for in range (3) le damos 3 instancias de golpes antes de romper el bucle
                chance=random.randint(1,4)
                if chance != 4:
                    vida_enemigo -=(8-armadura_enemigo) #al haber agregado la variable de armadura y de chances de golpear, me vi obligado a subir el daño del ataque ligero de 5 a 8, sino el enemigo al tomarse sus pociones no hacíamos daño alguno
                    print("golpe número ", i+1, "conecta") #con eso le mostramos al usuario qué golpes conectaron y cuales no. i+1 es debido a que el primer i es el número 0, queda raro anunciar que tu golpe número 0 conecta, ahora dice de manera correcta golpes 1, 2 y 3
                    
                else:
                    print("golpe número", i+1, "no conecta")
            turno_usuario=False #despues de romperse el for, terminamos el turno
        elif menu=="3":
            if pociones_vida_usuario>0: #chequea que aún tengamos pociones
                if vida_usuario<=70:  #con esto cequeamos que si toma una pocion de vida teniendo mas de 70 de vida, no termine con vida sobrepasando 100.
                    pociones_vida_usuario-=1
                    vida_usuario+=30 #Esto es simple, toma la poción, se saca uno del valor de pociones_vida_usuario, se agrega vida. sin embargo, en una versión anterior, sin querer puse que las pociones sacaran vida; los gladiadores estaban bebiendo veneno
                    print("Recuperaste 30 de vida, te quedan ", pociones_vida_usuario, "pociones.")
                    turno_usuario=False
                else:
                    pociones_vida_usuario -=1
                    vida_usuario=100
                    print("Has tomado una poción de vida, tenes vida máxima")
                    turno_usuario=False

            else:
                print("Ya no tenes pociones de vida.") #me pareció injusto terminar el turno si no tiene mas pociones
        elif menu=="4": #la formula para las pociones de armadura es igual a la de vida, nada mas que subimos el valor de armadura y gastamos las pociones indicadas
            if pociones_armadura_usuario>0:
                pociones_armadura_usuario-=1
                armadura_usuario+=1
                print("Bebiste una poción de Armadura, resistirás el daño un poco mas. Armadura actual: ", armadura_usuario)
                turno_usuario=False
            else:
                print("Ya no tenes pociones de armadura.")
    elif turno_usuario==False: #cuando el usuario termina una acción y cambia el flag de turno_usuario a False, empieza el turno del enemigo, que en cada acción cambia la bandera a true, cambiando el turno al usuario otra vez.
        turno_enemigo=random.randint(1,3) #como el usuario no tiene control en las acciones del enemigo, decidí crear esta función. nos tira un número del 1 al 3, dependiendo de lo que sale tomará una acción. si alguna ya no puede hacerla, seguirá tirando números hasta caer en una acción válida
        if turno_enemigo==1:
            chance=random.randint(1,3) 
            if chance != 3:            # a diferencia del usuario, el enemigo solo tiene un 66.6% de chances de golpear
                    vida_usuario-= (daño_enemigo-armadura_usuario) #misma fórmula para el ataque del usuario se cumple acá
                    print("El Tigre del Quequén logra golpearte")
                    turno_usuario=True #en cada uno de estos cambiamos el turno al usuario
            else:
                    print("El Tigre ha fallado el golpe")
                    turno_usuario=True
        elif turno_enemigo==2:
            if vida_enemigo>70: #De esta manera nos aseguramos que el enemigo no pueda usar esta opción cuando tiene mas vida que 70, evitando que llegue a tener mas de 100 de vida
                continue
            elif pociones_vida_enemigo>0: #con esto chequeamos que solo tome pociones si tiene suficientes
                pociones_vida_enemigo-=1
                vida_enemigo+=30
                print("Tu contrincante bebe una poción de vida y recupera 30 puntos.")
                turno_usuario=True
            else:
                continue
        elif turno_enemigo==3: #al igual que con el usuario, las pociones de armadura funcionan de la misma manera
            if pociones_armadura_enemigo>0:
                pociones_armadura_enemigo-=1
                armadura_enemigo+=1
                print("El Tigre bebe una poción de armadura. Armadura actual: ", armadura_enemigo)
                turno_usuario=True
            else:
                continue

if vida_usuario<=0:
    print("El Tigre del Quequén ha probado ser un enemigo muy poderoso. Perdiste")
elif vida_enemigo<=0:
    print("Has logrado vencer a tu contrincante. Ganaste")






