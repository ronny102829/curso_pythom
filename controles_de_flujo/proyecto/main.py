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


# Lista de horarios libres
horarios_libres = ["08:00", "09:00", "10:00", "11:00", "12:00"]

# Mostrar la lista de horarios libres
print("Horarios libres:")
for horario in horarios_libres:
    print(horario)

# Reservar un horario
horario_elegido = input("Ingrese el horario que desea reservar: ")
if horario_elegido in horarios_libres:
    print("¡Horario reservado con éxito!")
else:
    print("El horario seleccionado no está disponible.")

# Pagar por el alquiler de la reserva
costo_alquiler = 10 # Costo ficticio del alquiler
confirmacion_pago = input("¿Desea proceder con el pago de $10? (Sí/No): ")
if confirmacion_pago.lower() == "sí":
    print("Pago realizado correctamente.")
else:
    print("Pago cancelado.")

# Verificar detalles del alquiler
if confirmacion_pago.lower() == "sí":
    print("Detalles de la reserva:")
    print("Fecha: 2024-05-23") # Fecha ficticia
    print("Hora: " + horario_elegido)
    print("Costo: $" + str(costo_alquiler))
else:
    print("No se ha realizado el pago, no hay detalles de reserva.")