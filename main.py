import pygame, sys
pygame.init()

width = 1700
height = 956
screen = pygame.display.set_mode((width, height))

white = (255,255,255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    screen.fill(white)
    pygame.display.flip()

pygame.quit()
