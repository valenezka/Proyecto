# import pygame
# from PodSixNet.Channel import Channel
# from PodSixNet.async import poll

# # Inicializar Pygame
# pygame.init()

# # Definir la pantalla del juego
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))

# # Definir los colores
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Definir el reloj
# clock = pygame.time.Clock()

# # Definir la clase del canal de red
# class ClientChannel(Channel):
#     def Network(self, data):
#         print('network data:', data)

# # Conectar al servidor
# address = ('localhost', 8888)
# client = ClientChannel()
# client.Connect(address=address)

# # Loop del juego
# while True:
#     # Manejar eventos
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             # Salir del juego
#             pygame.quit()
#             sys.exit()

#     # Actualizar pantalla
#     screen.fill(WHITE)
#     pygame.draw.rect(screen, BLACK, (100, 100, 50, 50))
#     pygame.display.flip()

#     # Enviar datos al servidor
#     client.Send({'action': 'move', 'x': 100, 'y': 100})

#     # Actualizar la conexión de red
#     poll()

#     # Controlar la velocidad del juego
#     clock.tick(60)
import pygame
from PodSixNet.Connection import ConnectionListener, connection
import sys

class GameClient(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))
        self.clock = pygame.time.Clock()
        self.player_pos = [0, 0]
        self.opponent_pos = [0, 0]
        self.obstacle_pos = [0, 0]
        self.score = 0

        # Inicializar pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Juego de saltar obstáculos")
        self.font = pygame.font.SysFont(None, 48)

    def Loop(self):
        # Loop principal del juego
        while True:
            # Escuchar eventos de la red
            connection.Pump()
            self.Pump()

            # Escuchar eventos del teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.Send({"action": "jump"})

            # Dibujar el juego
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), (self.player_pos[0], self.player_pos[1], 50, 50))
            pygame.draw.rect(self.screen, (255, 0, 0), (self.opponent_pos[0], self.opponent_pos[1], 50, 50))
            pygame.draw.rect(self.screen, (0, 255, 0), (self.obstacle_pos[0], self.obstacle_pos[1], 50, 50))
            score_text = self.font.render("Score: {}".format(self.score), True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))
            pygame.display.flip()

            # Esperar un poco
            self.clock.tick(5)

    # Métodos de la red
    def Network_player_pos(self, data):
        self.player_pos = data['pos']

    def Network_opponent_pos(self, data):
        self.opponent_pos = data['pos']

    def Network_obstacle_pos(self, data):
        self.obstacle_pos = data['pos']

    def Network_score_update(self, data):
        self.score = data['score']

# Inicializar y ejecutar el cliente
client = GameClient("localhost", 8888)
client.Loop()

