# Crear una clase gato que contenga 5 atributos (Nombre, Color de pelo, color de
# ojos, cansancio, energia y hambre) y 4 métodos (Comer, Dormir, Jugar, Acariciar). Luego
# instanciar 3 objetos de la clase gato con distintos atributos y utilizar sus
# Metodos.
class Gato: 
    nombre=""
    color_pelo=""
    color_ojos=""
    energia=0
    hambre=0

    def __init__(self,Nombre,Color_pelo,Color_ojos,Energia,Hambre):#Constructor
        self.nombre=Nombre
        self.color_pelo=Color_pelo
        self.color_ojos=Color_ojos
        self.energia=Energia
        self.hambre=Hambre

    def Comer(self):
        self.hambre-=1


    def Dormir(self):
        self.energia+=1
        print(f"{self.nombre} esta durmiendo")

    def Jugar(self):
        self.energia-=1
        self.hambre+=1

    def Acariciar(self):
        print(f"{self.nombre} se siente querido")
        self.energia+=1


name=input("Por favor ingrese el nombre del gato: ")
color=input("Por favor ingrese el color del gato: ")
eyes=input("Por favor ingrese el color de ojos del gato: ")
energy=int(input("Por favor ingrese la energia del gato"))
hunger=int(input("Por favor ingrese su nivel de hambre: "))


gato1=Gato(name,color ,eyes ,energy,hunger)
gato1.Acariciar()
print(f"Energia= {gato1.energia}")


