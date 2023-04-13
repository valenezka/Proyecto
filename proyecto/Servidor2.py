# import socket

# serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# host= socket.gethostname()

# serversocket.bind((host,8080))

# serversocket.listen(1)

# while True:
#     clientsocket,addr=serversocket.accept()

#     print("Got a connection from %s" % str(addr))
#     message= clientsocket.recv(1024)
#     print(message.decode("ascii"))
#     clientsocket.close()
import socket
import sys
# Crear socket
socketAbierto = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Nombre del equipo (o IP), en blanco para localhost
# para recibir conexiones externas
equipo = "localhost"
# Puerto de escucha del servidor
puerto = 8080
socketAbierto.bind((equipo, puerto))

print("Escuchando en el puerto: ", puerto)
while True:
    # A la espera de una conexión de un cliente
    connection,address = socketAbierto.recvfrom(1024)
    print("Cliente ", address[0],address[1], " conectado")
    print(connection.decode())
    # Enviar un mensaje al cliente conectado
    # mensaje = "Mensaje enviado al cliente desde el servidor"
    # connection.send(mensaje.encode())
    # Cerrar el socket


socketAbierto.close()