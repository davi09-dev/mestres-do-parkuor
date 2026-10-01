import pygame

from plataforma import Plataforma
from config import *


# Classe responsável pela segunda fase
class Fase2:

    def __init__(self):

        # Lista que guarda todas as plataformas
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

        # Cria as plataformas da fase
        self.criar_plataformas()

        # Define a área de chegada
        self.chegada = pygame.Rect(
            3700,
            150,
            60,
            60
        )

        # Carrega a imagem da bandeira
        self.imagem_chegada = pygame.image.load(
            "assets\chegada.png"
        ).convert_alpha()

        # Define o tamanho da bandeira
        self.imagem_chegada = pygame.transform.scale(
            self.imagem_chegada,
            (60, 60)
        )


# Cria as plataformas da fase
    def criar_plataformas(self):

        # Lista com as posições e tamanhos dos prédios
        predios = [

            # Spawn
            {"x": 80, "y": 300, "largura": 120, "altura": 20},

            # Parte 1
            {"x": 280, "y": 430, "largura": 80, "altura": 300},
            {"x": 450, "y": 330, "largura": 70, "altura": 300},
            {"x": 620, "y": 450, "largura": 70, "altura": 250},
            {"x": 790, "y": 280, "largura": 80, "altura": 350},

            # Parte 2
            {"x": 1000, "y": 380, "largura": 70, "altura": 250},
            {"x": 1160, "y": 250, "largura": 70, "altura": 380},
            {"x": 1330, "y": 400, "largura": 60, "altura": 230},
            {"x": 1480, "y": 220, "largura": 70, "altura": 410},

            # Parte 3
            {"x": 1660, "y": 350, "largura": 60, "altura": 280},
            {"x": 1810, "y": 180, "largura": 60, "altura": 450},
            {"x": 1970, "y": 320, "largura": 60, "altura": 310},
            {"x": 2130, "y": 150, "largura": 70, "altura": 480},

            # Parte 4
            {"x": 2310, "y": 380, "largura": 60, "altura": 250},
            {"x": 2460, "y": 250, "largura": 60, "altura": 380},
            {"x": 2620, "y": 400, "largura": 60, "altura": 230},
            {"x": 2780, "y": 200, "largura": 70, "altura": 430},

            # Parte 5
            {"x": 2960, "y": 340, "largura": 60, "altura": 290},
            {"x": 3120, "y": 180, "largura": 70, "altura": 450},
            {"x": 3290, "y": 300, "largura": 70, "altura": 330},
            {"x": 3450, "y": 220, "largura": 80, "altura": 410},

            # Prédio final
            {"x": 3650, "y": 240, "largura": 180, "altura": 360},
        ]

        # Cria uma plataforma para cada prédio
        for predio in predios:

            self.plataformas.append(
                Plataforma(
                    predio["x"],
                    predio["y"],
                    predio["largura"],
                    predio["altura"]
                )
            )


# Desenha todos os elementos da fase
    def desenhar(self, tela, camera_x):

        # Pega a largura do fundo
        largura_fundo = self.fundo.get_width()

        # Calcula a posição do fundo com efeito de paralaxe
        x_fundo = -(camera_x * 0.2) % largura_fundo

        # Desenha uma cópia do fundo
        tela.blit(
            self.fundo,
            (x_fundo - largura_fundo, 0)
        )

        # Desenha outra cópia do fundo
        tela.blit(
            self.fundo,
            (x_fundo, 0)
        )

        # Desenha todas as plataformas
        for plataforma in self.plataformas:

            plataforma.desenhar(
                tela,
                camera_x
            )

        # Desenha a bandeira
        tela.blit(
            self.imagem_chegada,
            (
                self.chegada.x - camera_x,
                self.chegada.y
            )
        )