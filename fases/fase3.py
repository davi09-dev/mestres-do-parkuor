import pygame

from plataforma import Plataforma
from config import *


# Classe responsável pela terceira fase
class Fase3:

    def __init__(self):

        # Lista que guarda as plataformas
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

        # Cria o mapa da fase
        self.criar_plataformas()

        # Define a área de chegada
        self.chegada = pygame.Rect(
            3900,
            120,
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


# Cria as plataformas da terceira fase
    def criar_plataformas(self):

        # Lista com posição e tamanho dos prédios
        predios = [

            # Spawn
            {"x": 80, "y": 300, "largura": 110, "altura": 20},

            # Parte 1
            {"x": 260, "y": 450, "largura": 70, "altura": 250},
            {"x": 410, "y": 300, "largura": 60, "altura": 330},
            {"x": 550, "y": 430, "largura": 60, "altura": 200},
            {"x": 690, "y": 220, "largura": 60, "altura": 410},

            # Parte 2
            {"x": 850, "y": 380, "largura": 55, "altura": 250},
            {"x": 990, "y": 180, "largura": 55, "altura": 450},
            {"x": 1130, "y": 400, "largura": 55, "altura": 230},
            {"x": 1270, "y": 140, "largura": 60, "altura": 490},

            # Parte 3
            {"x": 1430, "y": 350, "largura": 55, "altura": 280},
            {"x": 1570, "y": 100, "largura": 55, "altura": 530},
            {"x": 1710, "y": 330, "largura": 55, "altura": 300},
            {"x": 1850, "y": 170, "largura": 55, "altura": 460},

            # Parte 4
            {"x": 2000, "y": 400, "largura": 50, "altura": 230},
            {"x": 2140, "y": 200, "largura": 50, "altura": 430},
            {"x": 2280, "y": 360, "largura": 50, "altura": 270},
            {"x": 2420, "y": 120, "largura": 60, "altura": 510},

            # Parte 5
            {"x": 2580, "y": 380, "largura": 50, "altura": 250},
            {"x": 2720, "y": 160, "largura": 50, "altura": 470},
            {"x": 2860, "y": 340, "largura": 50, "altura": 290},
            {"x": 3000, "y": 100, "largura": 60, "altura": 530},

            # Parte 6
            {"x": 3160, "y": 350, "largura": 50, "altura": 280},
            {"x": 3300, "y": 180, "largura": 50, "altura": 450},
            {"x": 3440, "y": 300, "largura": 50, "altura": 330},
            {"x": 3580, "y": 140, "largura": 60, "altura": 490},

            # Final
            {"x": 3740, "y": 260, "largura": 70, "altura": 370},
            {"x": 3900, "y": 220, "largura": 180, "altura": 380},
        ]

        # Cria cada plataforma
        for predio in predios:

            self.plataformas.append(
                Plataforma(
                    predio["x"],
                    predio["y"],
                    predio["largura"],
                    predio["altura"]
                )
            )


# Desenha a fase
    def desenhar(self, tela, camera_x):

        # Pega a largura do fundo
        largura_fundo = self.fundo.get_width()

        # Cria o efeito de paralaxe
        x_fundo = -(camera_x * 0.2) % largura_fundo

        # Desenha o fundo
        tela.blit(
            self.fundo,
            (x_fundo - largura_fundo, 0)
        )

        tela.blit(
            self.fundo,
            (x_fundo, 0)
        )

        # Desenha as plataformas
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