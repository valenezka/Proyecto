# #Ejercicio 1
# lista = []
# for i in range (35+1):
#     lista.append(i)
# print(lista)

# lista2 = []
# Numero= int(input("Por favor ingrese un numero: "))
# contador1=0
# while contador1 <= Numero:
#     lista2.append(contador1)
#     contador1+=1
# print(lista2)

# Numeroinicial=int(input("Por favor ingrese el numero inicial: "))
# Numerofinal=int(input("Por favor ingrese el numero final "))
# lista = []
# for i in range (Numeroinicial,Numerofinal):
#     i+=1
#     lista.append(i)
# print(lista)

# Ejercicio N2
# cadena=input("Por favor ingrese una cadena de caracteres: ")
# listacaracater= []
# cantidadstring=len(cadena)
# for i in range (cantidadstring):
#     if cadena[i]!=" ":
#         listacaracater.append(cadena[i])
# print(listacaracater)
""""""
# cadena = input("Ingresa una cadena de caracteres: ")
# lista_caracteres = []
# for caracter in cadena:
#     if caracter not in lista_caracteres:
#         lista_caracteres.append(caracter)

# print("La lista de caracteres sin repetir es:", lista_caracteres)
#Ejercicio N3
# import random
# lista_aleatoria= []
# for i in range (10):
#     lista_aleatoria.append(random.randint(0,10))
# print(lista_aleatoria)
# for i in range (10):
#     print(f"{lista_aleatoria[i]} su cuadrado es {lista_aleatoria[i]*lista_aleatoria[i]},su cubo es {lista_aleatoria[i]*lista_aleatoria[i]*lista_aleatoria[i]}")

#print("a" in cadena) #Aqui pregunto si la letra "a" se encuentra en la cadena de caracteres ingresados
#Tambien puede ser una lista, los strings son considerados listas tambien 

# #Ejercicio N4
# tupla=(1,2,3,3,5,6,7,8,3,10)
# Numero=int(input("Por favor ingrese el valor que desea buscar: "))
# contador=0
# for i in range (10):
#     if tupla[i]==Numero:
#         contador+=1

# print(contador)

# #Ejercicio N5
# tupla=(1,2,3,4,5,6,7,8,9,10,7,6,5,4,8,4,3,2,4)
# indice=int(input("Por favor ingrese el idice: "))

numero=int(input("Por favor ingrese un numero: "))
lista_numeros=[]
posicion=None
while numero!=0:
    lista_numeros.append(numero)
    numero=int(input("Por favor ingrese un numero o 0 para terminar: "))
print(lista_numeros)
#vamos a ordenar los numeros
lista_ordenada=[]
menor=0
while len(lista_numeros)!=0:
    
    for i in range (len(lista_numeros)):
        if lista_numeros[i] < menor:
            menor=lista_numeros[i]
            posicion=i 
    if menor not in lista_ordenada:
        lista_ordenada.append(menor)
    lista_numeros.remove(menor)

print(lista_ordenada)

diccionario={"Nombre":"Sebas",}

