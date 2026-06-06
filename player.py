import pygame
from config import *

class Player:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 40, 60)
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
        self.rect.x += self.vel_x

        for plataforma in plataformas:

            if self.rect.colliderect(plataforma.rect) and self.vel_x != 0:

                if self.vel_x > 0:
                    self.rect.right = plataforma.rect.left

                elif self.vel_x < 0:
                    self.rect.left = plataforma.rect.right

        self.rect.y += self.vel_y
        self.no_chao = False

        for plataforma in plataformas:

            if self.rect.colliderect(plataforma.rect):
                if self.vel_y > 0:
                    self.rect.bottom = plataforma.rect.top
                    self.vel_y = 0
                    self.no_chao = True
                elif self.vel_y < 0:
                    self.rect.top = plataforma.rect.bottom
                    self.vel_y = 0

        # morte
        if self.rect.y > altura:
            return "morreu"

    def resetar(self, x, y):

        self.rect.x = x
        self.rect.y = y

        self.vel_x = 0
        self.vel_y = 0

        self.no_chao = False

    def desenhar(self, tela, camera_x):

        pygame.draw.rect(
            tela,
            cor_player,
            (
                self.rect.x - camera_x,
                self.rect.y,
                self.rect.width,
                self.rect.height
            )
        )