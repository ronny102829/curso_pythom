# # lista=["abeel","anttony","miguel"]
# # diccionario={"NOMBRE":"ANTONIO","EDAD":15,"SEXO":False}
# # print(lista[1:])
# lista=["abeel","anttony","miguel"]
# diccionario={"NOMBRE":"ANTONIO","EDAD":15,"SEXO":False}
# print(diccionario["nombre"])
# # ejemplos
# texto="hola"
# ista_texto=list(texto)
# lista2=[e for e in texto]
# print(lista2)

# texto_largo="hola como est<an vienvenidos al salon "
# nueva_lista=texto_largo.split(" ")
# print(nueva_lista)
# texto_largo="este es un texto largo chiquitas y chiquiotos"
# nuevo_texto=texto_largo.split(" ")
# print("".join(nuevo_texto))# Definir la lista de alumnos
# alumnos = [
#     {"nombre": "Juan", "apellido": "Perez", "edad": 20},
#     {"nombre": "Maria", "apellido": "Gomez", "edad": 22},
#     {"nombre": "Pedro", "apellido": "Lopez", "edad": 19},
#     {"nombre": "Abel", "apellido": "Gonzalez", "edad": 21}
# ]

# # Insertar los datos de Antoni al final de la lista
# alumnos.append({"nombre": "Antoni", "apellido": "Martinez", "edad": 23})

# # Eliminar los datos de Abel si existe en la lista
# alumnos = [alumno for alumno in alumnos if alumno["nombre"] != "Abel"]

# # Buscar y mostrar el alumno en la posición 4 de la lista
# if len(alumnos) >= 4:
#     alumno_posicion_4 = alumnos[3]
#     print("Alumno en la posición 4:")
#     print("Nombre:", alumno_posicion_4["nombre"])
#     print("Apellido:", alumno_posicion_4["apellido"])
#     print("Edad:", alumno_posicion_4["edad"])
# else:
#     print("No hay suficientes alumnos en la lista para mostrar al alumno en la posición 4.")

# # adto primitivo
# # nombre="avel"
# # otro_nombre=nombre
# # print(id(nombre))
# # print(id(otro_nombre))
# lista_original=[1,2,3,4]
# copia_lista=lista_original

# lista_original[-1]=15

# print(copia_lista)
# lista=[1,6,2,5,8,23]
# print(lista,end="\n ordenar\n")
# lista.sort()
lista=[3,235,1,5,6,8,54,2]
copia_lista=lista.copy()
copia_lista.sort()
print(lista)
print(copia_lista)