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
 Las funciones internas de Python son funciones predefinidas que están disponibles para su uso en cualquier programa de Python sin necesidad de importar ningún módulo adicional. Algunas de las funciones internas más comunes en Python incluyen:
 
1.  print() : Utilizada para imprimir mensajes en la consola.
2.  len() : Devuelve la longitud de un objeto, como una lista o una cadena.
3.  input() : Permite al usuario ingresar datos desde la consola.
4.  int() ,  float() ,  str() : Utilizadas para convertir valores a enteros, flotantes o cadenas respectivamente.
5.  range() : Genera una secuencia de números.
6.  type() : Devuelve el tipo de un objeto.
7.  sum() ,  max() ,  min() : Funciones para realizar operaciones matemáticas en listas de números.
8.  abs() : Devuelve el valor absoluto de un número.
9.  round() : Redondea un número al entero más cercano.
 
Estas son solo algunas de las muchas funciones internas que Python ofrece. Puedes encontrar una lista completa de las funciones integradas en la documentación oficial de Python.
 En Python, el empaquetado y desempaquetado se refieren a la capacidad de asignar múltiples valores a una sola variable (empaquetado) y de extraer esos valores individuales de la variable para asignarlos a variables separadas (desempaquetado).
 
Empaquetado en Python:
 
El empaquetado en Python se refiere a la asignación de múltiples valores a una sola variable. Esto se puede hacer de varias formas, como en el caso de una tupla o una lista. Por ejemplo:
 
python
 Copiar
###  Empaquetado en una tupla
tupla = 1, 2, 3
### Empaquetado en una lista
lista = [4, 5, 6]
 
 
Desempaquetado en Python:
 
El desempaquetado en Python implica extraer los valores individuales de una variable empaquetada y asignarlos a variables separadas. Esto se puede hacer de la siguiente manera:
 
python
 Copiar
### Desempaquetado de una tupla
a, b, c = tupla
### Desempaquetado de una lista
x, y, z = lista
 
 
Ejemplo de Empaquetado y Desempaquetado:
 
python
 Copiar
### Empaquetado
coordenadas = (10, 20)
### Desempaquetado
x, y = coordenadas
print("Coordenada x:", x)  # Salida: Coordenada x: 10
print("Coordenada y:", y)  # Salida: Coordenada y: 20
 
 
El empaquetado y desempaquetado son técnicas útiles en Python para trabajar con múltiples valores de manera eficiente. Se utilizan principalmente con tuplas, listas y diccionarios para asignar y extraer valores de manera conveniente.

## funciones internas de python(tarea)
Las funciones internas de Python son funciones predefinidas que están disponibles para su uso en cualquier programa de Python sin necesidad de importar ningún módulo adicional. Algunas de las funciones internas más comunes en Python incluyen:
 
1.  print() : Utilizada para imprimir mensajes en la consola.
2.  len() : Devuelve la longitud de un objeto, como una lista o una cadena.
3.  input() : Permite al usuario ingresar datos desde la consola.
4.  int() ,  float() ,  str() : Utilizadas para convertir valores a enteros, flotantes o cadenas respectivamente.
5.  range() : Genera una secuencia de números.
6.  type() : Devuelve el tipo de un objeto.
7.  sum() ,  max() ,  min() : Funciones para realizar operaciones matemáticas en listas de números.
8.  abs() : Devuelve el valor absoluto de un número.
9.  round() : Redondea un número al entero más cercano.
## tipo de funciuones 
### FUNCIONES ANONIMAS ( FUNCIONES LAMBD)
 “función lambda” significa función anónima en Python. Para crear una función lambda, Python utiliza la palabra clave lambda. Una expresión lambda consiste en la palabra clave lambda seguida de una lista de argumentos, dos puntos y una única expresión (“expression”). En cuanto se llama la función lambda, se proporciona la expresión con los argumentos y se evalúa:

lambda argument: expression
Las funciones son una construcción lingüística fundamental de casi todos los lenguajes de programación y representan la unidad más pequeña de código reutilizable. Normalmente, las funciones en Python se definen con la palabra clave def. Por ejemplo, este también sería el caso de la función square que multiplica un número por sí mismo:
### FUNCIONES CALOSURE
A. Definición de "Closure"
Un closure se define como una función anónima que puede acceder a variables fuera de su ámbito de definición. En otras palabras, permite encapsular datos y lógica en un bloque independiente y reutilizable.

B. Importancia en Programación
La capacidad de utilizar closures en programación aporta flexibilidad y modularidad al código. Esto facilita la creación de funciones más dinámicas y adaptables a diferentes contextos.
¿Cómo Funcionan los Closures?
A. Encapsulamiento de Variables
Un aspecto fundamental de los closures es su capacidad para encapsular variables. Esto significa que pueden retener el estado de las variables en el momento de su creación, incluso si esas variables están fuera de su alcance original.

B. Uso de Variables Externas
Un closure puede hacer referencia y modificar variables externas a él. Este comportamiento es útil cuando se desea que una función conserve el estado de ciertas variables a lo largo de su ejecución.
### FUNCIONES CALLBACK
¿qué son las funciones callback?
JavaScript es uno de los lenguajes más populares para crear sitios web. Las posibilidades que ofrece este lenguaje de secuencias de comandos se aprovechan para diseñar páginas interactivas que sean capaces de reaccionar a las solicitudes. Para ello, se emplean variables, objetos y funciones en el marco del lenguaje. Todos ellos pueden recurrir los unos a los otros y siempre reflejan el mismo resultado en diferentes navegadores. Detrás de la mayoría de los botones o las pantallas de contenido que aparecen en un momento determinado en los sitios web, se encuentra una función callback.

Sin embargo, las funciones de este tipo no son exclusivas de JavaScript: otros lenguajes de programación conocidos, como C, Java, PHP o Python, también utilizan el callback para pasar ciertos parámetros de usuario de la forma más fácil.

¿Qué es un callback?
Las funciones siempre se referencian a determinados parámetros. Si asignas una función como parámetro a otra función, hablaremos de un callback. Las funciones callback suelen utilizarse mucho en bibliotecas y frameworks, como las aplicaciones JavaScript jQuery, Angular o node.js. Estas aplicaciones son adecuadas para crear funciones extensibles y se ejecutan únicamente después de que tenga lugar otro evento o circunstancia.

¿Cómo funciona un callback?
La función callback siempre tiene un efecto determinado que está relacionado con ciertas circunstancias. En otras palabras, solo se invoca si ha tenido lugar otra acción claramente definida. Un buen ejemplo de función callback son los controladores de eventos, que se utilizan, por ejemplo, en elementos HTML como los botones. El evento podría ser un clic del ratón que hace que se ejecute el callback, y la función en sí misma podría provocar el redireccionamiento a otra página o transmitir un valor que se haya introducido en un formulario.

La principal diferencia entre una función normal y un callback sería la siguiente: si bien una función normal se ejecuta directamente, la función callback solo se define y se llama y ejecuta únicamente cuando ocurre un evento concreto. Como hemos mencionado, las funciones callback se utilizan en numerosos lenguajes de programación y, aunque la sintaxis y la estructura de los métodos difieren, sus principios se mantienen en todos los lenguajes.
### prOgramacion funcionaL
```python
lista=[5,7,6,8,4,1]
def num_minimo(l):
minimo=l[0]
for n in l:
    if n <  mnimo:
        minimo=n
min()
```
####  averriguar sobre map(), filter(), reeduce()
