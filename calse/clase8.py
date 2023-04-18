# try: 
#     "a"/"b"
# except Exception as e:
#     print(e)

# Crear una funcion que dado un String devuelva si se lo puede convertir a int
# def ConvertirString(Dato):
    # num=("0","1","2","3","4","5","6","7","8","9",".")
    # for i in Dato: 
    #     if i not in num:
    #         return False
    #     else:
    #         return True
#     try:
#         numero=int(Dato)
#         return True
#     except Exception as error: 
#         return False
    
# dato=input("Por favor ingrese un string: ")
# if ConvertirString(dato)==False:
#     print("No se puede convertir el string")
# else:
#     print("Si se puede convertir a int")


#Crear una funcion que pida un archivo al usuario, lo abra y muestre su contenido (solo r) en caso de no existir 
#El archivo mostrar el error y pedir otro archivo

def verif_archivo():
    while True:
        archivo=input("Por favor ingrese la ruta del archivo: ")
        try:
            with open (archivo,"r") as file:
                lista_Archivo=file.readlines()
                print(lista_Archivo)
                break
        except FileNotFoundError:
            print("No se encontro el archivo")
        except Exception as error:
            print(error)


verif_archivo()









