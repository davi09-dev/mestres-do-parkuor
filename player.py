import pygame

from config import *
from entidade import Entidade


class Player(Entidade):

    def __init__(self, x, y):

        super().__init__(
            x,
            y,
            40,
            60
        )

        self.vel_x = 0
        self.vel_y = 0

        self.velocidade = 5
        self.forca_pulo = -14

        self.no_chao = False

        self.direcao = 1

        self.frame = 0
        self.tempo_animacao = 0

        # ================= SPRITES =================

        self.sprite_andar = pygame.image.load(
            "assets/andar_sprites.png"
        ).convert_alpha()

        self.sprite_pular = pygame.image.load(
            "assets/pular_sprites.png"
        ).convert_alpha()

        # ================= ANDAR =================

        # Linha de cima = esquerda
        andar_esquerda = [
            (36, 39, 238, 311),
            (362, 40, 235, 310),
            (697, 33, 243, 322),
            (1031, 38, 237, 313),
            (1369, 31, 230, 324),
            (1762, 34, 180, 319)
        ]

        # Linha de baixo = direita
        andar_direita = [
            (36, 439, 211, 254),
            (330, 435, 205, 261),
            (656, 432, 227, 265),
            (1005, 432, 215, 260),
            (1328, 434, 216, 260),
            (1756, 434, 147, 264)
        ]

        self.frames_andar_esquerda = self.carregar_frames(
            self.sprite_andar,
            andar_esquerda
        )

        self.frames_andar_direita = self.carregar_frames(
            self.sprite_andar,
            andar_direita
        )

        # ================= PULAR =================

        # Linha de cima = direita
        pular_direita = [
            (27, 227, 181, 223),
            (256, 224, 186, 231),
            (483, 212, 179, 226),
            (712, 161, 166, 217),
            (936, 135, 167, 197),
            (1154, 211, 166, 228),
            (1354, 239, 193, 218),
            (1565, 236, 181, 221)
        ]

        # Linha de baixo = esquerda
        pular_esquerda = [
            (55, 581, 180, 216),
            (274, 584, 194, 219),
            (495, 572, 183, 208),
            (723, 527, 165, 200),
            (945, 512, 158, 208),
            (1163, 580, 165, 222),
            (1396, 597, 159, 226),
            (1598, 603, 158, 217)
        ]

        self.frames_pular_direita = self.carregar_frames(
            self.sprite_pular,
            pular_direita
        )

        self.frames_pular_esquerda = self.carregar_frames(
            self.sprite_pular,
            pular_esquerda
        )

        self.imagem = self.frames_andar_direita[0]

    def carregar_frames(self, imagem, areas):

        frames = []

        for area in areas:

            x, y, largura, altura = area

            frame = imagem.subsurface(
                pygame.Rect(
                    x,
                    y,
                    largura,
                    altura
                )
            ).copy()

            # Mantém a proporção original
            escala = min(
                35 / largura,
                35 / altura
            )

            nova_largura = int(largura * escala)
            nova_altura = int(altura * escala)

            frame = pygame.transform.scale(
                frame,
                (
                    nova_largura,
                    nova_altura
                )
            )

            frames.append(frame)

        return frames

    def mover(self, teclas, inverter=False):

        self.vel_x = 0

        if teclas[pygame.K_a]:

            if inverter:
                self.vel_x = self.velocidade
                self.direcao = 1

            else:
                self.vel_x = -self.velocidade
                self.direcao = -1

        if teclas[pygame.K_d]:

            if inverter:
                self.vel_x = -self.velocidade
                self.direcao = -1

            else:
                self.vel_x = self.velocidade
                self.direcao = 1

    def pular(self):

        if self.no_chao:

            self.vel_y = self.forca_pulo
            self.no_chao = False

            self.frame = 0
            self.tempo_animacao = 0

    def atualizar(self, plataformas):

        self.vel_y += gravidade

        # Movimento horizontal
        self.rect.x += self.vel_x

        # Colisão horizontal
        for plataforma in plataformas:

            if self.rect.colliderect(plataforma.rect):

                if self.vel_x > 0:

                    self.rect.right = plataforma.rect.left

                elif self.vel_x < 0:

                    self.rect.left = plataforma.rect.right

        # Movimento vertical
        self.rect.y += self.vel_y

        self.no_chao = False

        # Colisão vertical
        for plataforma in plataformas:

            if self.rect.colliderect(plataforma.rect):

                if self.vel_y > 0:

                    self.rect.bottom = plataforma.rect.top
                    self.vel_y = 0
                    self.no_chao = True

                    self.frame = 0

                elif self.vel_y < 0:

                    self.rect.top = plataforma.rect.bottom
                    self.vel_y = 0

        # Animação
        self.tempo_animacao += 1

        # PULANDO
        if not self.no_chao:

            if self.tempo_animacao >= 5:

                self.tempo_animacao = 0
                self.frame += 1

                if self.frame >= 8:
                    self.frame = 7

        # NO CHÃO
        else:

            if self.vel_x != 0:

                if self.tempo_animacao >= 5:

                    self.tempo_animacao = 0
                    self.frame += 1

                    if self.frame >= 6:
                        self.frame = 0

            else:

                self.frame = 0

        # Morte
        if self.rect.y > altura:

            return "morreu"

        return None

    def resetar(self, x, y):

        self.rect.x = x
        self.rect.y = y

        self.vel_x = 0
        self.vel_y = 0

        self.no_chao = False

        self.frame = 0
        self.tempo_animacao = 0

    def desenhar(self, tela, camera_x):

        # ================= PULANDO =================

        if not self.no_chao:

            if self.direcao == 1:

                self.imagem = self.frames_pular_direita[
                    min(
                        self.frame,
                        len(self.frames_pular_direita) - 1
                    )
                ]

            else:

                self.imagem = self.frames_pular_esquerda[
                    min(
                        self.frame,
                        len(self.frames_pular_esquerda) - 1
                    )
                ]

        # ================= ANDANDO =================

        elif self.vel_x != 0:

            if self.direcao == 1:

                self.imagem = self.frames_andar_direita[
                    min(
                        self.frame,
                        len(self.frames_andar_direita) - 1
                    )
                ]

            else:

                self.imagem = self.frames_andar_esquerda[
                    min(
                        self.frame,
                        len(self.frames_andar_esquerda) - 1
                    )
                ]

        # ================= PARADO =================

        else:

            if self.direcao == 1:

                self.imagem = self.frames_andar_direita[0]

            else:

                self.imagem = self.frames_andar_esquerda[0]

        # Mantém os pés do personagem no chão
        x = self.rect.centerx - self.imagem.get_width() // 2

        y = self.rect.bottom - self.imagem.get_height()

        tela.blit(
            self.imagem,
            (
                x - camera_x,
                y
            )
        )