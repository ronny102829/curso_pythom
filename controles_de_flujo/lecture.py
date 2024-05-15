# ejersicios de clase
# #primer ejemplo if estructurado
edad:int=int(imput("escrivir tu edad: "))
#if edad>=18:
    #print("eres mayor de edad")
#else:
    #print("eres menor de edad")
 ## segundo ejemplo de if almacenado en vaRRIABLES 
 edad_dos:init=int(input("escribir tu edad: "))
respuesta:str="eres mayor de edad" if edad_dos>=18 else "eres menor de edad "
print(respuesta )
# crear un programa k imprima las 5 bocales 
vocales:str="aeiou"
for n in range(0,5):
    #print(vocales[n])
## crear un programas k me muestre los 8 primeros numeros pares
contador=0
for n in range(1,17):
    if n%2==0:
        contador+=1
        #print(f"{n} es par numero{contador}") 
## crear un programa k  pida al usuario escrivir uma oacion 
##y mostrar por terminal la cantidad de vocales "a" k tien esa oracion
## ojo: solo las"a" minuscula
oracion:str=input("escribir una oracion :")
contador:int=0
for n in range(0,lent(oracion)) 
    if oracion[n]=="a"
        cointador=contador+1
#print(f"LA CANTIDA DE LETRAS A QUE ES {contador} ")
# otra manera 
for n in "aeiou"
   # print(n)
for i,l in enumerate("aeiou"):
   # print(f"el indicees{i} y la letra es {l}")

print(f"la cantidad de las letras a que teenga es {contador}")
#ejercicio
pida=input("ingrese oraciones separadas por comas->")
contador=0
for i in range(0,len(pida)):
    if pida[i] == ",":
        contador+=1
        print(f"la cantidad de es {contador}")    
# otreo metodo
oracion:str=input("ingrese una oracion: ")
contador:input=0
for indice,letra in enumerate(oracion):
    if letra == ",":
        print(f"su indice es {indice}")
        contador+=1
print(f"la cantidad de comas es {contador}")

###cilos
son controles de flujo que repiten un codigos
### el bucle for
en el bucle for sabes donde va a terminar tu codigo
### in (para oraciones medianas )
consume menos memoria en cantidades grande de cadena y es mas rapido
### enumerate
consume mas memoria en grandes cantidades de cadena pero es rapido
### range y len (mejor para oraciones pequeñas)
consume mas memoria en cadenas grandes
#ejrcicio
edad_persona:int=int(input("ingrsar su edad: "))
for edad in range(1,edad+1):
    print(edad)
#ejercicio 15-05-2024
primera_persona:str=str(input("ingrsar su nombre: "))
segunda_persona:str=str(input("ingrsar su nombre: "))
tersera_persona:str=str(input("ingrsar su nombre: "))
print(primera_persona,segunda_persona,tersera_persona)