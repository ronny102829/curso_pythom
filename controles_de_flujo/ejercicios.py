##escrivir un programa k pida al usuario su edad y k muewtre por plantilla si es mayor de edad 
#ejecucion d el programa#ingresar datos
edad = int(input("ingresar su edad porfabor: "))
if edad >= 18:
#EJECUCION DE PROGRAMA
    print("eres Mayor de edad.")
else:
    print("eres menor de edad.")
##VISTA DEL RESULTADO   


#ejercicio 2
##INGRESAR DATOS 
guardar_contraseña="ronny2028" 
ingresar_contraseña= input("ingrese la contraseña: ")
if guardar_contraseña.upper() ==ingresar_contraseña.upper():
## EJECUCUION DE PROGRAMAS 
    print("la contraseña es correcta.")
else:
    print("la contraseña es incorecta.") 
##VISTA DEL RESULTADO 


#ejercico 3 
##INGRESAR DATOS 
numero=int(input("ingresar un numero entero positivo: "))
##EJUCUCION DE PROGRAMAS 
if numero > 0:
    print(*range(numero, -1,-1), sep=",")
else:
    print("el numero ingresado no es valido")
##VISTA DEL RESULTAFO
# ejercicioo 20-05-2024
nota=int(input(f"ingrese al nota :"))