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
```python
