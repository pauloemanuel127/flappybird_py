import pygame
from random import randint
class Passaro:

    def __init__(self):

        self.pos_x = 200
        self.pos_y = 370
        self.cor = (255, 255, 0)
        self.velocidade = 0
        self.gravidade = 0.1

    def jump(self):

        self.velocidade = -6

    def update(self):

        self.velocidade += self.gravidade
        self.pos_y += self.velocidade

    def draw(self, tela):

        pygame.draw.rect(tela, self.cor, (self.pos_x, self.pos_y, 40, 40))
class Chao:

    def __init__(self):

        self.pos_x = 0
        self. pos_y = 760
        self.cor = (136, 231, 136)

    def draw(self, tela):
    
            pygame.draw.rect(tela, self.cor, (self.pos_x, self.pos_y, 600, 100))
    
class Canos:

    def __init__(self, x):

        self.pos_x = x
        self.largura = 40
        self.cor = (34, 139, 34)
        self.velocidade = 4
        
        self.espaço = 150


        self.altura_topo = randint(50, 560)

        self.pos_y_inferior = self.altura_topo + self.espaço

        self.altura_base = 760 - self.pos_y_inferior

    def update(self):

        self.pos_x -= self.velocidade

    def draw(self, tela):

        pygame.draw.rect(tela, self.cor, (self.pos_x, 0, self.largura, self.altura_topo))

        pygame.draw.rect(tela, self.cor, (self.pos_x, self.pos_y_inferior, self.largura, self.altura_base))