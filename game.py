import pygame
import sys
from elements import Passaro, Chao

class Game:

    def __init__(self):

        pygame.init()
        self.tela = pygame.display.set_mode((600,860))
        pygame.display.set_caption("Flappy_Bird with POO")
        self.clock = pygame.time.Clock()

        self.fonte = pygame.font.SysFont("Arial", 30, True, True)
        self.texto_inicio = self.fonte.render("Aperte barra de espaço para jogar", False, (255, 255, 255))
        self.texto_gameover = self.fonte.render("GAME OVER! \n" \
        "Aperte barra de espaço para tentar novamente", False, (255, 255, 255))

        self.passaro = Passaro()
        self.chao = Chao()
        self.estado = "inicio"

    def eventos(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    if self.estado == "inicio" or self.estado == "gameover":
                        self.estado = "jogando"
                        self.passaro = Passaro()

                    elif self.estado == "jogando":
                        self.passaro.jump()

    def atualizar(self):

        if self.estado == "jogando":

            self.passaro.update()

            rect_passaro = pygame.Rect(self.passaro.pos_x, self.passaro.pos_y, 40, 40)
            rect_chao = pygame.Rect(self.chao.pos_x, self.chao.pos_y, 600, 100)

            if rect_passaro.colliderect(rect_chao):
                self.estado = "game_over"

    def desenhar(self):

        self.tela.fill((173, 216, 230))

        self.passaro.draw(self.tela)
        self.chao.draw(self.tela)

        if self.estado == "inicio":
            self.tela.blit(self.texto_inicio, (65, 240))

        elif self.estado == "game_over":
            self.tela.blit(self.texto_gameover, (75, 240))

        pygame.display.update()

    def run(self):

        while True:
            self.clock.tick(60)
            self.eventos()
            self.atualizar()
            self.desenhar()


jogo = Game()

jogo.run()
    