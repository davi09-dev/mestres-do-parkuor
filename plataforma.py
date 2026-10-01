from entidade import Entidade
from config import cor_plataforma


# Plataforma herda características de Entidade
class Plataforma(Entidade):

    def __init__(self, x, y, largura, altura):

        # Usa o construtor da classe Entidade
        super().__init__(
            x,
            y,
            largura,
            altura
        )


# Desenha a plataforma
    def desenhar(self, tela, camera_x):

        # Usa o método desenhar da classe Entidade
        super().desenhar(
            tela,
            camera_x,
            cor_plataforma
        )