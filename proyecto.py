import random

listaInstancias = [[5,7,6,10],[8,12,10,20],[13,18,20,30],[19,23,30,40],[24,30,40,50],
                    [32,38,50,65],[39,45,65,80],[46,54,80,95],[54,65,95,110],[65,72,110,125],
                    [72,81,125,145],[82,92,145,165],[92,101,165,185],[102,111,185,205],[112,131,205,225]
                    ]
a = 0
while a < 1:
    Instancias = listaInstancias[a]
    minI = Instancias[0]
    maxI = Instancias[1]
    minJ = Instancias[2]
    maxJ = Instancias[3]
    print("instacia numero: ",a+1)
    if a < 5:
        print("instancia pequeña")
    elif a < 10:
        print("instancia mediana")
    else:
        print("instancia grande")

    I = random.randint(minI,maxI)
    J = random.randint(minJ,maxJ)
    operacion = random.randint(20,70)
    
    print("I: ",I)
    print("J: ",J)
    print("emisiones por operacion de la bodega: ",operacion)
    
    
    #generar I puntos de bodegas en un plano 600x600 excluyendo centro de 150x150
    #generar J puntos de tiendas en el centro 150x150 del plano 600x600
    bodegas = []
    tiendas = []
    i = 0
    while i < I:
        x = random.randint(0,600)
        y = random.randint(0,600)
        if x < 225 or x > 375 or y < 225 or y > 375:
            bodegas.append([x,y])
            i += 1
    j = 0
    while j < J:
        x = random.randint(225,375)
        y = random.randint(225,375)
        tiendas.append([x,y])
        j += 1
    print("bodegas: ",bodegas)
    print("tiendas: ",tiendas)
    
    #cada tienda satisfecha por almenos una bodega
    #costo de transporte de bodega i al tienda j = distancia euclidiana * 1,25
    #costo de instalacion de bodega i = numero aleatorio entre 1000 y 3000
    #capacidad de bodega i = numero aleatorio entre 2 y J/3
    #instalar bodega en almenos 40% de I
    
    
    
    a += 1
    

#grupo 23, se uso la asignacion del grupo 3 A=1,B=3,C=a

#minimizar los costos de transporte e instalacion, emisiones <=500 * J

#variables de decision
#Xij = costo de transporte de bodega i al tienda j
#Yi = costo de instalacion de bodega i

#funcion objetivo
#min Z = sumatoria de i=1 hasta I sumatoria de j=1 hasta J (Xij) + sumatoria de i=1 hasta I (Yi)

#restricciones
#emisiones <= 500 * J

