import pygame
import sys
from elements import Bird

pygame.init()

largura_tela = 600
altura_tela = 860
tela = pygame.display.set_mode((largura_tela, altura_tela))

bird = Bird(370)



clock = pygame.time.Clock() 

running = True

while running:

    clock.tick(60)

    tela.fill((46, 111, 64))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                bird.jump()

    bird.update()

    pygame.draw.rect(tela, (255, 0, 0), (200, bird.pos_y, 40, 60))
    pygame.draw.rect(tela, (136, 231, 136), (0, 760, 600, 100))

    pygame.display.update()

pygame.quit()
sys.exit()