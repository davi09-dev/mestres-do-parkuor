from entidade import Entidade
from config import cor_plataforma


# ==================================================
# CLASSE PLATAFORMA
# ==================================================

# Plataforma herda características da classe Entidade.
#
# Portanto, Plataforma possui:
# - rect
# - posição
# - largura
# - altura
# - método desenhar()
#
# A herança evita que seja necessário
# escrever tudo novamente.
class Plataforma(Entidade):

    def __init__(self, x, y, largura, altura):

        # Chama o construtor da classe Entidade
        # usando super().
        super().__init__(
            x,
            y,
            largura,
            altura
        )


    # Desenha a plataforma
    def desenhar(self, tela, camera_x):

        # Reutiliza o método desenhar da classe Entidade,
        # passando a cor específica da plataforma.
        super().desenhar(
            tela,
            camera_x,
            cor_plataforma
        )