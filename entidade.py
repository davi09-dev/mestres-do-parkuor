import pygame


# ==================================================
# CLASSE BASE DAS ENTIDADES
# ==================================================

# Entidade é a classe base usada por outros objetos
# que possuem uma posição e um tamanho no jogo.
class Entidade:

    def __init__(self, x, y, largura, altura):

        # Cria um Rect do Pygame para representar
        # a posição e o tamanho da entidade.
        self.rect = pygame.Rect(
            x,
            y,
            largura,
            altura
        )


    # Desenha a entidade como um retângulo
    def desenhar(self, tela, camera_x, cor):

        pygame.draw.rect(
            tela,
            cor,
            (
                # A câmera é descontada da posição X
                # para criar o efeito de movimentação.
                self.rect.x - camera_x,

                self.rect.y,

                self.rect.width,

                self.rect.height
            )
        )