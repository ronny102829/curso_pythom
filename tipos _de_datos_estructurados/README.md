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

