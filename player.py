import pygame

from config import *
from entidade import Entidade


# Player herda características da classe Entidade
class Player(Entidade):

    def __init__(self, x, y):

        # Chama o construtor da classe Entidade
        super().__init__(
            x,
            y,
            40,
            60
        )

        # Carrega a imagem do jogador
        self.imagem = pygame.image.load(
            "assets\personagem.png"
        ).convert_alpha()

        # Define o tamanho da imagem
        self.imagem = pygame.transform.scale(
            self.imagem,
            (40, 60)
        )

        # Velocidade horizontal
        self.vel_x = 0

        # Velocidade vertical
        self.vel_y = 0

        # Velocidade de movimento
        self.velocidade = 5

        # Força do pulo
        self.forca_pulo = -14

        # Verifica se o jogador está no chão
        self.no_chao = False


# Controla o movimento horizontal
    def mover(self, teclas):

        # Começa sem movimento
        self.vel_x = 0

        # Move para a esquerda
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.vel_x = -self.velocidade

        # Move para a direita
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.vel_x = self.velocidade


# Controla o pulo
    def pular(self):

        # Só permite pular quando está no chão
        if self.no_chao:

            # Aplica uma velocidade para cima
            self.vel_y = self.forca_pulo

            # Informa que o jogador saiu do chão
            self.no_chao = False


# Atualiza a física do jogador
    def atualizar(self, plataformas):

        # Aplica a gravidade
        self.vel_y += gravidade

        # Move horizontalmente
        self.rect.x += self.vel_x

        # Verifica colisões horizontais
        for plataforma in plataformas:

            if self.rect.colliderect(plataforma.rect):

                # Colisão pela direita
                if self.vel_x > 0:
                    self.rect.right = plataforma.rect.left

                # Colisão pela esquerda
                elif self.vel_x < 0:
                    self.rect.left = plataforma.rect.right

        # Move verticalmente
        self.rect.y += self.vel_y

        # Assume que o jogador está no ar
        self.no_chao = False

        # Verifica colisões verticais
        for plataforma in plataformas:

            if self.rect.colliderect(plataforma.rect):

                # Jogador caiu sobre a plataforma
                if self.vel_y > 0:

                    self.rect.bottom = plataforma.rect.top

                    # Para a queda
                    self.vel_y = 0

                    # Informa que está no chão
                    self.no_chao = True

                # Jogador bateu na parte inferior
                elif self.vel_y < 0:

                    self.rect.top = plataforma.rect.bottom

                    # Para o movimento para cima
                    self.vel_y = 0

        # Verifica se o jogador caiu da fase
        if self.rect.y > altura:
            return "morreu"

        # Informa que o jogador continua vivo
        return None


# Volta o jogador para uma posição
    def resetar(self, x, y):

        # Define a posição
        self.rect.x = x
        self.rect.y = y

        # Para os movimentos
        self.vel_x = 0
        self.vel_y = 0

        # Define que não está no chão
        self.no_chao = False


# Desenha o jogador na tela
    def desenhar(self, tela, camera_x):

        # Mostra a imagem na posição do jogador
        tela.blit(
            self.imagem,
            (
                self.rect.x - camera_x,
                self.rect.y
            )
        )