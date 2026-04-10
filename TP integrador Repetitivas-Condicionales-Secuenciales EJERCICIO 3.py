#ALUMNO: LAUTARO BUSTILLO
"""turnos lunes"""
lunes1=""
lunes2=""
lunes3=""
lunes4=""

"""turnos martes"""
martes1=""
martes2=""
martes3=""

while True:
    usuario=input("ingrese su nombre de usuario: ")
    if usuario.isalpha(): #con esto chequeamos que el nombre de usuario tenga solo caracteres alfabéticos
        break
    else:
        print("ingrese un usuario válido")


if usuario != "": #nos aseguramos que entramos en el bucle si el nombre de usuario es válido
    while True:
        print("Bienvenido")
        menu=input("opciones:  \n"
        "1) Reservar turno  \n"
        "2) Cancelar turno(por nombre)  \n"
        "3)Ver Agenda del Día  \n"
        "4)Ver resumen General  \n"
        "5) salir\n")
        if  not menu.isdigit()  or menu  not in ["1", "2", "3", "4","5"]: #nos aseguramos que la elección del usuario para el menú sea de caracteres numéricos y que sea entre los números 1 al 5
            print("por favor, elija una opción válida")
            continue
        if menu =="1":
            while True:
                menu_reserva=input("elija qué día prefiere para su turno: \n"
                      "1) Lunes \n"
                      "2) Martes ")
                if  not menu_reserva.isdigit()  or menu_reserva  not in ["1", "2"]:
                    print("por favor, elija una opción válida")
                elif menu_reserva in ["1", "2"]:
                    while True:
                        nombre= input("Ingrese un nombre de 3 dígitos: ")
                        if len(nombre) != 3: #evitamos que el nombre sea de mas de 3 caracteres o menos
                            print("por favor elija un nombre de solo 3 dígitos.")
                        elif not nombre.isalpha():#evitamos que el nombre no tenga caracteres alfabéticos
                            print("Por favor, elija un nombre sin números.")
                        elif nombre.isalpha() and len(nombre)==3:
                            break
                    if menu_reserva == "1": #entramos a la opción del Lunes
                        if nombre in [lunes1, lunes2, lunes3, lunes4]: #chequeamos que el nombre ya no esté agendado en el Lunes
                            print("Ese nombre ya está agendado este día\n")
                            break
                        else: #por cada uno chequeamos si ese turno está vacío, si lo está lo llenamos con el nombre dado, sino sigue al siguiente turno
                            if lunes1 == "":
                             lunes1 = nombre
                            elif lunes2 == "":
                                lunes2 = nombre
                            elif lunes3 == "":
                                lunes3 = nombre
                            elif lunes4 == "":
                                lunes4 = nombre
                            else:
                                print("No hay turnos disponibles para el Lunes\n") #si llegamos a esta instancia, ya no hay turnos disponibles y terminamos el bucle, volviendo al menú
                                break
                        print("turno reservado\n") #teniendo en cuenta que si no hay espacio rompe el bucle, la unica manera de llegar a este print es si se agendó un turno de manera exitosa. Lo puse aquí para no tener que escribir el print en cada uno de los IF
                        break
                    if menu_reserva == "2": #entramos a la opción del Martes, la cual es igual a la del Lunes, pero con un turno menos 
                        if nombre in [martes1, martes2, martes3]:
                            print("Ese nombre ya está agendado este día")
                            break
                        else:
                            if martes1 == "":
                             martes1 = nombre
                            elif martes2 == "":
                                martes2 = nombre
                            elif martes3 == "":
                                martes3 = nombre                        
                            else:
                                print("No hay turnos disponibles para el Martes\n")
                                break
                        print("turno reservado\n")
                        break
        if menu=="2": #para eliminar un turno es muy parecido en agregar uno, nada mas que los chequeos son para resetear el estado de ese día en lugar de agregar las letras
            while True:
                menu_cancelacion=input("elija el día el cual agendó el turno: \n"
                      "1) Lunes \n"
                      "2) Martes ")
                if  not menu_cancelacion.isdigit()  or menu_cancelacion  not in ["1", "2"]:
                    print("por favor, elija una opción válida")
                elif menu_cancelacion in ["1", "2"]:
                    while True:
                        nombre= input("Ingrese un nombre de 3 dígitos: ")
                        if len(nombre) != 3:
                            print("por favor elija un nombre de solo 3 dígitos.")
                        elif not nombre.isalpha():
                            print("Por favor, elija un nombre sin números.")
                        elif nombre.isalpha() and len(nombre)==3:
                            break
                    if menu_cancelacion == "1":
                        if nombre  not in [lunes1, lunes2, lunes3, lunes4]: #chequeamos si el nombre válidado anteriormente esta agendado en este día
                            print("Ese nombre no está agendado este día\n")
                            break
                        else:
                            if lunes1 == nombre: #la fórmula funciona igual que en agendar un turno, la diferencia es que en lugar de ver si esta vacío, chequea si esta ese nombre en el turno, si lo esta cambiamos el estado del mismo a vacío ("")
                             lunes1 = ""
                            elif lunes2 == nombre:
                                lunes2 = ""
                            elif lunes3 == nombre:
                                lunes3 = ""
                            elif lunes4 == nombre:
                                lunes4 = ""
                       
                        print("turno cancelado\n")
                        break
                    if menu_cancelacion == "2":
                        if nombre not in [martes1, martes2, martes3]:
                            print("Ese nombre no está agendado este día")
                            break
                        else:
                            if martes1 == nombre:
                             martes1 = ""
                            elif martes2 == nombre:
                                martes2 = ""
                            elif martes3 == nombre:
                                martes3 = ""                      
       
                        print("turno cancelado\n")
                        break
        if menu=="3":
            while True:
                menu_agenda=input("elija el día el cual agendó el turno: \n"
                      "1) Lunes \n"
                      "2) Martes ")
                if  not menu_agenda.isdigit()  or menu_agenda  not in ["1", "2"]:
                    print("por favor, elija una opción válida")
                elif menu_agenda in ["1", "2"]:
                    if menu_agenda == "1":
                        if lunes1=="": #en cada turno tenemos dos IF, si esta vacío, nos dirá que esta disponible.
                            print("Lunes Turno 1: Disponible")
                        elif lunes1 != "": #de lo contrario, si ese turno tiene algo escrito, , va a imprimir el nombre agendado
                            print("Lunes turno 1: ", lunes1)
                        if lunes2=="":
                            print("Lunes Turno 2: Disponible")
                        elif lunes2 != "":
                            print("Lunes turno 2: ", lunes2)
                        if lunes3=="":
                            print("Lunes Turno 3: Disponible")
                        elif lunes3 != "":
                            print("Lunes turno 3: ", lunes3)
                        if lunes4=="":
                            print("Lunes Turno 4: Disponible")
                        elif lunes4 != "":
                            print("Lunes turno 4: ", lunes4)
                        break
                    if menu_agenda == "2":
                        if martes1=="":
                            print("Martes Turno 1: Disponible")
                        elif martes1 != "":
                            print("Martes turno 1: ", martes1)
                        if martes2=="":
                            print("Martes Turno 2: Disponible")
                        elif martes2 != "":
                            print("Martes turno 2: ", martes2)
                        if martes3=="":
                            print("Martes Turno 3: Disponible")
                        elif martes3 != "":
                            print("Martes turno 3: ", martes3)
                     
                        break
        if menu=="4":
            #creamos dos variables para contar los turnos ocupados de cada día
            cont_ocup_lunes=0

            cont_ocup_martes=0
         

            if lunes1!= "":#con esto chequeamos que, si cada turno NO ESTA VACÍO, lo contamos como ocupado y le sumamos uno a la variable de ese día, en este caso siendo lunes
                cont_ocup_lunes +=1
            if lunes2!= "":
                cont_ocup_lunes +=1
            if lunes3!= "":
                cont_ocup_lunes +=1       
            if lunes4!= "":
                cont_ocup_lunes +=1

            if martes1!= "":
                cont_ocup_martes +=1
            if martes2!= "":
                cont_ocup_martes +=1
            if martes3!= "":
                cont_ocup_martes +=1 
            #para contar turnos disponibles, simplemente hacemos los turnos totales (4 en Lunes, 3 en Martes) y le restamos el valor que quedó en las variables de los turnos ocupados    
            cont_disp_lunes=4-int(cont_ocup_lunes)
            cont_disp_martes=3-int(cont_ocup_martes)
            print("Lunes: \nTurnos Ocupados:", cont_ocup_lunes, )
            print("Turnos Disponibles: ", cont_disp_lunes)
            print("Martes: \nTurnos Ocupados: ", cont_ocup_martes)
            print("Turnos Disponibles: ", cont_disp_martes)
            
            if cont_ocup_lunes>cont_ocup_martes:
                print("Día con mas turnos: Lunes, con " , cont_ocup_lunes, " turnos.")
            elif cont_ocup_lunes<cont_ocup_martes:
                print("Día con mas turnos: Martes, con ", cont_ocup_martes, "turnos.")
            elif cont_ocup_martes==cont_ocup_lunes:
                print("Ambos días tienen la misma cantidad de turnos.")
        

        if menu=="5":
            print("Hasta luego.")
            break
         
                 
                

                        
                        
            


