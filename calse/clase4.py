# cadena=input("Por favor ingrese una palabra: ")
# lista_cadena=[]
# for i in cadena: 
#     lista_cadena.append(i)

# print(lista_cadena)

# Realizar un programa que inicialice una lista con 10 números ingresados por el
# usuario y luego muestre en pantalla cual elemento es el menor
# lista=[]
# final=int(input("Por favor ingrese cuantos numeros desea en la lista: "))
# for i in range (final):
#     numero=int(input("Por favor ingrese un numero:"))
#     lista.append(numero)

# print(lista)
# menor=lista[0]
# for i in lista:
#     if i < menor:
#         menor=i

# print(menor)

# Crea una tupla que contenga todos los meses de un año. Luego pedir al usuario
# un numero y mostrar que mes representa
# tupla=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
# numero=int(input("Por favor ingrese el numero que desea buscar en la tupla: "))
# print(f"El mes asociado a {numero} es {tupla[numero-1]}")



# materias=("Matematica","Fisica","Quimica","Historia","Lengua")
# for i in range(len(materias)):
#     nota=input(f"Que nota sacaste en: {materias[i]}: ")
#     print(f"en {materias[i]} sacaste {nota}")

# Crea un programa que pida un número al usuario el nombre de un mes (Enero,
# Febrero, etc.) y diga cuántos días tiene (por ejemplo, 30. Para simplificarlo
# vamos a suponer que febrero tiene 28 días. Usar diccionarios
# dicc_meses={"Enero":31,"Febrero":28,"Marzo":31,"Abril":30,"Mayo":31,"Junio":30,"Julio":31,"Agosto":31,"Septiembre":30,"Octubre":31,"Noviembre":30,"Diciembre":31}
# mes=input("Por favor ingrese el mes del que desea saber: ")
# while True:
#     if mes=="0":
#         break
#     else:
#         print(f"El mes {mes} tiene {dicc_meses[mes]} dias")
#         mes=input("Por favor ingrese el mes del que desea saber,0 para terminar: ")

# Cree un programa que calcule el factorial de un numero,luego muestre 3 mensajes, calcule el factorial de otro numero
# calcule el factorial de otro numero sume los numeros del 1 al 100 calcule el factorial de otro numero
def quick_sort(lista, start, end):
    if start < end:
        pivot = lista[start]
        valor_izquierdo = start + 1
        valor_derecho = end
        while valor_izquierdo <= valor_derecho:
            while valor_izquierdo <= valor_derecho and lista[valor_izquierdo] <= pivot:
                valor_izquierdo += 1
            while valor_izquierdo <= valor_derecho and lista[valor_derecho] >= pivot:
                valor_derecho -= 1
            if valor_izquierdo <= valor_derecho:
                lista[valor_izquierdo], lista[valor_derecho] = lista[valor_derecho], lista[valor_izquierdo]
        lista[start], lista[valor_derecho] = lista[valor_derecho], lista[start]
        quick_sort(lista, start, valor_derecho - 1)
        quick_sort(lista, valor_derecho + 1, end)


quick_sort(lista, 0, len(lista) - 1)
print(lista)
