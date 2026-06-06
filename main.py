import pygame

from config import *
from player import Player
from fases.fase1 import Fase1

pygame.init()

tela = pygame.display.set_mode(
    (largura, altura)
)

pygame.display.set_caption(
    "Mestre do Parkour"
)

clock = pygame.time.Clock()

fonte = pygame.font.SysFont(None, 48)

estado = "menu"

spawn_x = 100
spawn_y = 200

player = Player(
    spawn_x,
    spawn_y
)

fase = Fase1()

camera_x = 0

rodando = True

while rodando:

    clock.tick(fps)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if estado == "menu":

                if evento.key == pygame.K_SPACE:

                    player.resetar(
                        spawn_x,
                        spawn_y
                    )

                    estado = "jogo"

            elif estado == "jogo":

                if evento.key == pygame.K_SPACE:
                    player.pular()

            elif estado == "vitoria":

                if evento.key == pygame.K_r:
                    estado = "menu"

    teclas = pygame.key.get_pressed()

    tela.fill(cor_fundo)

    # MENU
    if estado == "menu":

        texto = fonte.render(
            "Pressione ESPAÇO",
            True,
            cor_texto
        )

        tela.blit(texto, (250, 250))

    # JOGO
    elif estado == "jogo":

        player.mover(teclas)

        resultado = player.atualizar(
            fase.plataformas
        )

        # câmera
        alvo_camera = player.rect.x - 400

        camera_x += (
            alvo_camera - camera_x
        ) * suavidade_camera

        camera_x = max(0, camera_x)

        # morte
        if resultado == "morreu":

            player.resetar(
                spawn_x,
                spawn_y
            )

            camera_x = 0

            estado = "menu"

        # vitória
        if player.rect.colliderect(
            fase.chegada
        ):
            player.vel_x = 0   
            player.vel_y = 0         

            estado = "vitoria"

        fase.desenhar(
            tela,
            camera_x
        )

        player.desenhar(
            tela,
            camera_x
        )

    # VITÓRIA
    elif estado == "vitoria":

        texto = fonte.render(
            "VOCE VENCEU!",
            True,
            cor_texto
        )

        tela.blit(texto, (280, 250))

    pygame.display.update()

pygame.quit()