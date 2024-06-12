`## funciones 
matemaTICA,EMTE ES UNA FUNCION ES UNA OPERACION K TOMANA UNA O MNAS VALORES  LLAMANDAS `ARGUMENTOS` Y PRODUCE UN VALOR DOMINANTE `RESULTADO` 
>[!NOTE]
todos los lenguajes de programacion tiene funciones incorporads (`funciones imternas `) y fdunciones credas por el usuario (`funciones externas `) 
enn programacion ua funcion es un subprograma , es una estructura k nos permite agrupar codigas y sus prinsi´pales objetivo son: 
-`NO REPETIR` fracmentos de codigo
-`REUTILIZAR`
## estructura de uan fuincion 
una fincion biene `definida` poor un `nombre` y sus`parametros`.-
una ves creada la funcion podemos crear podemos solicitar su ejecucion `invocacion la funcion por su `nombre`
## definir una funcion en python 
paera definir funcioners en python primero utilisamos la palabra reserbada `def` segida por el `nombre` der kla funcion  . A CONTINUACIONN ESPISIFICAREMOS 
los `parametros` con `()` si es una funcion sin parametros , `(a)` si es una funciobn com parametros , si se tubira mas de un prametros iran separados por 
`,`finalizaremos la linia con `:` ,en la sigiente linia del valor identado, comensara el`cuerpo` de la funcion (micro programa) que resultado con la palabra reservada `returbn`
>[!TIP]
comoretorno tambien se puede utilisar la `funcion interna `, `print`, `()`, para depuracion de codigo no esrecomendable usarlo en produccion . 

**ejemplo:**
```python
def saludo():
    saludo="hola chivo"
    saludos_dos="como estas"
    return f"{saludo}, {saludo_dos}"
print(saludo)
```

## invocar una funcion
para invbocar , (o llamr, ejecutar) una funcion solo tendremos k escribir e `nombre` de la funcion segida por parentisis .
```python
def saludo():
    return 1 
    uno()
```

>[!WARNING]
>no confundir `print()` con `reutrn` no es ´permitido usurlao fuera de su contexto , y `print()`  solo mostrara del literal por terminal
*ejemplo:**
*el archivo `lectur.py`
## retornandop multiples valores
el secretyo es aserlo mediante un tipo de dato estructurado 
`


## parametros y argumentodos
si uan funciona  no dispusiera de valores b de entrada estaria limitadea en su actuacion. es por ello que los`parameteos` no permiten variar losd datos que consume una funcion
para obtener distintos resultados
**ejemplo**

*crear una funcion que resive un valor numerico y retoorna su raiz cuadrada*
```python
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este cso, el valor 4 es un argumento de la funcion
sqrt(4)
```
cuandop llamamos  a un funcion con ` argumentos`, los valores de estos argumentos  se copian en los correpondientes `parametros`,dentro de las funcion.
```python
def ejem(a,b,c):
    return a+b+c
ejem(4,5,6)
```
### argumentos nominales 
en esta aproximamcion  los argumentosno sosn copiados en un orden espesifico sino que  **se asigna por nombre acada perimetro** . ello nos evita el problema de conocer o reconocer cual  es el orden  e los parametros  en la  funcion. para utilizarlo, basta con ralisar un asignacion de acada argumento en la propia llamada  de la funcion.

**ejemplo** 
```python
def  build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la famila {familia},
    con {num_core} cores y una 
    frecuencia  de {frecuencia}
    """)
# haciendo uso  de argumentos dominales 
build_cpu("intel",4,2,7)
build_cpu(num_core=4,familia="intel", frecuencia=2.7)
```
### argumentos posicionales 
los argumnetos son copias en un orden espesifico, en ste caos de bemos conocer o recordar cual es el orden de los parametros .

**ejemplo**
```python
def  build_cpu(familia,num_core,frecuencia):
    print(f"""
        la cpu es de la famila {familia},
        con {num_core} cores y una 
        frecuencia  de {frecuencia}
    """)
#haciendo uso  de argumentos dominales 
build_cpu("intel",4,2,7)
```
### parametrsiopor defecto
es posible spisificar **valores por defecto** en losn parametros de una funcion , en el caso que no se proporcione un valor al argumento  en la llmada a la funcion, el paraetro cvorrespondiente  tomara el valor defenidom por defecto .

**ejemplo**
```python
def alumnos(nom,app,estado="aprobado"):

alumnos("ruth","castillo")
alumnos("anthony","crucez","desaprovado")
```

###  desenpaquetado/ empequetado de argumentos(tarea)

## funciones internas de python(tarea)