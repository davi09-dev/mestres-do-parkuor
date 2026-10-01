import pygame

from config import *
from player import Player
from fases.fase1 import Fase1
from fases.fase2 import Fase2
from fases.fase3 import Fase3
from fases.fase_secreta import FaseSecreta


pygame.init()


# Cria a tela
tela = pygame.display.set_mode(
    (largura, altura)
)

# Define o nome da janela
pygame.display.set_caption(
    "Mestre do Parkour"
)

# Controla o FPS
clock = pygame.time.Clock()

# Fonte usada nos textos
fonte = pygame.font.SysFont(None, 36)


# Define o estado inicial do jogo
estado = "menu"


# Posição inicial do jogador
spawn_x = 100
spawn_y = 200


# Cria o jogador
player = Player(
    spawn_x,
    spawn_y
)


# Cria as fases
fase1 = Fase1()
fase2 = Fase2()
fase3 = Fase3()
fase_secreta = FaseSecreta()


# Define a fase atual
fase_atual = fase1

# Guarda o número da fase atual
numero_fase = 1


# Guarda até qual fase o jogador desbloqueou
fase_desbloqueada = 1


# Controla a posição da câmera
camera_x = 0


# Controla se o jogo está rodando
rodando = True


# Opções do menu
opcoes_menu = [
    "Fase 1",
    "Fase 2",
    "Fase 3",
    "Creditos",
    "Sair"
]


# Guarda a opção selecionada
opcao_selecionada = 0


while rodando:

    # Mantém o jogo em 60 FPS
    clock.tick(fps)


    # Verifica os eventos
    for evento in pygame.event.get():

        # Fecha o jogo
        if evento.type == pygame.QUIT:
            rodando = False


        # Verifica teclas pressionadas
        if evento.type == pygame.KEYDOWN:


            # ================= MENU =================

            if estado == "menu":

                # Sobe no menu
                if evento.key == pygame.K_UP:

                    opcao_selecionada -= 1


                # Desce no menu
                elif evento.key == pygame.K_DOWN:

                    opcao_selecionada += 1


                # Impede de sair das opções
                opcao_selecionada %= len(opcoes_menu)


                # Seleciona uma opção
                if evento.key == pygame.K_RETURN:


                    # ================= FASE 1 =================

                    if opcao_selecionada == 0:

                        fase_atual = fase1

                        numero_fase = 1

                        player.resetar(
                            spawn_x,
                            spawn_y
                        )

                        camera_x = 0

                        estado = "jogo"


                    # ================= FASE 2 =================

                    elif opcao_selecionada == 1:

                        # Verifica se a fase está desbloqueada
                        if fase_desbloqueada >= 2:

                            fase_atual = fase2

                            numero_fase = 2

                            player.resetar(
                                spawn_x,
                                spawn_y
                            )

                            camera_x = 0

                            estado = "jogo"


                    # ================= FASE 3 =================

                    elif opcao_selecionada == 2:

                        # Verifica se a fase está desbloqueada
                        if fase_desbloqueada >= 3:

                            fase_atual = fase3

                            numero_fase = 3

                            player.resetar(
                                spawn_x,
                                spawn_y
                            )

                            camera_x = 0

                            estado = "jogo"


                    # ================= CREDITOS =================

                    elif opcao_selecionada == 3:

                        estado = "creditos"


                    # ================= SAIR =================

                    elif opcao_selecionada == 4:

                        rodando = False


            # ================= JOGO =================

            elif estado == "jogo":

                # Faz o jogador pular
                if evento.key == pygame.K_SPACE:

                    player.pular()


                # Volta para o menu
                if evento.key == pygame.K_ESCAPE:

                    estado = "menu"


            # ================= CREDITOS =================

            elif estado == "creditos":

                # Volta para o menu
                if evento.key == pygame.K_ESCAPE:

                    estado = "menu"


            # ================= VITORIA =================

            elif estado == "vitoria":

                # Volta para o menu
                if evento.key == pygame.K_r:

                    estado = "menu"


    # Pega as teclas que estão sendo pressionadas
    teclas = pygame.key.get_pressed()


    # Limpa a tela
    tela.fill(cor_fundo)


    # ================= MENU =================

    if estado == "menu":

        # Desenha o título
        titulo = fonte.render(
            "MESTRE DO PARKOUR",
            True,
            cor_texto
        )

        tela.blit(
            titulo,
            (
                largura // 2 - titulo.get_width() // 2,
                80
            )
        )


        # Mostra as opções do menu
        for i, opcao in enumerate(opcoes_menu):

            # Verifica se a fase está bloqueada
            bloqueada = False

            if i == 1 and fase_desbloqueada < 2:
                bloqueada = True

            if i == 2 and fase_desbloqueada < 3:
                bloqueada = True


            # Coloca o texto de bloqueada
            if bloqueada:

                texto_opcao = opcao + " [BLOQUEADA]"

            else:

                texto_opcao = opcao


            # Coloca uma seta na opção selecionada
            prefixo = "> " if i == opcao_selecionada else "  "


            # Cria o texto
            texto = fonte.render(
                prefixo + texto_opcao,
                True,
                cor_texto
            )


            # Mostra o texto na tela
            tela.blit(
                texto,
                (
                    largura // 2 - texto.get_width() // 2,
                    180 + i * 55
                )
            )


        # Mostra uma informação sobre a fase secreta
        segredo = fonte.render(
            "Existe um segredo escondido...",
            True,
            cor_texto
        )

        tela.blit(
            segredo,
            (
                largura // 2 - segredo.get_width() // 2,
                500
            )
        )


    # ================= JOGO =================

    elif estado == "jogo":

        # Movimenta o jogador
        player.mover(teclas)


        # Atualiza física e colisões
        resultado = player.atualizar(
            fase_atual.plataformas
        )


        # Calcula onde a câmera deve ficar
        alvo_camera = player.rect.x - 400


        # Move a câmera suavemente
        camera_x += (
            alvo_camera - camera_x
        ) * suavidade_camera


        # Impede a câmera de ir para a esquerda
        camera_x = max(
            0,
            camera_x
        )


        # ================= MORTE =================

        if resultado == "morreu":

            # Verifica se o jogador estava na Fase 1
            if numero_fase == 1:

                # Verifica se caiu para trás do spawn
                if player.rect.x < spawn_x:

                    # Entra na fase secreta
                    fase_atual = fase_secreta

                    numero_fase = 4

                    # Posiciona o jogador no começo da fase secreta
                    player.resetar(
                        100,
                        300
                    )

                    # Reinicia a câmera
                    camera_x = 0

                    # Continua no jogo
                    estado = "jogo"

                else:

                    # Morte normal volta para o menu
                    player.resetar(
                        spawn_x,
                        spawn_y
                    )

                    camera_x = 0

                    estado = "menu"

            else:

                # Morte nas outras fases volta para o menu
                player.resetar(
                    spawn_x,
                    spawn_y
                )

                camera_x = 0

                estado = "menu"


        # ================= VITORIA =================

        if player.rect.colliderect(
            fase_atual.chegada
        ):

            # Para o movimento do jogador
            player.vel_x = 0
            player.vel_y = 0


            # Fase 1 libera a Fase 2
            if numero_fase == 1:

                if fase_desbloqueada < 2:

                    fase_desbloqueada = 2


            # Fase 2 libera a Fase 3
            elif numero_fase == 2:

                if fase_desbloqueada < 3:

                    fase_desbloqueada = 3


            # Vai para a tela de vitória
            estado = "vitoria"


        # Desenha a fase atual
        fase_atual.desenhar(
            tela,
            camera_x
        )


        # Desenha o jogador
        player.desenhar(
            tela,
            camera_x
        )


    # ================= CREDITOS =================

    elif estado == "creditos":

        # Título dos créditos
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


        # Nomes dos integrantes
        nomes = [
            "Davi Araujo",
            "Ytalo Kaua",
            "Pablo Lorran"
        ]


        # Mostra os nomes
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


        # Texto para voltar
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


    # ================= VITORIA =================

    elif estado == "vitoria":

        # Verifica se foi a fase secreta
        if numero_fase == 4:

            texto = fonte.render(
                "FASE SECRETA CONCLUIDA!",
                True,
                cor_texto
            )

            tela.blit(
                texto,
                (
                    largura // 2 - texto.get_width() // 2,
                    220
                )
            )


            segredo = fonte.render(
                "VOCE ENCONTROU O SEGREDO!",
                True,
                cor_texto
            )

            tela.blit(
                segredo,
                (
                    largura // 2 - segredo.get_width() // 2,
                    280
                )
            )


        else:

            # Mensagem normal de vitória
            texto = fonte.render(
                "VOCE VENCEU!",
                True,
                cor_texto
            )

            tela.blit(
                texto,
                (
                    largura // 2 - texto.get_width() // 2,
                    220
                )
            )


            # Mostra qual fase foi concluída
            fase_vencida = fonte.render(
                "Fase " + str(numero_fase) + " concluida!",
                True,
                cor_texto
            )

            tela.blit(
                fase_vencida,
                (
                    largura // 2 - fase_vencida.get_width() // 2,
                    280
                )
            )


        # Texto para voltar ao menu
        reiniciar = fonte.render(
            "Pressione R para voltar ao menu",
            True,
            cor_texto
        )

        tela.blit(
            reiniciar,
            (
                largura // 2 - reiniciar.get_width() // 2,
                350
            )
        )


    # Atualiza a tela
    pygame.display.update()


# Fecha o Pygame
pygame.quit()