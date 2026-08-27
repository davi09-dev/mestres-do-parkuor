from entidade import Entidade
from config import cor_plataforma


class Plataforma(Entidade):

    def __init__(self, x, y, largura, altura):

        super().__init__(
            x,
            y,
            largura,
            altura
        )

    def desenhar(self, tela, camera_x):

        super().desenhar(
            tela,
            camera_x,
            cor_plataforma
        )