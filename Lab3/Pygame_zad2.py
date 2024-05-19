from pickle import FALSE
from tkinter import TRUE
from turtle import Screen
import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        win.fill((255,255,255))
        pygame.draw.rect(win,ZIELONY,(150,150,300,300))
        pygame.draw.polygon(win,(255,255,255),((150,450),(300,300),(450,450)))
    pygame.display.update()


pygame.quit()



