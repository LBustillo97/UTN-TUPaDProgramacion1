#ALUMNO: LAUTARO BUSTILLO
energia=100
tiempo= 12
cerraduras_abiertas=0
alarma=False
codigo_parcial=""
contador_forceo=0


while True:
    usuario=input("ingrese su nombre, agente: ")
    if usuario.isalpha(): #Con esto chequeamos si el nombre del usuario es válido, usando solo caracteres lafabéticos
        break
    else:
        print("ingrese un nombre válido")
print("Bienvenido, agente ", usuario,", se le ha asignado la misión de abrir la bóveda del Dr Malito. \n"
"Tiene 12 minutos para hacerlo, tenga cuidado de no forcejear las cerraduras mas de 2 veces, o el sistema de seguridad se activará.  \n"
"Mucha suerte agente. ")

if usuario !="": #ya habiendochequeado que el nombre sea válido, con esto empezamos el juego, el cual no empieza si el nombre no fué validado
    while energia>0 and tiempo>0 and cerraduras_abiertas!=3:
        if 0<tiempo<5 and alarma==True: #este aviso es para notificar al jugador que le queda poco tiempo al haber activado la alarma
            print("Debo apurarme, si el contador llega a 3 minutos el sistema de seguridad me atrapará por haber activado la alarma.")
        
        if alarma==True and tiempo <= 3: #de esta manera generamos la condición de derrota por alarma, rompiendo el while.
            break
        print("Ahora mismo tenemos ", energia, " de energía y  ",tiempo, " minutos." )
        print("Tenemos ", cerraduras_abiertas, " cerraduras abiertas") #estos prints son para notificar al usuario de sus recursos y avance en la misión
        menu = input(
            f"ok ¿qué hacemos ahora? \n"
            f"1) Forzar cerradura, esto nos costará 20 de energía y 2 minutos "
            f"(cantidad de veces hechas = {contador_forceo} veces)\n" #de esta manera ya le avisamos al jugador la cantidad de veces que ha forcejeado la cerradura
            f"2) Hackear el panel de seguridad, esto nos costará 10 de energía y 3 minutos \n"
            f"3) Meditar un poco y descansar la mente, esto me dará energía pero perderé 1 minuto \n")
        if  not menu.isdigit()  or menu  not in ["1", "2", "3"]: #con esto chequeamos que la opción del usuario para el menú sea válida. Chequeamos si son caracteres númericos y si esta en la lista en 1; 2 o 3
            print("por favor, elija una opción válida")
            continue
        elif menu=="1":
            if (energia-20)<0: #de esta manera evitamos que el usuario use opciones sin tener la energía suficiente
                print("No tengo suficiente energía para esto")
                continue
            elif alarma==True: #con esto evitamos que usen devuelta forcejear la cerradura despues de haber activado la alarma
                print("Las cerraduras estan bloqueadas, ya no podré fotzarlas, debo elegir otra opción.")
            elif contador_forceo >=2 and energia>=40: 
                energia -=20
                tiempo-=2
                contador_forceo+=1
                print("Oh no, he activado la alarma, trabando la cerradura. Debo apurarme o los sistemas de seguridad me acabarán")
                alarma=True
            elif alarma==False:
                if energia<40 and energia>=20: #con esto  activamos el riesgo de alarma
                    energia -= 20
                    tiempo -= 2
                    contador_forceo += 1
                    codigo=input("Debo tener cuidado, si no elijo el siguiente número bien, se activará la alarma\n" \
                    "Debo elegir entre los números 1, 2 o 3: \n" \
                    "¿Cuál elijo?   ")
                    while codigo not in ["1", "2", "3"]: #con esto evitamos que elijan caracteres por fuera de las opciones dadas
                        codigo=input("NO, debo elegir entre el 1, 2 o 3, debo concentrarme.")
                    if codigo=="3":
                        print("Diantres, he activado la alarma, debo apresurarme.")
                    else:
                        print("Lo logré, pero debo tener mas cuidado en el futuro")
                        cerraduras_abiertas +=1
                else:
                    print("¡Presto! Cerradura abierta") #habiendo hecho opciones para cada siituación, la única que queda es si forcejea sin problemas
                    energia -= 20
                    tiempo -= 2
                    contador_forceo += 1
                    cerraduras_abiertas+=1
            elif alarma==True:
                print("Las cerraduras estan bloqueadas, ya no podré fotzarlas, debo elegir otra opción.")
        elif menu=="2":
            if (energia-10)<0:
                print("No tengo suficiente energía para esto")
                continue
            energia -= 10
            tiempo -= 3
            print("Debo ingresar 4 codigos alfabéticos, una vez que consiga terminar el código con 8 letras podré abrir una cerradura, pero cada intento sólo me deja agregar 4")

            for i in range(4):
                letra=input("Debo ingresar la letra número " + str(len(codigo_parcial)+1) + ": ") #me pareció una buena idea decirle al usuario cuantas letras se han ingresado
                while not letra.isalpha() and len(letra) != 1: #de esta manera evitamos que pongan caracteres no alfabéticos o que agreguen mas de una letra
                    letra=input("No, debo agregar una letra, y solo una: ")
                codigo_parcial +=letra
            print("perfecto, 4 letras agregadas")
            if len(codigo_parcial)==8: #si ya se agregaron 8 letras despues de haber pasado por el FOR, se desbloquea una cerradura y se reinicia el código_parcial para evitar que spameen esta opción para ganar
                print("Perfecto, 8 letras agregadas de manera sastifactoria")
                codigo_parcial=""
                cerraduras_abiertas+=1
        elif menu=="3":
            if alarma==True: #con esto chequeamos la alarma para ver cuál de los dos descansos se consigue
                energia+=5
                tiempo-=1
                print("Debo descansar mi mente y enfocarme, pero no logro hacerlo de manera adecuada culpa de esa maldita alarma.")
                print("se recuperó 5 de energía.")
            else:
                energia+=15
                tiempo-=1
                if energia>100:
                    energia=100
                print("perfecto, pude calmar mis nervios y recuperar energía, aunque no debo descansar tanto, el tiempo es crucial en esta misión.")

if cerraduras_abiertas==3:
    print("Perfecto, he logrado abrir la bóveda y robar los planes del Dr Malito. Ganamos, baby")
if energia <=0 or tiempo<= 0 and cerraduras_abiertas<3:
    print("La bóveda del Dr Malito ha demostrado ser más dfifícil de lo esperado, he perdido mi groove, baby....y este juego")
if alarma and tiempo<=3:
    print("Al parecer mis drones de seguridad han logrado atraparlo, agente", usuario, ", ahora nada ni nadie pordrá detenerme en mi plan de conseguir.....1 MILLÓN DE DOLARES (musica de suspenso)----Partida perdida")


            
