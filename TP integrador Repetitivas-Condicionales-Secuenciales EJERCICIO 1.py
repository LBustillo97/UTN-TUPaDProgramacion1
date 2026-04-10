#Alumno: Lautaro Bustillo
while True:
    nombre=input("Ingrese su nombre: ")
    if nombre.isalpha(): #chequeamos que el nombre contenga solo caracteres alfabeticos
        break
    else:
        print("error, por favor ingrese un nombre válido")


while True:
    numero_productos= input("por favor ingrese la cantidad de productos: ")
    if numero_productos.isdigit() and int(numero_productos)>0: #con esto chequeamos que numero_productos contenga caracteres numéricos y que el número no sea negativo o cero
        numero_productos= int(numero_productos) #cambiamos el formato de numero_productos de STR a INT
        break
    else:
        print("por favor ingrese un número válido") 

#creamos las variables del precio total con descuento y sin descuento
total_descuento= 0 

total_sin_descuento=0




for i in range (numero_productos): #empieza el bucle acorde a la cantidad de productos que nos dieron antes, por eso cambiamos numero_produsctos de STR a INT
    while True:
        print("producto número ", i+1, ":" ) #le decimos al usuario cual producto esta ingresando. agrego el +1 porque sino el primer print va a decir "producto número 0"
        precio= input("por favor indique el precio del producto: ")
        if precio.isdigit() and int(precio)>=0: #igual que antes, chequeamos que lo ingresado sea un número y que no sea negativo
            precio= int(precio) #lo pasamos a INT para que podamos sumarlo en los totales
            total_sin_descuento += precio
            break
           
        else:
            print("Por favor ingrese un número válido")

    while True:
        check_descuento=input("¿el producto tiene descuento?) S/N   ").lower() #le pedimos si tiene descuento el producto. el lower() hace que la letra que ingrese el usuario SIEMPRE SEA MINUSCULA
        if check_descuento in["s", "n"]: #chequea que el usuario haya elegido una opción válida
            break
        else:
            print("Ingrese una letra válida")
        
    if check_descuento== "s": #solo hace falta hacer el IF de una de las dos opciones
        total_descuento+= precio*0.9
    else:
        total_descuento+= precio


print(total_descuento, total_sin_descuento)
           
     
print("Nombre Cliente: " , nombre ) 
print("Cantidad de productos: ", numero_productos)
print("Monto total con descuentos: ", total_descuento)
print("Monto toal sin descuentos: ", total_sin_descuento)
print("Total ahorrado: ", total_sin_descuento-total_descuento)
print("promedio por producto: ", total_descuento/numero_productos)
 




                         
                         




