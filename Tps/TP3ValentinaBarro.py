#Ejercicio1
lista= []
for i in range (20+1):
    lista.append(i)
print(lista)

lista2=[]
numero_ini=int(input("Por favor ingrese el numero por donde quiere iniciar: "))
numero_fin=int(input("Por favor ingrese el numero por donde quiere finalizar: "))

for i in range (numero_ini,numero_fin+1):
    lista2.append(i)
print(lista2)

# #Ejercicio2
# lista=[]
# numero=int(input("Por favor ingrese un numero: "))
# for i in range (10+1):
#     lista.append(i*numero)
# print(lista)

#Ejercicio3

# caracteres=input("Por favor ingrese una cadena de caracteres: ")
# lista_caracteres=[]

# for i in range(len(caracteres)):
#     contador1=0
#     for n in range (i+1,len(caracteres)):
#          if caracteres[i]==caracteres[n]:
#             contador1+=1
    
#     if contador1==0:
#         lista_caracteres.append(caracteres[i])
   
# print(lista_caracteres)

#Ejercicio 4
# cadena=input("Por favor ingrese una cadena de string: ")
# sin_espacios=[]
# for i in range (len(cadena)):
#     if cadena[i]!=" ":
#         sin_espacios.append(cadena[i])

# print(sin_espacios)

#Ejercicio 5
# Crea una tupla con números, pide un numero por teclado e indica cuantas veces se
# repite.
# tupla=(1,2,3,4,1,5,2,5,3,7,3,6)
# numero=int(input("Por favor ingrese el numero que desea buscar: "))
# contador=0
# for i in range (len(tupla)):
#     if tupla[i]==numero:
#         contador+=1
# print(contador)

#Ejercicio 6
# tupla=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
# numero=int(input("Por favor ingrese un numero para la tupla: "))
# while numero!=0:
#     if 1<=numero<=len(tupla):
#         print(f"el mes asociado a {numero} es {tupla[numero-1]} ")
#     else :
#         print("No se encontro ningun mes asociado al numero")
#     numero=int(input("Por favor ingrese un numero para la tupla o 0 para terminar: "))

#Ejercicio7
# ) Crea una tupla con números e indica el número con mayor valor y el que menor
# tenga.
# tupla=(1,2,3,5,8,25,88,4,-5)
# mayor=0
# menor=0
# for i in tupla:
#     if i < menor :
#         menor=i
#     elif i> mayor:
#         mayor=i

# print(f"el numero mayor de la tupla es {mayor} y el menor es {menor}")

#Ejercicio 8
# dicc_telefonos={"valentina":"3875754602"}
# nombres=input("Por favor ingrese un nombre: ")
# while nombres!="*":
#     if nombres in dicc_telefonos:
#         print(dicc_telefonos[nombres])
#         respuesta=input("desea cambiar el numero de telefono?: ")
#         if respuesta.lower()=="si":
#             dicc_telefonos[nombres]=input("Ingrese el numero nuevo de telefono: ")
#     else :
#         dicc_telefonos[nombres]=input(f"Agregue el numero de telefono para {nombres}: ")

#     nombres=input("Por favor ingrese un nombre, * para terminar : ")

# print(dicc_telefonos)

#Ejercicio 9
# Opcional: Pide números y mételos en una lista, cuando el usuario meta un 0 ya
# dejaremos de insertar. Por último, muestra los números ordenados de menor a
# mayor.
# numero=int(input("Por favor ingrese un numero: "))
# lista_numeros=[]

# while numero!=0:
#     lista_numeros.append(numero)
#     numero=int(input("Por favor ingrese un numero o 0 para terminar: "))
# print(lista_numeros)
# #vamos a ordenar los numeros
# lista_ordenada=[]
# posicion=None
# while len(lista_numeros)!=0:
#     menor=lista_numeros[0]
#     for i in range (len(lista_numeros)):
#         if lista_numeros[i] <= menor:
#             menor=lista_numeros[i]
#             posicion=i 
#     if menor not in lista_ordenada:
#         lista_ordenada.append(menor)
#     lista_numeros.remove(menor)

# print(lista_ordenada)
    
#Ejercicio 10
# numero=int(input("Por favor ingrese un numero: "))
#posicion=None
# lista_numeros=[]
# while numero!=0:
#     lista_numeros.append(numero)
#     numero=int(input("Por favor ingrese un numero o 0 para terminar: "))
# print(lista_numeros)
# #vamos a ordenar los numeros
# lista_ordenada=[]
# while len(lista_numeros)!=0:
#     mayor=lista_numeros[0]
#     for i in range (len(lista_numeros)):
#         if lista_numeros[i] >= mayor:
#             mayor=lista_numeros[i]
#             posicion=i 
#     if mayor not in lista_ordenada:
#         lista_ordenada.append(mayor)
#     lista_numeros.remove(mayor)

# print(lista_ordenada)

#Ejercicio 11
# codigo_morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
#     "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
#     "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
#     "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
#     "x": "-..-", "y": "-.--", "z": "--.."," ":" / "}

# mensaje=input("Por favor ingrese el mensaje que desea traducir a morse: ")
# lista_morse=""
# for i in range (len(mensaje)):
#     lista_morse= str(lista_morse) + str(codigo_morse[mensaje[i]])


# print(lista_morse)
