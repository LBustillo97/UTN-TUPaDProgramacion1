dias_climas=[
[21, 26], #lunes
[18, 22], #martes
[25, 31], #miercoles
[27,35],  #jueves
[10, 15], #viernes
[21,27],  #sabado
[18, 29]  #domingo
]

#creamos variables para sumar el total de las maximas y minimas
minimas=0
maximas=0

for i in dias_climas:#hacemos el bucle que pasa por todos los dias de la lista
    minimas+=i[0]#sumamos las temperaturas minimas
    maximas+=i[1]#sumamos las temperaturas maximas

promedio_minimas=minimas/7
print("El promedio de las temperaturas mínimas de la semana es ",promedio_minimas)
promedio_maximas=maximas/7
print("El promedio de las temperaturas maximas de la semana es ", promedio_maximas)


lista_amp_temp=[]#hacemos una lista donde vamos a agregar la amplitud termica de cada dia

for i in dias_climas:#hacemos el bucle que pasa por todos los dias de la lista
    amp=i[1]-i[0]#hacemos la resta entre la maxima y la minima de cada día
    lista_amp_temp.append(amp) #agregamos el valor a la lista de amplitudes termicas

amp_max=max(lista_amp_temp) #creamos una variable para guardar la amplitud maxima


#acá hacemos condicionales los cuales nos ayudarán a ver qué día tiene la amplitud mas grande
if lista_amp_temp.index(amp_max)==0:#usando el valor de amp_max, chequeamos cada elemento en la lista de lista_amp_temp, si coinciden y la posición coincide con el número (en este caso 0 por lunes), imprimimos el mensaje
    print("el día con mayor amplitud térmica es Lunes con ", amp_max)
elif lista_amp_temp.index(amp_max)==1:
    print("el dia con mayor amplitud térmica es martes con ", amp_max)
elif lista_amp_temp.index(amp_max)==2:
    print("el día con mayor amplitud térmica es miercoles con ", amp_max)
elif lista_amp_temp.index(amp_max)==3:
    print("el día con mayor amplitud térmica es jueves con ", amp_max)
elif lista_amp_temp.index(amp_max)==4:
    print("el día con mayor amplitud térmica es viernes con ", amp_max)
elif lista_amp_temp.index(amp_max)==5:
    print("el día con mayor amplitud térmica es sabado con ", amp_max)
elif lista_amp_temp.index(amp_max)==6:
    print("el día con mayor amplitud térmica es domingo con ", amp_max)