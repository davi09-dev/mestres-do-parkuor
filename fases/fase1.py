import pygame
from plataforma import Plataforma
from config import cor_chegada

class Fase1:

    def __init__(self):

        self.plataformas = []

        # spawn
        self.plataformas.append(
            Plataforma(80, 300, 140, 20)
        )

        plataformas_dados = [

            (300, 420, 120, 300),
            (520, 360, 100, 300),
            (820, 300, 120, 300),
            (1050, 420, 100, 300),
            (1250, 350, 100, 300),
            (1450, 280, 100, 320),
            (1650, 380, 80, 250),
            (1820, 340, 80, 260),
            (1980, 300, 80, 300),
            (2250, 260, 120, 340),
            (2600, 360, 100, 240),
            (2780, 420, 100, 180),
            (3050, 350, 120, 250),
            (3280, 280, 120, 320),
            (3600, 220, 200, 400)
        ]

        for dados in plataformas_dados:

            x, y, largura, altura = dados

            self.plataformas.append(
                Plataforma(x, y, largura, altura)
            )

        self.chegada = pygame.Rect(
            3670,
            160,
            60,
            60
        )

    def desenhar(self, tela, camera_x):

        for plataforma in self.plataformas:

            plataforma.desenhar(tela, camera_x)

        pygame.draw.rect(
            tela,
            cor_chegada,
            (
                self.chegada.x - camera_x,
                self.chegada.y,
                self.chegada.width,
                self.chegada.height
            )
        )