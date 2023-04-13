# def numeros_primos(limite):
    
#     for i in range (1,limite+1):
#         contador=0
#         for j in range (1,i+1):
#             if i%j==0: 
#                 contador+=1
#         if contador==2:
#             print(f"El numero {i} es primo")

# limite=int(input("Por favor ingrese hasta donde quiere ver los numeros primos"))
# numeros_primos(limite)

# . Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si
# la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se
# considerará válida si contiene el símbolo "@".
# def correo(mail):
#     if mail.find("@") ==-1: 
#         print("El mail no es valido")
#     else:
#         print("El mail es correcto")


# mail=input("Por favor ingrese su direccion de correo:")
# correo(mail)

# ▪ 3. Definir una función que muestre el factorial de un número
# def factorial(numero):
#     contador=1
#     for i in range (1,numero+1):
#         contador=contador*i
#     return print(contador)

# numero=int(input("Por favor ingrese el numero del que quiera ver su factorial: "))
# factorial(numero)

# 4. Escriba una función que le pida al usuario ingresar condimentos para un sándwich,
# hasta que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un
# mensaje avisando que ya se agregó el condimento al sándwich.

def condimentos():
    con=input("Por favor ingrese el condimento para el sadnwich: ")
    while con != "salir": 
        print(f"Se agrego el condimento {con}")
        con=input("Por favor ingrese el condimento para el sadnwich, escriba salir para terminar: ")

condimentos()