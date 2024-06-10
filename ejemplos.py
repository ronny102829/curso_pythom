# ejercicio
#pida=input("ingrese oraciones separadas por comas->")
#contador=0
#for i in range(0,len(pida)):
 #   if pida [i] == ",":
  #      contador+=1
#print(f"la cantidad de es {contador}")    
# otro ejemplo
#oracion:str=input("ingrese una oracion: ")
#contador:input=0
#for indice,letra in enumerate(oracion):
 #   if letra == ",":
  #     # print(f"su indice es {indice}")
   #     contador+=1
#print(f"la cantidad de comas es {contador}")

# edad_persona:int=int(input("ingrese su edad porfabor: "))
# for edad in range(1,edad_persona+1):
#    print(edad)
#    print("gracias por ingresar su edad")
# primera_persona:str=str(input("ingrsar su nombre: "))
# segunda_persona:str=str(input("ingrsar su nombre: "))
# tersera_persona:str=str(input("ingrsar su nombre: "))
# persona=(primera_persona,segunda_persona,tersera_persona)
# for indice,letra in enumerate(persona):
# print(indice,letra)
# ultima_letra:str=""
# for _ in range(3):
#     nombre:str=input("escribe tu nombre: ")
#     last_letter:str=nombre[-1]
# ultima_letra=+last_latter
# print(ultima_letra) 


# for i,letra in enumerate("aeiou"):
#     print(letra*(i + 1))
    # # `grs cunca`
# horarios_libres=["9:00","10:00","12:00","13:00"]
# reservas=[]

# print("horarios libres: ")
# for horarios in horarios_libres:
#     print(horarios) 

# horario_eligido=input("selecionar un horario para reservar: ")
# if horario_eligido in horarios_libres:
#     reservas.append(horario_eligido)
#     print("reserva realisado con exito para el hoario", horario_eligido)    
# else:
#     print("horario seleccionado no esta disponible")  
# costo_alquiler=25
# pago_realisado= False
# while not pago_realisado:
#     confirmacion_pago=input("¿desea realisar el pago de $" + str(costo_alquiler)+"por la reserva ?(SI/NO):")
#     if confirmacion_pago.lower() == "si" :
#      pago_realizado=True
#     print("pago realisado con exito")
# else:
#     print("el pago no se ha realisado. porfavor. realice el pago para comfirmar la reserva ")
#     if reservas:
#         print("reservas_realisadas") 
#         for reserva in reservas:
#             print("horario:", reserva,"-costo:$",costo_alquiler)
#     else:
#             print("no se a realisado ninguan reserva")
# Función para verificar si un número es primo
# def es_primo(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# # Generar una lista de los primeros 20 números primos
# numeros_primos = []
# numero = 2
# while len(numeros_primos) < 20:
#     if es_primo(numero):
#         numeros_primos.append(numero)
#     numero += 1

# print(numeros_primos]
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
numeros_primos = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))][:20]