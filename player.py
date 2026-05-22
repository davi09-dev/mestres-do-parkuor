import pygame
from config import *

class Player:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 40, 60)
        self.vel_x = 0
        self.vel_y = 0
        self.velocidade = 5
        self.forca_pulo = -15
        self.no_chao = False

        # DASH
        self.vel_dash = 15
        self.pode_dash = True
        self.dash_tempo = 0
        self.direcao = 1

    def mover(self, teclas):

        if self.dash_tempo <= 0:
            self.vel_x = 0

            if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
                self.vel_x = -self.velocidade
                self.direcao = -1

            if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
                self.vel_x = self.velocidade
                self.direcao = 1

    def pular(self):

        if self.no_chao:
            self.vel_y = self.forca_pulo
            self.no_chao = False

    def dash(self):

        if self.pode_dash:
            self.vel_x = self.vel_dash * self.direcao
            self.dash_tempo = 10
            self.pode_dash = False

    def atualizar(self, plataformas):
        self.vel_y += gravidade

        # duração dash
        if self.dash_tempo > 0:
            self.dash_tempo -= 1
        else:
            self.vel_x *= 0.8

        self.rect.x += self.vel_x

        for plataforma in plataformas:

            if self.rect.colliderect(plataforma.rect):

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
                    self.pode_dash = True
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