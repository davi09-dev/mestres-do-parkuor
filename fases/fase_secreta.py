import pygame

from plataforma import Plataforma
from config import *


# ==================================================
# CLASSE FASE SECRETA
# ==================================================

class FaseSecreta:

    def __init__(self):

        # ==================================================
        # PLATAFORMAS
        # ==================================================

        # Lista que guarda todas as plataformas
        self.plataformas = []


        # ==================================================
        # FUNDO
        # ==================================================

        # Carrega o fundo da fase
        self.fundo = pygame.image.load(
            "assets/fundo.jpg"
        ).convert()

        # Ajusta o fundo ao tamanho da tela
        self.fundo = pygame.transform.scale(
            self.fundo,
            (largura, altura)
        )


        # ==================================================
        # CRIAÇÃO DO MAPA
        # ==================================================

        self.criar_plataformas()


        # ==================================================
        # CHEGADA
        # ==================================================

        # Define a área onde o jogador termina a fase
        self.chegada = pygame.Rect(
            1800,
            180,
            60,
            60
        )


        # Carrega a imagem da bandeira
        self.imagem_chegada = pygame.image.load(
            "assets/chegada.png"
        ).convert_alpha()


        # Ajusta o tamanho da bandeira
        self.imagem_chegada = pygame.transform.scale(
            self.imagem_chegada,
            (60, 60)
        )


    # ==================================================
    # CRIAÇÃO DAS PLATAFORMAS
    # ==================================================

    def criar_plataformas(self):

        # Cada dicionário representa uma plataforma
        # da fase secreta.
        predios = [

            # Local onde o jogador aparece
            {
                "x": 80,
                "y": 400,
                "largura": 120,
                "altura": 20
            },


            # Primeiro caminho
            {
                "x": 280,
                "y": 350,
                "largura": 90,
                "altura": 300
            },

            {
                "x": 470,
                "y": 250,
                "largura": 80,
                "altura": 400
            },

            {
                "x": 650,
                "y": 400,
                "largura": 80,
                "altura": 250
            },


            # Segundo caminho
            {
                "x": 850,
                "y": 300,
                "largura": 70,
                "altura": 350
            },

            {
                "x": 1030,
                "y": 200,
                "largura": 70,
                "altura": 450
            },

            {
                "x": 1210,
                "y": 350,
                "largura": 70,
                "altura": 300
            },


            # Terceiro caminho
            {
                "x": 1390,
                "y": 250,
                "largura": 70,
                "altura": 400
            },

            {
                "x": 1570,
                "y": 350,
                "largura": 70,
                "altura": 300
            },


            # Prédio final
            {
                "x": 1750,
                "y": 240,
                "largura": 180,
                "altura": 360
            }
        ]


        # Cria um objeto Plataforma para
        # cada item da lista
        for predio in predios:

            self.plataformas.append(
                Plataforma(
                    predio["x"],
                    predio["y"],
                    predio["largura"],
                    predio["altura"]
                )
            )


    # ==================================================
    # DESENHO DA FASE
    # ==================================================

    def desenhar(self, tela, camera_x):

        # Pega a largura do fundo
        largura_fundo = self.fundo.get_width()


        # ==================================================
        # PARALAXE
        # ==================================================

        # Faz o fundo se movimentar mais lentamente
        # que o jogador, criando o efeito de profundidade.
        x_fundo = (
            -(camera_x * 0.2)
        ) % largura_fundo


        # Desenha uma cópia do fundo
        tela.blit(
            self.fundo,
            (
                x_fundo - largura_fundo,
                0
            )
        )


        # Desenha outra cópia para preencher a tela
        tela.blit(
            self.fundo,
            (
                x_fundo,
                0
            )
        )


        # ==================================================
        # PLATAFORMAS
        # ==================================================

        # Desenha todas as plataformas da fase
        for plataforma in self.plataformas:

            plataforma.desenhar(
                tela,
                camera_x
            )


        # ==================================================
        # CHEGADA
        # ==================================================

        # Desenha a bandeira no final da fase
        tela.blit(
            self.imagem_chegada,
            (
                self.chegada.x - camera_x,
                self.chegada.y
            )
        )