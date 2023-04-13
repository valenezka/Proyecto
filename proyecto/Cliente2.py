# import socket

# clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host=socket.gethostname()

# clientsocket.connect((host,8080))

# message= "Conexion Exitosa" 
# clientsocket.send(message.encode("ascii"))

# clientsocket.close()
import socket
import sys
 
# Crear socket
socketConexion = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
# Servidor de conexión
servidor = "localhost"
# El puerto a utilizar (el servidor debe estar escuchando en este puerto)
puerto = 8080
 
msg = "Hola mundo de cliente" + "\r\n"
socketConexion.sendto(msg.encode(),(servidor,puerto))
# Recibir y mostrar el mensaje del servidor
# mensajeServidor = socketConexion.recv(1024)
# print(mensajeServidor.decode())
# Cerrar el socket
socketConexion.close()