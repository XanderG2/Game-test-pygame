import pygame, sys
pygame.init()

width = 1700
height = 956
screen = pygame.display.set_mode((width, height))

white = (255,255,255)
black = (0,0,0)

ph = 100
pw = 50
player = pygame.Rect(round(width/2-pw/2), round(height/2-ph/2), pw, ph)

fps = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    screen.fill(white)
    pygame.draw.rect(screen, black, player)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
