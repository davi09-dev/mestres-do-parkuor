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

fonte = pygame.font.SysFont(None, 36)

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

opcoes_menu = [
    "Jogar",
    "Creditos",
    "Sair"
]

opcao_selecionada = 0

while rodando:

    clock.tick(fps)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            # MENU
            if estado == "menu":

                if evento.key == pygame.K_UP:
                    opcao_selecionada -= 1

                elif evento.key == pygame.K_DOWN:
                    opcao_selecionada += 1

                opcao_selecionada %= len(opcoes_menu)

                if evento.key == pygame.K_RETURN:

                    # Jogar
                    if opcao_selecionada == 0:

                        player.resetar(
                            spawn_x,
                            spawn_y
                        )

                        camera_x = 0

                        estado = "jogo"

                    # Créditos
                    elif opcao_selecionada == 1:

                        estado = "creditos"

                    # Sair
                    elif opcao_selecionada == 2:

                        rodando = False

            # JOGO
            elif estado == "jogo":

                if evento.key == pygame.K_SPACE:
                    player.pular()

            # CRÉDITOS
            elif estado == "creditos":

                if evento.key == pygame.K_ESCAPE:
                    estado = "menu"

            # VITÓRIA
            elif estado == "vitoria":

                if evento.key == pygame.K_r:
                    estado = "menu"

    teclas = pygame.key.get_pressed()

    tela.fill(cor_fundo)

    # ================= MENU =================

    if estado == "menu":

        titulo = fonte.render(
            "MESTRE DO PARKOUR",
            True,
            cor_texto
        )

        tela.blit(
            titulo,
            (
                largura // 2 - titulo.get_width() // 2,
                120
            )
        )

        for i, opcao in enumerate(opcoes_menu):

            prefixo = "> " if i == opcao_selecionada else "  "

            texto = fonte.render(
                prefixo + opcao,
                True,
                cor_texto
            )

            tela.blit(
                texto,
                (
                    largura // 2 - texto.get_width() // 2,
                    240 + i * 50
                )
            )

    # ================= JOGO =================

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

    # ================= CRÉDITOS =================

    elif estado == "creditos":

        titulo = fonte.render(
            "CREDITOS",
            True,
            cor_texto
        )

        tela.blit(
            titulo,
            (
                largura // 2 - titulo.get_width() // 2,
                100
            )
        )

        nomes = [
            "Davi Araujo",
            "Ytalo Kaua",
            "Pablo Lorran"
        ]

        for i, nome in enumerate(nomes):

            texto = fonte.render(
                nome,
                True,
                cor_texto
            )

            tela.blit(
                texto,
                (
                    largura // 2 - texto.get_width() // 2,
                    200 + i * 50
                )
            )

        voltar = fonte.render(
            "Pressione ESC para voltar",
            True,
            cor_texto
        )

        tela.blit(
            voltar,
            (
                largura // 2 - voltar.get_width() // 2,
                430
            )
        )

    # ================= VITÓRIA =================

    elif estado == "vitoria":

        texto = fonte.render(
            "VOCE VENCEU!",
            True,
            cor_texto
        )

        tela.blit(
            texto,
            (
                largura // 2 - texto.get_width() // 2,
                250
            )
        )

        reiniciar = fonte.render(
            "Pressione R para voltar ao menu",
            True,
            cor_texto
        )

        tela.blit(
            reiniciar,
            (
                largura // 2 - reiniciar.get_width() // 2,
                320
            )
        )

    pygame.display.update()

pygame.quit()