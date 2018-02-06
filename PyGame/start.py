import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    # Drawing
    pygame.draw.rect(screen,(0,150,255), pygame.Rect(10,50,200,100))
    pygame.display.flip()