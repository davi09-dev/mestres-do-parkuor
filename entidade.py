import pygame


# Classe base das entidades do jogo
class Entidade:

    def __init__(self, x, y, largura, altura):

        # Cria o retângulo que representa a entidade
        self.rect = pygame.Rect(
            x,
            y,
            largura,
            altura
        )


# Desenha uma entidade como retângulo
    def desenhar(self, tela, camera_x, cor):

        pygame.draw.rect(
            tela,
            cor,
            (
                self.rect.x - camera_x,
                self.rect.y,
                self.rect.width,
                self.rect.height
            )
        )