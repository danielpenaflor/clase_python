'''

print("Hola, causitas")

#listas
#tuplsa
#conjunto
#diccionarios

nombres = ["Aldo", "Alberto", "Alejandro", "Alejandro", "Edi"]

for x in nombres:
    print(x)


datos = [15, 13, 9, True, False, "Maria del Pindongal", "41824687"]

for data in datos:
    print (data)

print("=========despues de la ejecucion=================")

datos.append("Daniel Romulano")
for data in datos:
    print (data)
print("=========yapa=================")

print (datos[2])

print("=========despues de la ejecucion=================")

print(datos[5])

print("=========despues de la ejecucion=================")

datos.append(0)

print("=========despues de la ejecucion=================")

datos.insert(3,"Francisco")



for y in datos:
    print(y)

datos = [15, 13, 9, True, False, "Maria del Pindongal", "41824687"]
cantidadElementos = len(datos)
print(cantidadElementos)

datos = [15, 13, 9, True, False, "Maria del Pindongal", "41824687"]

print(len(datos))
datos.remove(True)
print("============================pera====================================")
print(len(datos))
print(datos)
print("Ultimo casillero es el numero ", len(datos)-1)
print("============================pera====================================")
cantidadElementos = len(datos)
print("la posicion del ultimo valor es  ", len(datos)-1)


datos =  [15, 13.9, True, "Francisco", False, "Maria del Pindongal", "41824687", 15, 13, True, False, "Francisco Javier", False, "Maria del Pindongal", "41823759", 18, 120, True, "Francisco 3ero", False, "Maria Pindonga"]

datos_sin_maria_del_pindongal = [x for x in datos if x != "Maria del Pindongal"]
print (datos)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxoooxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(datos_sin_maria_del_pindongal)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxoooxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("la canrtidad de espacios ocupados es de  ", len(datos_sin_maria_del_pindongal))
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxoooxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("el ultimo valor esta en el sitio ordinal numero  ", len(datos_sin_maria_del_pindongal) -1)
print ("fin")

'''
#Si mi lista es:
datos = [15, 13.9, True, "Francisco", False, "Maria del Pindongal", "41824687", 15, 13, True, False, "Francisco Javier", False, "Maria del Pindongal", "41823759", 18, 120, True, "Francisco 3ero", False, "Maria Pindonga"]


#Y deseo eliminar "Maria del Pindongal":
datos_sin_maria_del_pindongal = [x for x in datos if x != "Maria del Pindongal"]
print(datos_sin_maria_del_pindongal)




'''
coordenadas = (422528, 485275248, 268584157, -48257842)

for punto in coordenadas:
    print(punto)

print("============despues de la ejecucion=================")
'''