import pygame
size = (800, 600)
screen = pygame.display.set_mode(size)
menu_image=pygame.image.load('imagenes\menu.jpg').convert()
menu_image=pygame.transform.scale(menu_image,(800,600))
        
# Configuración del reloj
clock = pygame.time.Clock()

def generar_otra_pantalla():
    otra_pantalla = True
    while otra_pantalla:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                #IMPORTANTE ESTA ACCION, DE MODO QUE SI PULSAN DE NUEVO LA TECLA SE OCULTE EL MENU
                    otra_pantalla = False
                    return True
                elif event.key==pygame.K_h:
                    otra_pantalla=True
                    return False
                
        screen.fill((0, 0, 0))
        # DIBUJAMOS COSAS
        screen.blit(menu_image, (0, 0))
        # UNICAMENTE ACTUALIZAR LA PORCION DE PANTALLA QUE ESTAMOS USANDO, NOTODO.
        # PORQUE DE LO CONTRARIO BORRARIA LO QUE ESTABA DEBAJO, 
        # DIGAMOS ERA UN MENU DE PAUSA, SI USAMOS FLIP CUANDO QUITEMOS EL MENU NO QUEDARA NADA
        pygame.display.update()

        # Y LUEGO PONEMOS EL RELOJ RAPIDO PARA QUE SEA UN RENDERIZADO PERMANENTE
        clock.tick(5)

