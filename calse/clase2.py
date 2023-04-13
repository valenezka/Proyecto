# Numero= int(input("por favor ingrese el numero del cliente:"))
# if Numero==1000 :
#     print("Ganaste un premio")
# else: 
#     print("Sigue intentando")

# #Ejercicio N2
# Numero1= int(input("Por favor ingrese el primer numero: "))
# Numero2= int(input("Por favor ingrese el segundo numero: "))

# if Numero1>Numero2:
#     print(Numero2,"es menor")
# else :
#     print(Numero1,"es menor")

# #Ejercicio N3
# Numero1= float(input("Por favor ingrese el primer numero: "))
# Numero2= float(input("Por favor ingrese el segundo numero: "))

# if Numero1>Numero2:
#     print(Numero2,"es menor")
# elif Numero2>Numero1:
#     print(Numero1,"es menor")
# else :
#     print ("Los numeros son iguales")
    
# #Ejercicio N4
# x=100
# suma=0
# while True :
#     print(x)
#     suma=suma+x
#     x=x+1
#     if x>=201:
#         break
# print(suma)
    
    

# #Ejercicio N5 Ctrl+c cancela la ejecucion
# y=5
# while True:
#     print(y)
#     y=y+1
#Esto representa un ciclo infinito

#Ejercicio N6
# respuesta= input(" Desea terminar el programa? Por favor ingrese la respuesta (SI,Si,si,sí:)")
# while respuesta!= "SI" :
#     print("Desea terminar el programa?")
#     respuesta=input("Por favor ingrese la respuesta  (SI,Si,si,sí):")

# while True:
#     print(" Desea terminar el programa?")   
#     respuesta1=input("Por favor ingrese su respuesta: ")

#     if respuesta1=="SI":
#         break

#print("Hola mundo",end= "#")

# Num=int(input("Por favor ingrese el numero para mostrar su tabla: "))
# for i in range (1,10+1): ##Al limite siempre se le suma uno
#     print(f"{i}*{Num}={Num*i}")
##Ejercicio
c=0

x = ""


for i in range (100,200+1):
    c += i
    print(f"i={i} y la suma es {c}")
