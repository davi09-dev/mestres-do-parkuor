import pygame

from config import *
from entidade import Entidade


# ==================================================
# CLASSE PLAYER
# ==================================================

# Player também herda da classe Entidade.
#
# Assim, o jogador aproveita o rect criado
# pela classe base.
class Player(Entidade):

    def __init__(self, x, y):

        # Chama o construtor da classe Entidade.
        #
        # O jogador possui 40 pixels de largura
        # e 60 pixels de altura.
        super().__init__(
            x,
            y,
            40,
            60
        )


        # ==================================================
        # IMAGEM
        # ==================================================

        # Carrega a imagem do personagem
        self.imagem = pygame.image.load(
            "assets/personagem.png"
        ).convert_alpha()

        # Ajusta o tamanho da imagem
        self.imagem = pygame.transform.scale(
            self.imagem,
            (40, 60)
        )


        # ==================================================
        # MOVIMENTO
        # ==================================================

        # Velocidade horizontal
        self.vel_x = 0

        # Velocidade vertical
        self.vel_y = 0

        # Velocidade de movimento para os lados
        self.velocidade = 5

        # Força aplicada quando o jogador pula
        self.forca_pulo = -14

        # Indica se o jogador está sobre uma plataforma
        self.no_chao = False


    # ==================================================
    # MOVIMENTAÇÃO
    # ==================================================

    # Controla o movimento horizontal do jogador
    def mover(self, teclas):

        # Começa cada atualização sem movimento horizontal
        self.vel_x = 0


        # Movimento para a esquerda
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:

            self.vel_x = -self.velocidade


        # Movimento para a direita
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:

            self.vel_x = self.velocidade


    # ==================================================
    # PULO
    # ==================================================

    # Faz o jogador pular
    def pular(self):

        # O jogador só pode pular quando está no chão
        if self.no_chao:

            # Aplica a velocidade vertical do pulo
            self.vel_y = self.forca_pulo

            # Agora o jogador está no ar
            self.no_chao = False


    # ==================================================
    # ATUALIZAÇÃO
    # ==================================================

    # Atualiza movimento, gravidade e colisões
    def atualizar(self, plataformas):

        # Aplica a gravidade à velocidade vertical
        self.vel_y += gravidade


        # ==================================================
        # MOVIMENTO HORIZONTAL
        # ==================================================

        self.rect.x += self.vel_x


        # Verifica colisões horizontais
        for plataforma in plataformas:

            if self.rect.colliderect(
                plataforma.rect
            ):

                # Colisão enquanto está indo para a direita
                if self.vel_x > 0:

                    self.rect.right = plataforma.rect.left

                # Colisão enquanto está indo para a esquerda
                elif self.vel_x < 0:

                    self.rect.left = plataforma.rect.right


        # ==================================================
        # MOVIMENTO VERTICAL
        # ==================================================

        self.rect.y += self.vel_y


        # Assume inicialmente que o jogador
        # não está no chão
        self.no_chao = False


        # Verifica colisões verticais
        for plataforma in plataformas:

            if self.rect.colliderect(
                plataforma.rect
            ):

                # Jogador está caindo sobre uma plataforma
                if self.vel_y > 0:

                    self.rect.bottom = plataforma.rect.top

                    # Para a velocidade vertical
                    self.vel_y = 0

                    # Confirma que está no chão
                    self.no_chao = True


                # Jogador está subindo e bateu
                # na parte inferior da plataforma
                elif self.vel_y < 0:

                    self.rect.top = plataforma.rect.bottom

                    # Para a subida
                    self.vel_y = 0


        # ==================================================
        # QUEDA
        # ==================================================

        # Se o jogador ultrapassar a altura da tela,
        # significa que caiu do mapa.
        if self.rect.y > altura:

            return "morreu"


        # Se não morreu, não retorna nenhum resultado
        return None


    # ==================================================
    # RESET DO JOGADOR
    # ==================================================

    # Reinicia a posição e o movimento do jogador
    def resetar(self, x, y):

        # Define a nova posição
        self.rect.x = x
        self.rect.y = y

        # Zera as velocidades
        self.vel_x = 0
        self.vel_y = 0

        # Começa sem estar no chão
        self.no_chao = False


    # ==================================================
    # DESENHO
    # ==================================================

    # Desenha a imagem do jogador na tela
    def desenhar(self, tela, camera_x):

        tela.blit(
            self.imagem,
            (
                self.rect.x - camera_x,
                self.rect.y
            )
        )