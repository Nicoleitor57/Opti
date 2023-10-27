import random

listaInstancias = [[5,7,6,10],[8,12,10,20],[13,18,20,30],[19,23,30,40],[24,30,40,50],
                    [32,38,50,65],[39,45,65,80],[46,54,80,95],[54,65,95,110],[65,72,110,125],
                    [72,81,125,145],[82,92,145,165],[92,101,165,185],[102,111,185,205],[112,131,205,225]
                    ]
a = 0
while a < 3:
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
    bodegasAzul = []
    bodegasVerde =[]
    tiendas = []
    i = 0
    while i < I:
        x = random.randint(0,600)
        y = random.randint(0,600)
        if x < 225 or x > 375 or y < 225 or y > 375:
            if x <= 100 or x >= 500 or y <= 100 or y >= 500:
                bodegasAzul.append([x,y])
            elif ((x < 500 and x > 100) or (y < 100 and y > 500)):
                bodegasVerde.append([x,y])
            i += 1
    j = 0
    while j < J:
        x = random.randint(225,375)
        y = random.randint(225,375)
        tiendas.append([x,y])
        j += 1
    print("bodegasAzul: ",bodegasAzul)
    print("bodegasVerde: ",bodegasVerde)
    print("tiendas: ",tiendas)
    
    #cada tienda satisfecha por almenos una bodega
    #costo de transporte de bodega i al tienda j = distancia euclidiana * 1,25
    #costo de instalacion de bodega i = numero aleatorio entre 1000 y 3000
    #capacidad de bodega i = numero aleatorio entre 2 y J/3
    #instalar bodega en almenos 40% de I
    
    #matriz de costos de transporte
    bodegas = bodegasAzul + bodegasVerde
    costos = []
    i = 0
    while i < I:
        costos.append([])
        j = 0
        while j < J:
            costo = ((bodegas[i][0]-tiendas[j][0])**2+(bodegas[i][1]-tiendas[j][1])**2)**(1/2)*1.25
            costos[i].append(costo)
            j += 1
        i += 1
    print("costos de transporte: ",costos)
    
    #matriz de emisiones por transporte, emisiones = distancia recorrida(distancia aritmetica) * 1.5
    emisiones = []
    i = 0
    while i < I:
        emisiones.append([])
        j = 0
        while j < J:
            emision = ((bodegas[i][0]-tiendas[j][0])**2+(bodegas[i][1]-tiendas[j][1])**2)**(1/2)*1.5
            emisiones[i].append(emision)
            j += 1
        i += 1
    print("emisiones por transporte: ",emisiones)
    
    
    
    #lista de costos de instalacion
    costosInstalacion = []
    i = 0
    while i < I:
        costo = random.randint(1000,3000)
        costosInstalacion.append(costo)
        i += 1
    print("costos de instalacion: ",costosInstalacion)
    
    #lista de capacidades de bodegas
    capacidades = []
    i = 0
    while i < I:
        capacidad = random.randint(2,int(J/3))
        capacidades.append(capacidad)
        i += 1
    print("capacidades de bodegas: ",capacidades)
    
    """
    #lista de bodegas instaladas
    bodegasInstaladas = []
    i = 0
    while i < I:
        bodegasInstaladas.append(0)
        i += 1
    print("bodegas instaladas: ",bodegasInstaladas)
    
    #lista de tiendas satisfechas
    tiendasSatisfechas = []
    j = 0
    while j < J:
        tiendasSatisfechas.append(0)
        j += 1
    print("tiendas satisfechas: ",tiendasSatisfechas)
    
    #lista de bodegas con capacidad
    bodegasConCapacidad = []
    i = 0
    while i < I:
        bodegasConCapacidad.append(0)
        i += 1
    print("bodegas con capacidad: ",bodegasConCapacidad)
    
    #lista de bodegas con capacidad y no instaladas
    bodegasConCapacidadNoInstaladas = []
    i = 0
    while i < I:
        bodegasConCapacidadNoInstaladas.append(0)
        i += 1
    print("bodegas con capacidad y no instaladas: ",bodegasConCapacidadNoInstaladas)
    
    #lista de tiendas no satisfechas
    tiendasNoSatisfechas = []
    j = 0
    while j < J:
        tiendasNoSatisfechas.append(0)
        j += 1
    print("tiendas no satisfechas: ",tiendasNoSatisfechas)
    """
    
    a += 1
    

#grupo 23, se uso la asignacion del grupo 3 A=1,B=3,C=a

#minimizar los costos de transporte e instalacion, emisiones <=500 * J

#variables de decision
#Xij = costo de transporte de bodega i al tienda j
#Yi = costo de instalacion de bodega i
#Bi = 1 si bodega i es instalada, 0 si no
#Cij = 1 si bodega i satisface tienda j, 0 si no 


#funcion objetivo
#min Z = sumatoria de i=1 hasta I sumatoria de j=1 hasta J (Xij*Cij) + sumatoria de i=1 hasta I (Yi*Bi)

#restricciones
#emisiones <= 500 * J

