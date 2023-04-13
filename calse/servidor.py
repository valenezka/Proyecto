# import socket
# import threading

# def handle_client(client_socket):
#     # Recibe datos del cliente
#     request = client_socket.recv(1024)
#     print(f"Received: {request.decode('utf-8')}")

#     # Envía una respuesta al cliente
#     response = "Hello from server!"
#     client_socket.send(response.encode('utf-8'))

#     # Cierra el socket del cliente
#     client_socket.close()

# def start_server():
#     # Crea un socket TCP/IP
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     # Asocia el socket a una dirección y un puerto
#     server_address = ('localhost', 8080)
#     server_socket.bind(server_address)

#     # Comienza a escuchar en el puerto
#     server_socket.listen(5)
#     print(f"Server listening on port {server_address[1]}...")

#     while True:
#         # Espera a que llegue una conexión
#         client_socket, client_address = server_socket.accept()
#         print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

#         # Crea un hilo para manejar la conexión del cliente
#         client_thread = threading.Thread(target=handle_client, args=(client_socket,)
#         client_thread.start()

# if __name__ == '__main__':
#     start_server(

from PodSixNet.Server import Server
from PodSixNet.Channel import Channel
import random

# Definir la clase del canal de red
class ClientChannel(Channel):
    def Red(self, datos):
        print('Datos de la red:', datos)
        
    def Red_Movimientos(self, datos):
        print('Movimiento:', datos)
        # Agregar código para manejar la acción del jugador, como mover el personaje

# Definir la clase del servidor
class MyServer(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = []
        self.obstaculo_pos = 0
        self.puntuacion = 0
        
        # Configurar la posición inicial del obstáculo
        self.obstaculo_pos = random.randint(0, 700)

    def Connected(self, channel, addr):
        self.players.append(channel)
        print('new connection:', channel)

    def enviar_puntuacion_actualizada(self):
        # Enviar puntuación actualizada a todos los jugadores
        for player in self.players:
            player.Send({'action': 'puntuacion_actualizada', 'puntuacion': self.puntuacion})

    def actualizacion(self):
        # Mover obstáculo hacia abajo
        self.obstaculo_pos += 5
        if self.obstaculo_pos > 600:
            # Configurar la posición de un nuevo obstáculo
            self.obstaculo_pos = random.randint(0, 700)

            # Incrementar la puntuación del jugador
            self.puntuacion += 1
            self.enviar_puntuacion_actualizada()

    def Lanzar(self):
        while True:
            self.Pump()
            self.actualizacion()

# Inicializar y lanzar el servidor
my_server = MyServer()
my_server.Lanzar()
