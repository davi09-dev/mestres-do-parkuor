import pygame

from plataforma import Plataforma
from config import *


# Classe responsável pela fase secreta
class FaseSecreta:

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

        # Cria as plataformas
        self.criar_plataformas()

        # Define a posição da chegada
        self.chegada = pygame.Rect(
            1800,
            180,
            60,
            60
        )

        # Carrega a imagem da bandeira
        self.imagem_chegada = pygame.image.load(
            "assets\chegada.png"
        ).convert_alpha()

        # Ajusta o tamanho da bandeira
        self.imagem_chegada = pygame.transform.scale(
            self.imagem_chegada,
            (60, 60)
        )

    # Cria o mapa da fase secreta
    def criar_plataformas(self):

        # Lista com as plataformas da fase
        predios = [

            # Local onde o jogador aparece
            {"x": 80, "y": 400, "largura": 120, "altura": 20},

            # Primeiro caminho
            {"x": 280, "y": 350, "largura": 90, "altura": 300},
            {"x": 470, "y": 250, "largura": 80, "altura": 400},
            {"x": 650, "y": 400, "largura": 80, "altura": 250},

            # Segundo caminho
            {"x": 850, "y": 300, "largura": 70, "altura": 350},
            {"x": 1030, "y": 200, "largura": 70, "altura": 450},
            {"x": 1210, "y": 350, "largura": 70, "altura": 300},

            # Terceiro caminho
            {"x": 1390, "y": 250, "largura": 70, "altura": 400},
            {"x": 1570, "y": 350, "largura": 70, "altura": 300},

            # Prédio final
            {"x": 1750, "y": 240, "largura": 180, "altura": 360},
        ]

        # Cria as plataformas
        for predio in predios:

            self.plataformas.append(
                Plataforma(
                    predio["x"],
                    predio["y"],
                    predio["largura"],
                    predio["altura"]
                )
            )

    # Desenha a fase secreta
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