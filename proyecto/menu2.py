import pygame,sys
import Button

pygame.init()
SCREEN=pygame.display.set_mode((800,600))
pygame.display.set_caption("Menu")
fondo=pygame.image.load(r"imagenes\fondo_meu.jpg")
def main_menu():
    SCREEN.blit(fondo,(0,0))
    menu_mouse_pos=pygame.mouse.get_pos()
    menu_text=get_font(100).render("Mi Menu",True,"#b68f40")
    menu_rect=menu_text.get_rect(center=(640,100))

    play_button=Button(image=pygame.image.load(r"imagenes\play.jpg")), pos=(640,250)
