import pygame
from plataforma import Plataforma
from config import *


class Fase1:
    def __init__(self):

        self.plataformas = []

    # Carrega o fundo
        self.fundo = pygame.image.load(
        "assets/fundo.jpg"
    ).convert()

    # Ajusta o fundo ao tamanho da tela
        self.fundo = pygame.transform.scale(
            self.fundo,
        (largura, altura)
    )

        self.criar_plataformas()

        self.chegada = pygame.Rect(
        3600,
        180,
        60,
        60
    )
    def criar_plataformas(self):

        predios = [

            # Spawn
            {"x": 80, "y": 300, "largura": 140, "altura": 20},

    
            {"x": 300, "y": 420, "largura": 120, "altura": 300},
            {"x": 520, "y": 360, "largura": 100, "altura": 300},
            {"x": 760, "y": 280, "largura": 120, "altura": 340},


            {"x": 1050, "y": 420, "largura": 90, "altura": 250},
            {"x": 1230, "y": 340, "largura": 90, "altura": 280},
            {"x": 1450, "y": 250, "largura": 80, "altura": 350},

    
            {"x": 1620, "y": 380, "largura": 70, "altura": 220},
            {"x": 1760, "y": 320, "largura": 70, "altura": 280},
            {"x": 1900, "y": 260, "largura": 70, "altura": 340},

    
            {"x": 2000, "y": 360, "largura": 100, "altura": 240},
            {"x": 2180, "y": 300, "largura": 90, "altura": 300},
            {"x": 2350, "y": 400, "largura": 80, "altura": 200},

            # Final
            {"x": 2450, "y": 340, "largura": 100, "altura": 260},
            {"x": 2640, "y": 260, "largura": 100, "altura": 340},
            {"x": 2850, "y": 180, "largura": 120, "altura": 420},


            {"x": 3100, "y": 340, "largura": 80, "altura": 260},
            {"x": 3260, "y": 280, "largura": 80, "altura": 320},
            {"x": 3400, "y": 220, "largura": 100, "altura": 380},

            # Prédio final
            {"x": 3550, "y": 240, "largura": 180, "altura": 360},
        ]

        for predio in predios:

            self.plataformas.append(
                Plataforma(
                    predio["x"],
                    predio["y"],
                    predio["largura"],
                    predio["altura"]
                )
            )

    def desenhar(self, tela, camera_x):

    # Fundo repetido
        largura_fundo = self.fundo.get_width()

        x_fundo = -(camera_x * 0.2) % largura_fundo

        tela.blit(
            self.fundo,
            (x_fundo - largura_fundo, 0)
    )

        tela.blit(
            self.fundo,
        (x_fundo, 0)
    )

    # Prédios e plataformas
        for plataforma in self.plataformas:
            plataforma.desenhar(
            tela,
            camera_x
        )

    # Linha de chegada
        pygame.draw.rect(tela,cor_chegada,
        (
            self.chegada.x - camera_x,
            self.chegada.y,
            self.chegada.width,
            self.chegada.height
        )
    )