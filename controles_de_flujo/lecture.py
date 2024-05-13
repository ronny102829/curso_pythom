#ejersicios de clase
# #primer ejemplo if estructurado
edad:int=int(imput("escrivir tu edad: "))
if edad>=18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")
 ## segundo ejemplo de if almacenado en vaRRIABLES 
 edad_dos:int0int(input("escrivir tu edad: "))
respuesta:str="eres mayor de edad" if edad_dos>=18 else "eres menor de edad "
print(respuesta )
# crear un programa k imprima las 5 bocales 
vocales:str="aeiou"
for n in range(0,5):
    print(vocales[n])
## crear un programas k me muestre los 8 primeros numeros pares
contador=0
for n in range(1,17):
    if n%2==0:
        contador+=1
        print(f"{n} es par numero{contador}") 
## crear un programa k  pida al usuario escrivir uma oacion 
##y mostrar por terminal la cantidad de vocales "a" k tien esa oracion
## ojo: solo las"a" minuscula
oracion:str=input("escribir una oracion :")
contador:int=0
for n in range(0,lent(oracion)) 
    if oracion[n]=="a"
        cointador=contador+1
print(f"LA CANTIDA DE LETRAS A QUE ES {contador} ")
# otra manera 
for n in "aeiou"
    print(n)
for i,l in enumerate("aeiou"):
    print(f"el indicees{i} y la letra es {l}")

print(f"la cantidad de las letras a que teenga es {contador}")
#ejercicio
pida=input("ingrese oraciones separadas por comas->")
contador=0
for i in range(0,len(oracion)):
    if oracion[i] == ",":
        contador+=1
        print(f"la cantidad de es {contador}")    
