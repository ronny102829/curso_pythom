# #crear una funcion que reciba por argumentos n numeros y retorne una lista con numeros pares 
# def  numeros_pares(*args):
#     pares=[num for num in args if num% 2 == 0]
#     return pares
#     numeros=numeros_pares(1,2,3,4,5,6,7,8,8,9,10)
#     print(numeros)

# 2
# def num_pares(*args):
#     lista_pares=[]
#     for n in args:
#         lista_pares.apped()
#         return lista_pares
# print(num_pares(1,3,5,7,34,5,8,9,5,))

# ejerrcicio 2
## crar trew funciones para los sigientes casos 
# calcuar el numero menor 
# calcular el numero mayor
# calcular la suma de todos los numeros 
# se le pasara por argumentos n numeros 
# numeros_primos = []
# numero = 2
# while len(numeros_primos) < 20:
#     if es_primo(numero):
#         numeros_primos.append(numero)
#     numero += 1

# print(numeros_primos)
# numeros_primos = []
# num = 2

# while len(numeros_primos) < 20:
#     es_primo = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             es_primo = False
#             break
#     if es_primo:
#         numeros_primos.append(num)
#     num += 1

# print(numeros_primos)
# numeros_primos = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))][:20]
# def numero_menor(*args):
#     return min(args)

# def numero_mayor(*args):
#     return max(args)

# def suma_numeros(*args):
#     return sum(args)

# # Ejemplo de uso
# numeros = (10, 5, 20, 15, 30)
# print("Número menor:", numero_menor(*numeros))
# print("Número mayor:", numero_mayor(*numeros))
# print("Suma de todos los números:", suma_numeros(*numeros))


# travajo 27-05-2024
# Crear una lista de alumnos
estudiantes = [
    {"nombre": "jhonny", "apellido": "Pérez", "edad": 15, "celular": "1234567890", "email": "jhonnyperes@gmanil.coom"},
    {"nombre": "catalina", "apellido": "Gómez", "edad": 16, "celular": "0987654321", "email": "catalinagomes@example.com"},
    {"nombre": " rosa ", "apellido": "melano", "edad": 18, "celular": "1122334455", "email": "rosamelano@example.com"}
]
# Actualizar los registros con el campo "programa de estudios"
for alumno in estudiantes:
    alumno["programa de estudios"] = "mecatronica"

# Actualizar la edad del segundo registro a 50 años
if len(estudiantes) > 1:
    estudiantes[1]["edad"] = 50

# Imprimir la lista de alumnos actualizada
for alumno in estudiantes:
    print(alumno)