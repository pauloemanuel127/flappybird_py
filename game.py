import pygame
import sys
from elements import Passaro, Chao, Canos

class Jogo:

    def __init__(self):

        pygame.init()
        self.tela = pygame.display.set_mode((600,860))
        pygame.display.set_caption("Flappy_Bird with POO")
        self.clock = pygame.time.Clock()

        self.fonte = pygame.font.SysFont("Arial", 30, True, True)
        self.texto_inicio = self.fonte.render("Aperte Espaço para jogar", False, (255, 255, 255))
        self.texto_gameover = self.fonte.render("GAME OVER!", False, (255, 255, 255))

        self.passaro = Passaro()
        self.chao = Chao()
        self.canos = []
        self.estado = "inicio"

    def eventos(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    if self.estado == "inicio" or self.estado == "game_over":
                        self.estado = "jogando"
                        self.passaro = Passaro()
                        self.canos = [Canos(600)]

                    elif self.estado == "jogando":
                        self.passaro.jump()

    def atualizar(self):

        if self.estado == "jogando":
            self.passaro.update()

            if self.canos[-1].pos_x < 275:
                self.canos.append(Canos(600))

            for cano in self.canos:

                cano.update()

            if self.canos[0].pos_x < -50:
                self.canos.pop(0)

            rect_passaro = pygame.Rect(self.passaro.pos_x, self.passaro.pos_y, 40, 40)
            rect_chao = pygame.Rect(self.chao.pos_x, self.chao.pos_y, 600, 100)

            if rect_passaro.colliderect(rect_chao):
                self.estado = "game_over"


            for cano in self.canos:

                rect_cano_sup = pygame.Rect(cano.pos_x, 0, cano.largura, cano.altura_topo)
                rect_cano_base = pygame.Rect(cano.pos_x, cano.pos_y_inferior, cano.largura, cano.altura_base)

                if rect_passaro.colliderect(rect_cano_sup) or rect_passaro.colliderect(rect_cano_base):
                    self.estado = "game_over"


    def desenhar(self):

        self.tela.fill((173, 216, 230))

        self.passaro.draw(self.tela)
        self.chao.draw(self.tela)

        for cano in self.canos:

            cano.draw(self.tela)

        if self.estado == "inicio":
            self.tela.blit(self.texto_inicio, (125, 240))

        elif self.estado == "game_over":
            self.tela.blit(self.texto_gameover, (210, 240))

        pygame.display.update()

    def run(self):

        while True:
            self.clock.tick(60)
            self.eventos()
            self.atualizar()
            self.desenhar()

jogo = Jogo()
jogo.run()