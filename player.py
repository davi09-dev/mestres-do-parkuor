import pygame

from config import *
from entidade import Entidade


class Player(Entidade):

    def __init__(self, x, y):

        super().__init__(
            x,
            y,
            40,
            60
        )

        # IMAGEM DO PLAYER
        self.imagem = pygame.image.load(
            "ChatGpt1.png"
        ).convert_alpha()

        self.imagem = pygame.transform.scale(
            self.imagem,
            (40, 60)
        )

        self.vel_x = 0
        self.vel_y = 0

        self.velocidade = 5
        self.forca_pulo = -14

        self.no_chao = False

    def mover(self, teclas):

        self.vel_x = 0

        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:

            self.vel_x = -self.velocidade

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:

            self.vel_x = self.velocidade

    def pular(self):

        if self.no_chao:

            self.vel_y = self.forca_pulo
            self.no_chao = False

    def atualizar(self, plataformas):

        self.vel_y += gravidade

        # Movimento horizontal
        self.rect.x += self.vel_x

        # Colisão horizontal
        for plataforma in plataformas:

            if self.rect.colliderect(plataforma.rect):

                if self.vel_x > 0:

                    self.rect.right = plataforma.rect.left

                elif self.vel_x < 0:

                    self.rect.left = plataforma.rect.right

        # Movimento vertical
        self.rect.y += self.vel_y

        self.no_chao = False

        # Colisão vertical
        for plataforma in plataformas:

            if self.rect.colliderect(plataforma.rect):

                if self.vel_y > 0:

                    self.rect.bottom = plataforma.rect.top
                    self.vel_y = 0
                    self.no_chao = True

                elif self.vel_y < 0:

                    self.rect.top = plataforma.rect.bottom
                    self.vel_y = 0

        # Morte
        if self.rect.y > altura:

            return "morreu"

        return None

    def resetar(self, x, y):

        self.rect.x = x
        self.rect.y = y

        self.vel_x = 0
        self.vel_y = 0

        self.no_chao = False

    def desenhar(self, tela, camera_x):

        # DESENHA A IMAGEM DO BONECO
        tela.blit(
            self.imagem,
            (
                self.rect.x - camera_x,
                self.rect.y
            )
        )