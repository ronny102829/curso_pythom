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
### map 
Esta función trabaja de una forma muy similar a filter(), con la diferencia que en lugar de aplicar una condición a un elemento de una lista o secuencia, aplica una función sobre todos los elementos y como resultado se devuelve un iterable de tipo map:
```python

def doblar(numero):
    return numero*2

numeros = [2, 5, 10, 23, 50, 33]

map(doblar, numeros)

<map at 0x212eb6e0748>
```
Fácilmente podemos transformar este iterable en una lista:

```python
list(map(doblar, numeros))

[4, 10, 20, 46, 100, 66]
```
Y podemos simplificarlo con una función lambda para substituir la llamada de una función definida:

```python
list( map(lambda x: x*2, numeros) )

[4, 10, 20, 46, 100, 66]

La función map() se utiliza mucho junto a expresiones lambda ya que permite ahorrarnos el esfuerzo de crear bucles for.

Además se puede utilizar sobre más de un iterable con la condición que tengan la misma longitud.

Por ejemplo si queremos multiplicar los números de dos listas:

```pyton

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

list( map(lambda x,y : x*y, a,b) )

[7, 9, 11, 13, 15]
```
E incluso podemos extender la funcionalidad a tres listas o más:

```python
c = [11, 12, 13, 14, 15]

list( map(lambda x,y,z : x*y*z, a,b,c) )

[66, 168, 312, 504, 750]
```
### Función filter()
Tal como su nombre indica filter significa filtrar, y es una de mis funciones favoritas, ya que a partir de una lista o iterador y una función condicional, es capaz de devolver una nueva colección con los elementos filtrados que cumplan la condición.

Por ejemplo, supongamos que tenemos una lista varios números y queremos filtrarla, quedándonos únicamente con los múltiples de 5...
```python

def multiple(numero):    # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True      # Sólo devolvemos True si lo es

numeros = [2, 5, 10, 23, 50, 33]

filter(multiple, numeros)

<filter at 0x257ac84abe0>
```
Si ejecutamos el filtro obtenemos un objeto de tipo filtro, pero podemos transformarlo en una lista fácilmente haciendo un cast (conversión):
```python

list( filter(multiple, numeros) )

[5, 10, 50]
Por tanto cuando utilizamos la función filter() tenemos que enviar una función condicional, pero como recordaréis, no es necesario definirla, podemos utlizar una función anónima lambda:


list( filter(lambda numero: numero%5 == 0, numeros) )

[5, 10, 50]
```
Así, en una sola línea hemos definido y ejecutado el filtro utilizando una función condicional anónima y una lista de numeros.

Filtrando objetos
Sin embargo, más allá de filtrar listas con valores simples, el verdadero potencial de filter() sale a relucir cuando necesitamos filtrar varios objetos de una lista.

Por ejemplo, dada una lista con varias personas, nos gustaría filtrar únicamente las que son menores de edad:
```python

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)


personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manuel", 78),
    Persona("Eduardo", 12)
]
```
Para hacerlo nos vamos a servir de una función lambda, comprobando el campo edad para cada persona:

```python
menores = filter(lambda persona: persona.edad < 18, personas)

for menor in menores:
    print(menor)
```
Marta de 16 años
Eduardo de 12 años
Sé que es un ejemplo sencillo, pero estoy seguro que os puede servir como base para realizar filtrados en muchos de vuestros proyectos.

### La función reduce()
reduce() es una función incorporada de Python 2, que toma como argumento un conjunto de valores (una lista, una tupla, o cualquier objeto iterable) y lo "reduce" a un único valor. Cómo se obtiene ese único valor a partir de la colección pasada como argumento dependerá de la función aplicada.

Por ejemplo, el siguiente código reduce la lista [1, 2, 3, 4] al número 10 aplicando la función add(a, b), que retorna la suma de sus argumentos.
```python
def add(a, b):
    return a + b

print(reduce(add, [1, 2, 3, 4]))  # 10
```

La función pasada como primer argumento debe tener dos parámetros. reduce() se encargará de llamarla de forma acumulativa (es decir, preservando el resultado de llamadas anteriores) de izquierda a derecha. De modo que el código anterior es similar a:
```python
print(add(add(add(1, 2), 3), 4))

Es decir, la operación realizada es ((1 + 2) + 3) + 4, de la que resulta 10.
```

A partir de Python 3 la función fue movida al módulo estándar functools.

```python
from functools import reduce
```