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

points = [(150,450),(300,300),(450,450)] 

def hexagon(center,shift):
    r = 150
    c = center

    points = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        x = c[0] + r * math.cos(angle_rad)
        y = c[1] + r * math.sin(angle_rad)
        if i > 3:
            x += shift
        points.append((x, y))
    pygame.draw.polygon(win, CZERWONY, points)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_1:
                    win = pygame.display.set_mode((600, 600))
                    hexagon((300,300),0)
                    hex = pygame.transform.scale_by(win, (0.6,0.6))
                    rect = hex.get_rect(center=(300, 300))
                    win.blit(hex, rect)
                    pygame.display.update()
                case pygame.K_2:
                    win = pygame.display.set_mode((600, 600))
                    hexagon((300,300),0)
                    hex = pygame.transform.rotate(win, 45)
                    rect = hex.get_rect(center=(300, 300))
                    win.blit(hex, rect)
                    pygame.display.update()
                case pygame.K_3:
                    win = pygame.display.set_mode((600, 600))
                    hexagon((300,300),0)
                    hex = pygame.transform.scale_by(win, (0.6,1))
                    hex = pygame.transform.flip(hex, False, True)
                    rect = hex.get_rect(center=(300, 300))
                    win.blit(hex, rect)
                    pygame.display.update()
                case pygame.K_4:
                    win = pygame.display.set_mode((600, 600))
                    hexagon((300,300),70)
                    rect = win.get_rect(center=(300, 300))
                    win.blit(win, rect)
                    pygame.display.update()
                case pygame.K_5:
                    win = pygame.display.set_mode((600, 600))
                    hexagon((300,300),0)
                    hex = pygame.transform.scale_by(win, (1,1/3))
                    rect = hex.get_rect(center=(300, 50))
                    pygame.draw.rect(win,(0,0,0),(0,101,600,499))
                    win.blit(hex, rect)
                    pygame.display.update()
                case pygame.K_6:
                     win = pygame.display.set_mode((600, 600))
                     hexagon((300,300),70)
                     hex = pygame.transform.rotate(win, 90)
                     rect = hex.get_rect(center=(300, 300))
                     win.blit(hex, rect)
                     pygame.display.update()
                case pygame.K_7:
                    win = pygame.display.set_mode((600, 600))
                    hexagon((300,300),0)
                    hex = pygame.transform.scale_by(win, (0.6,1))
                    hex = pygame.transform.rotate(win, 180)
                    rect = hex.get_rect(center=(300, 300))
                    win.blit(hex, rect)
                    pygame.display.flip()
                case pygame.K_8:
                    win = pygame.display.set_mode((600, 600))
                    hexagon((300,300),0)
                    hex = pygame.transform.scale_by(win, (1,1/3))
                    hex = pygame.transform.rotate(hex, 120)
                    rect = hex.get_rect(center=(200, 400))
                    pygame.draw.rect(win,(0,0,0),(250,250,250,100))
                    win.blit(hex, rect)
                    pygame.display.flip()
                case pygame.K_9:
                     win = pygame.display.set_mode((600, 600))
                     hexagon((300,300),70)
                     hex = pygame.transform.rotate(win, 180)
                     rect = hex.get_rect(center=(490, 300))
                     pygame.draw.rect(win,(0,0,0),(0,150,320,400))
                     win.blit(hex, rect)
                     pygame.display.update()

pygame.quit()


