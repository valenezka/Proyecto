# with open("calse\Archivo.txt","r") as File:
#     lista=File.readlines()

# print(f"La cantidad de lineas que tiene el archivo es {len(lista)}")

# with open("calse\Archivo2.txt","w") as ejer2:
#     for i in range (11):
#         nuevo=input("Por favor ingrese lo que desea agregar: ")
#         ejer2.write(nuevo+"\n")

# with open("calse\Archivo2.txt","r+") as ejer2:
#     lista2=ejer2.readlines()
#     for i in range(len(lista2)):
#         lista2[i]=lista2[i].strip("\n")

# print(lista2)

#Ejercicio3

# def Cantidad_caracteres(lista):
#     contador=0
#     for i in lista:
#         for n in i:
#             contador+=1

#     return contador

# with open("calse\Archivo2.txt","r") as ejer3:
#     lista2=ejer3.readlines()
#     for i in range(len(lista2)):
#        lista2[i]=lista2[i].strip("\n")
       
# print(Cantidad_caracteres(lista2))

#Ejercicio4
# while True:
#     nombre=input("Por favor ingrese su nombre: ")
    
#     with open("calse\libro_invitados.txt","a") as visitantes:
#         if nombre!="":
#             visitantes.write(f"{nombre} nos visito \n")

#     if nombre=="":
#         break 
#     print(f"Bienvenido {nombre}")

#Ejercicio5
with open("calse\primero.txt","r") as A:
    lista=A.readlines()

with open("calse\segundo.txt","a") as B:
    for i in range (len(lista)):
        if i==0:
            B.write("\n"+lista[i] )
        else:
            B.write(lista[i])

    

