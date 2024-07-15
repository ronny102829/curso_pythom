# #return el valor que podre hacer uso
# #crear una funcion que retorne 10, muetre por termoinaal si es par 
# #siempre que el valor que tretorno mi funcion se utiliza en mas sen5tencias en massentyencias u operaciones. 
# def diez():
#     return 10
# if diez()%2==0:
#     print("es par")
# else:
#     print(" es inpar")
#     #print solo muestar por terminal 
# #return cuando queremos  que nuestra funciones devuelbe  o retorne in tipo de dato o un tipo nde dato estructurado
# #crear una funcion k me muestre el producto de dos numeros. 
# def producto(a,b):
#     return a*b
# print(producto(5,4))
# # crear una funcion queretorne una lista de tres numeros.
# def lista_numeros():
#     return[3,2,6]
# # crear una funcion k por pa5rametro resiva un nombre  y retorne un mensaje  de bienvenida  con el nombre.
# def mensaje(nombre):
#     print(f"hola,{nombre}, bienvinido al chongo")
# mensaje("jose")
  
#crear una FUNCION  QUE RECIVA POR parametro una lista  de numeros y me devuelva el numero menor , mostar por terminal el valor retornado  por la funcion

#-ejemplo clace 
# lista=[1,2,3,4]
# def Min(l):
#     minimo=1[0]
#     for n in l:
#         if n< minimo:
#             minimo=n
#     return minimo
# print(min(lista))
## trabajo yo
       
# def encontrar_numero_menor(lista_numeros):
#     if len(lista_numeros) == 0:
#         return None
#     else:
#         return min(lista_numeros)

# # Ejemplo de uso
# numeros = [10, 5, 8, 3, 12]
# numero_menor = encontrar_numero_menor(numeros)
# print("El número menor de la lista es:", numero_menor)


# def encontrar_numero_menor(lista_numeros):
#  if len(lista_numeros) == 0:       print("La lista está vacía. No se puede encontrar el número menor.")
#  else:
#         numero_menor = min(lista_numeros)
#         print("El número menor de la lista es:", numero_menor)
#         return numero_menor

# # Ejemplo de uso
# numeros = [10, 5, 8, 3, 12]
# numero_menor = encontrar_numero_menor(numeros)
# crear una funcion que reciba como parametro el nomnre y la edad  de una persona mi funcion debera  retornar un diccionario  con los datos,
# luego mostrar por terminal rl valor de retorno de mi funcion

# Ejemplo de uso
# nombre = "Juan"
# edad = 30
# def persona(nombre, edad):
#     datos_persona = {
#         "nombre": nombre,
#         "edad": edad
#     }
#     return datos_persona

# datos_persona =persona(nombre, edad)
# print("los datos de la persona es:", datos_persona)


# nombre =input("ingrese su nombre:")
# edad =int(imput("ingrese su edad"))
# def persona(nombre, edad):
#     # datos_persona = {
#     #     "nombre": nombre,
#     #     "edad": edad
#     #}
#     return disct(
#         nombre=nombre,
#         edad=edad
#     )

# print(persona(nombre, edad))
## eje,plos laMBDA
# saludo=lambda:"HOLA"
# print(saludo)


# numeros=[12,7,15,20,9]
# pares=list(lambda x:x %2 ==0,numeros)
# impares=list(lambda x:x %2 ==0,numeros)
# print("numeros pares:",pares)
# print("numeros impares:",impares)
#tengo una lista de alumnos que todos ellos aprobaron y paSARON AL TERCER SEMESTRE ,
# PROBLEMAS enn mi lista  todos estan en el seguno semestre  por lo que tendremos que crear  una salucion que cambie  el campo del 2 al 3 semestre 
# lista_alumnos=[
#     {
#         "nombre":"avel",
#         "edad": 36,
#         "semestre":2
#     },
#     {
#     "nombre":"anthony",
#         "edad": 40,
#         "semestre":2
#     },
#     {
#     "nombre":"edith",
#         "edad": 50,
#         "semestre":2
#     }
# ]
# def objeto (e):
#     if "semestre" in e:
#         e["semestre"]=e["semestre"]+1
# def objeto (e):
#         e["programa_etudio"]="apsti"
#     return [
#          e
#     ]
# alumnos_actualisados=list(map(objeto,lista_alumnos))
# print(alumnos_actualisados)
# ## filter 
# lista  