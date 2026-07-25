import pygame
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
    
class Cano:

    def __init__(self):

        self.largura = 10
        self.velocidade = 5

class CanoSuperior(Cano):

    def __init__(self, altura):

        super().__init__()
        self.altura = altura

class CanoInferior(Cano):

    def __init__(self, altura):

        super().__init__()
        self.altura = altura