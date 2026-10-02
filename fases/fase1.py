import pygame

from config import *
from plataforma import Plataforma


# ==================================================
# CLASSE FASE 1
# ==================================================

class Fase1:

    def __init__(self):

        # ==================================================
        # FUNDO
        # ==================================================

        # Carrega a imagem do cenário
        self.fundo = pygame.image.load(
            "assets/fundo.jpg"
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

        # Lista que armazenará todas as plataformas
        self.plataformas = []


        # Plataforma inicial onde o jogador aparece
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

        # Cada dicionário representa um prédio.
        #
        # x       = posição horizontal
        # largura = largura do prédio
        # altura  = altura do prédio
        predios = [

            {"x": 300, "largura": 120, "altura": 180},
            {"x": 520, "largura": 100, "altura": 240},
            {"x": 760, "largura": 120, "altura": 320},
            {"x": 1050, "largura": 90, "altura": 180},
            {"x": 1230, "largura": 90, "altura": 260},
            {"x": 1450, "largura": 80, "altura": 350},
            {"x": 1620, "largura": 70, "altura": 220},
            {"x": 1760, "largura": 70, "altura": 280},
            {"x": 1900, "largura": 70, "altura": 340},
            {"x": 2000, "largura": 100, "altura": 240},
            {"x": 2180, "largura": 90, "altura": 300},
            {"x": 2350, "largura": 80, "altura": 200},
            {"x": 2450, "largura": 100, "altura": 260},
            {"x": 2640, "largura": 100, "altura": 340},
            {"x": 2850, "largura": 120, "altura": 420},
            {"x": 3100, "largura": 80, "altura": 260},
            {"x": 3260, "largura": 80, "altura": 320},
            {"x": 3400, "largura": 100, "altura": 380},
            {"x": 3550, "largura": 180, "altura": 360}
        ]


        # Cria uma Plataforma para cada prédio
        for predio in predios:

            x = predio["x"]

            altura_predio = predio["altura"]

            # Posiciona o prédio começando
            # na parte inferior da tela
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

        # Área que detecta quando o jogador chegou ao final
        self.chegada = pygame.Rect(
            3550,
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

        # Começa do índice 1 porque o índice 0
        # é a plataforma inicial
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

            # Distância entre as janelas
            espaco = 25


            # Cria as janelas verticalmente
            for y in range(
                plataforma.rect.y + 20,
                plataforma.rect.bottom - 10,
                espaco
            ):

                # Cria as janelas horizontalmente
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

        # Desenha a bandeira na posição da chegada
        tela.blit(
            self.imagem_chegada,
            (
                self.chegada.x - camera_x,
                self.chegada.y
            )
        )