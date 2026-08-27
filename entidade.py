import pygame


class Entidade:

    def __init__(self, x, y, largura, altura):

        self.rect = pygame.Rect(
            x,
            y,
            largura,
            altura
        )

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