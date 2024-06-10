# tipod de datos estructurados(tda - tipos de datos abstractos)
```python
#lista
lista=["nombre",20,8,6,5,False,["texto",.2]]
#tuplas
tupla=("abel",20,5.2,False,[])
#tupla-  su valoeres o elementales no pueden ser modificados o eliminados
tupla=("abel",20,5.2,False[]) 
#diccionarios o objetos
#los diccionarios almacenan los datos clave :valor
diccionario={"NOMBRE":"ANTONIO","EDAD":15"SEXO" False}
```
-[!TIP]
-los tipos de datos estructurdos pueden almacenar otros tipos de datos estructurados 
```python
lista_alumno=[
    {
        "nombre":"abel",
        "edad":13
        "amigos"
    }.{
        "nombre":"ruth",
        "edad":15
    },{
        "nombre":"jose ma"
        "edad":17
    }.{
        "nombre":"ronny"
        "edad":15      
]
```
## metodos
### 1.convertir texto a lista 
``PYTHON
# METODO LISTA
texto="hola"
list(texto)
#["H","O","L","A"]

# metodo split
texto="hola alumnitos lindos"
texto.split(",")
# metodo join
texto_largo="este es un texto largo chiquitas y chiquiotos"
nuevo_texto=texto_largo.split(" ")
print("".join(nuevo_texto))
## metodo append- esd un metodo que me permite agregar elemtos al final de uan liasta 
lista=["hola"]
lista.append("mundo")
print(lista)
## medo insert- es el metodo que  me permite agregar elñementos en cuaslwuiier parte de la lsiata 
lista_nombre=["edith","ruth","luz"]
lista_nombre .insert(0,"antonny")
### 3. eliminar eklelmntos de unan listza
# metodo pop. est es el m,etodo k eliminba nel ultimo elemento de una LIASTA ES EL CONMTRADIODE APPEND
lista_nombre=["edith","ruth","luz"]
lista_nombre .POP ()
# primera manera - metodo remove - ete metodo elimina por el nombre  por el elmento que conside dentro de la lista 
lista_nombre=["edith","ruth","luz"]
lista_nombre .remove("ruth")
### 4. buscar un elemto en una lista
```python
lista_nombre=["edith","ruth","luz"]
indice=lista_nombre.index("ruth")
print(lista_nombre[indice])
### 5. comparcion de listas
 podemos hacer uso de los operadores de compaRACIONPARA PARA COMPARAR LISTAS 
 **EJEM**
 ```PYTHON
 compara=[1,2,3]>[1,2,4]
 # 1 no porque son iguales en ambas listas 
 # 2 no porque son iguales en ambas listas
 # 3 evalua k es menor k 4
 # 4 enotonces la primera lis es menos la segunda lista 
 print(compara)
 # salida:

 ### 6 cuidado de las copis 
 ### 7. fe de erratas(actualisar lista)
 ```python
 lista=[1,3,4,5,6]
 lista=[0]=2
 print(lista)


# DOCENTE 
## YO COMO DOCENTE DE LA INSTTITUTO "JOSE MARIA ARGEDAS"
## DESEO K LOS ALUNNOS PUEDAR VER SUS NOTAS (SIN K PUEDAN MODIFICAR ESA NOTA) 
### Y DE TAL MANERE , K ELLOS PUEDAN MEJORA EN ESA AREA 


### 8. lista y diccionario por comprecion 
es una tecnica pythonica que nos permite crear listas ty diccionariosen una solo linia combinado bucles y diccionarios
[!NOTE]
**vlc** value loop condicion - valor bucle condiccion 
```python 
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={}
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)
# aplicando el vlc 
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={amigo: len(amigo)for amigo  in lista_amigos}
print(diccionario)
