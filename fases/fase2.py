import pygame

from config import *
from plataforma import Plataforma


# ==================================================
# CLASSE FASE 2
# ==================================================

class Fase2:

    def __init__(self):

        # ==================================================
        # FUNDO
        # ==================================================

        # Carrega o cenário da Fase 2
        self.fundo = pygame.image.load(
            "assets/cenario2.jpg"
        ).convert()

        # Ajusta o fundo ao tamanho da tela
        self.fundo = pygame.transform.scale(
            self.fundo,
            (largura, altura)
        )

        self.largura_fundo = self.fundo.get_width()


        # ==================================================
        # PLATAFORMAS
        # ==================================================

        self.plataformas = []


        # Plataforma inicial
        self.plataformas.append(
            Plataforma(
                80,
                300,
                140,
                20
            )
        )


        # ==================================================
        # PRÉDIOS
        # ==================================================

        predios = [

            {"x": 300, "largura": 100, "altura": 220},
            {"x": 500, "largura": 80, "altura": 300},
            {"x": 700, "largura": 120, "altura": 180},
            {"x": 920, "largura": 80, "altura": 250},
            {"x": 1100, "largura": 100, "altura": 250},
            {"x": 1300, "largura": 70, "altura": 350},
            {"x": 1500, "largura": 100, "altura": 220},
            {"x": 1700, "largura": 80, "altura": 330},
            {"x": 1880, "largura": 70, "altura": 420},
            {"x": 2070, "largura": 100, "altura": 280},
            {"x": 2260, "largura": 80, "altura": 360},
            {"x": 2440, "largura": 100, "altura": 200},
            {"x": 2640, "largura": 80, "altura": 300},
            {"x": 2830, "largura": 100, "altura": 400},
            {"x": 3030, "largura": 80, "altura": 450},
            {"x": 3220, "largura": 100, "altura": 250},
            {"x": 3400, "largura": 80, "altura": 350},
            {"x": 3650, "largura": 180, "altura": 390}
        ]


        # Cria as plataformas dos prédios
        for predio in predios:

            x = predio["x"]

            altura_predio = predio["altura"]

            # Calcula a posição Y do prédio
            y = altura - altura_predio


            plataforma = Plataforma(
                x,
                y,
                predio["largura"],
                altura_predio
            )


            self.plataformas.append(
                plataforma
            )


        # ==================================================
        # CHEGADA
        # ==================================================

        self.chegada = pygame.Rect(
            3700,
            150,
            60,
            60
        )


        # Carrega a bandeira
        self.imagem_chegada = pygame.image.load(
            "assets/chegada.png"
        ).convert_alpha()


        # Ajusta o tamanho da bandeira
        self.imagem_chegada = pygame.transform.scale(
            self.imagem_chegada,
            (60, 60)
        )


    # ==================================================
    # DESENHO DA FASE
    # ==================================================

    def desenhar(self, tela, camera_x):

        # Desenha o fundo
        tela.blit(
            self.fundo,
            (0, 0)
        )


        # ==================================================
        # PLATAFORMA INICIAL
        # ==================================================

        plataforma = self.plataformas[0]

        pygame.draw.rect(
            tela,
            cor_plataforma,
            (
                plataforma.rect.x - camera_x,
                plataforma.rect.y,
                plataforma.rect.width,
                plataforma.rect.height
            )
        )


        # ==================================================
        # PRÉDIOS
        # ==================================================

        for plataforma in self.plataformas[1:]:

            pygame.draw.rect(
                tela,
                cor_plataforma,
                (
                    plataforma.rect.x - camera_x,
                    plataforma.rect.y,
                    plataforma.rect.width,
                    plataforma.rect.height
                )
            )


            # Tamanho das janelas
            tamanho_janela = 12

            # Espaço entre as janelas
            espaco = 25


            # Cria as janelas
            for y in range(
                plataforma.rect.y + 20,
                plataforma.rect.bottom - 10,
                espaco
            ):

                for x in range(
                    plataforma.rect.x + 15,
                    plataforma.rect.right - 10,
                    espaco
                ):

                    pygame.draw.rect(
                        tela,
                        (255, 220, 50),
                        (
                            x - camera_x,
                            y,
                            tamanho_janela,
                            tamanho_janela
                        )
                    )


        # ==================================================
        # CHEGADA
        # ==================================================

        tela.blit(
            self.imagem_chegada,
            (
                self.chegada.x - camera_x,
                self.chegada.y
            )
        )