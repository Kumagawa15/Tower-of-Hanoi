from typing import Text
import pygame

screen = pygame.display.set_mode((840, 480))
clock = pygame.time.Clock()
ticks = pygame.time.get_ticks()

# colors:
BG_COLOR = (240, 240, 217)      #WHITE
TOWER_COLOR = (129, 108, 91)    #BROWN
POINTER_COLOR = (255, 0, 0)     #RED
POLE_COLOR = (163, 173, 184)    #GREY

#text color:
TEXT_COLORG = (21, 171, 0)     #GREEN
TEXT_COLORB = (0, 0, 0)         #BLACK
TEXT_COLORR = (255, 0, 0)       #RED
TEXT_COLORY = (239, 229, 51)    #YELLOW
TEXT_COLORBL = (78,162,196)     #BLUE
TEXT_COLORW = (255, 255, 255)   #WHITE
#method atau fungsi pembuatan text 
def make_text(screen, text, midtop, aa=True, font=None, font_name = None, size = None, color=(255,0,0)):
    if font is None:                                    # font option is provided to save memory if font is
        font = pygame.font.SysFont(font_name, size)     # already loaded and needs to be reused many times
    font_surface = font.render(text, aa, color)
    font_rect = font_surface.get_rect()
    font_rect.midtop = midtop
    screen.blit(font_surface, font_rect)
