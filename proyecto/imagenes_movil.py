import itertools
import pygame
import os
class AnimatedBackground(pygame.sprite.Sprite):
    def __init__(self, position, images, delay):
        super(AnimatedBackground, self).__init__()

        self.images = itertools.cycle(images)
        self.image = next(self.images)
        self.rect = pygame.Rect(position,  self.image.get_rect().size)

        self.animation_time = delay
        self.current_time = 0

def Animar():
    
    pygame.init()

    # Configuración de la ventana
    size = (800, 335)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ultima Carrera del Rayo")
    #Fondo de pantalla

    imagen = None
    dir = sorted(os.listdir("choque"))
    #images =  [pygame.image.load("choque" + os.sep + file_name).convert() for file_name in sorted(os.listdir("choque"))]
    # Configuración de la variable de juego que indica si se está ejecutando o no
    running = True
    # Loop principal del juegoç
    i=0
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False   
        if i != 18:
            fondo_image = pygame.image.load(f"choque/{dir[i]}")
        screen.fill((255, 255, 255))
 
        screen.blit(fondo_image,(0,0))
        pygame.display.flip()
        if (i == dir.__len__()-1):
            break
        i+=1
