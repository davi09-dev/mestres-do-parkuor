import pygame
import os

from config import *
from player import Player
from fases.fase1 import Fase1
from fases.fase2 import Fase2
from fases.fase3 import Fase3
from fases.fase_secreta import FaseSecreta

# ==================================================
# INICIALIZAÇÃO DO PYGAME
# ==================================================

pygame.init()

# ==================================================
# CONFIGURAÇÃO DA TELA
# ==================================================

tela = pygame.display.set_mode(
    (largura, altura)
)

pygame.display.set_caption(
    "Mestre do Parkour"
)

# Controla a quantidade de FPS do jogo
clock = pygame.time.Clock()

# ==================================================
# FONTES
# ==================================================

# Fonte principal
fonte = pygame.font.SysFont(
    None,
    36
)

# Fonte menor
fonte_pequena = pygame.font.SysFont(
    None,
    26
)

# Fonte maior para títulos
fonte_grande = pygame.font.SysFont(
    None,
    52
)

# ==================================================
# CERTIFICADO
# ==================================================

# Carrega a imagem do certificado
certificado = pygame.image.load(
    "assets/certificado.png"
).convert()

# Ajusta o certificado para ocupar toda a tela
certificado = pygame.transform.scale(
    certificado,
    (largura, altura)
)

# ==================================================
# RANKING
# ==================================================

# Arquivo usado para guardar os tempos
arquivo_ranking = "ranking.txt"

# Carrega os resultados salvos no arquivo
def carregar_ranking():

    # Cria um ranking separado para cada fase
    ranking = {
        "1": [],
        "2": [],
        "3": [],
        "4": []
    }

    # Se o arquivo ainda não existe,
    # retorna o ranking vazio
    if not os.path.exists(arquivo_ranking):

        return ranking

    # Abre o arquivo no modo de leitura
    with open(
        arquivo_ranking,
        "r",
        encoding="utf-8"
    ) as arquivo:

        linhas = arquivo.readlines()

    # Guarda qual fase está sendo lida
    fase_atual = None

    # Percorre todas as linhas do arquivo
    for linha in linhas:

        # Remove espaços e quebras de linha
        linha = linha.strip()

        # Ignora linhas vazias
        if linha == "":
            continue

        # Verifica se a linha indica uma fase
        if linha.startswith("FASE"):

            numero = linha.replace(
                "FASE ",
                ""
            )

            fase_atual = numero

        else:

            # Divide a linha entre nome e tempo
            partes = linha.split(" - ")

            # Verifica se encontrou nome e tempo
            if len(partes) == 2:

                nome = partes[0]
                tempo = partes[1]

                # Adiciona o jogador na fase correta
                if fase_atual in ranking:

                    ranking[fase_atual].append({
                        "nome": nome,
                        "tempo": tempo
                    })

    # Organiza os jogadores pelo menor tempo
    for fase in ranking:

        ranking[fase].sort(
            key=lambda jogador:
            tempo_para_milisegundos(
                jogador["tempo"]
            )
        )

    return ranking


# Converte o tempo para milissegundos
# Isso facilita a comparação entre os jogadores
def tempo_para_milisegundos(tempo):

    # Divide o tempo em minutos, segundos e centésimos
    partes = tempo.split(":")

    minutos = int(partes[0])
    segundos = int(partes[1])
    centesimos = int(partes[2])

    # Converte tudo para milissegundos
    return (
        minutos * 60000
        + segundos * 1000
        + centesimos * 10
    )


# Salva o ranking no arquivo
def salvar_ranking(ranking):

    # Abre o arquivo no modo de escrita
    with open(
        arquivo_ranking,
        "w",
        encoding="utf-8"
    ) as arquivo:

        # Salva as quatro fases
        for numero_fase in ["1", "2", "3", "4"]:

            arquivo.write(
                "FASE " + numero_fase + "\n"
            )

            # Salva cada jogador daquela fase
            for jogador in ranking[numero_fase]:

                arquivo.write(
                    jogador["nome"]
                    + " - "
                    + jogador["tempo"]
                    + "\n"
                )

            arquivo.write("\n")


# Adiciona um novo resultado ao ranking
def adicionar_ranking(
    numero_fase,
    nome,
    tempo
):

    # Carrega os resultados existentes
    ranking = carregar_ranking()

    # Converte o número da fase para texto
    chave = str(numero_fase)

    # Adiciona o novo resultado
    ranking[chave].append({
        "nome": nome,
        "tempo": formatar_tempo(tempo)
    })

    # Ordena do menor para o maior tempo
    ranking[chave].sort(
        key=lambda jogador:
        tempo_para_milisegundos(
            jogador["tempo"]
        )
    )

    # Mantém somente os 10 melhores resultados
    ranking[chave] = ranking[chave][:10]

    # Salva o ranking atualizado
    salvar_ranking(ranking)


# Formata o tempo para o formato:
# minutos:segundos:centésimos
def formatar_tempo(tempo):

    minutos = tempo // 60000

    segundos = (
        tempo % 60000
    ) // 1000

    centesimos = (
        tempo % 1000
    ) // 10

    return (
        f"{minutos:02d}:"
        f"{segundos:02d}:"
        f"{centesimos:02d}"
    )


# ==================================================
# JOGADOR
# ==================================================

# Posição inicial do jogador
spawn_x = 100
spawn_y = 200

# Cria o objeto jogador
player = Player(
    spawn_x,
    spawn_y
)


# ==================================================
# FASES
# ==================================================

# Cria cada uma das fases
fase1 = Fase1()
fase2 = Fase2()
fase3 = Fase3()
fase_secreta = FaseSecreta()

# Define a fase que está sendo jogada
fase_atual = fase1

# Número da fase atual
numero_fase = 1


# ==================================================
# FASES DESBLOQUEADAS
# ==================================================

# Começa apenas com a Fase 1 liberada
fase_desbloqueada = 1


# ==================================================
# CÂMERA
# ==================================================

# Posição horizontal da câmera
camera_x = 0


# ==================================================
# CRONÔMETRO
# ==================================================

# Momento em que a fase começou
tempo_inicio = 0

# Tempo final da fase
tempo_final = 0


# ==================================================
# NOME DO JOGADOR
# ==================================================

# Nome confirmado do jogador
nome_jogador = ""

# Texto que está sendo digitado
texto_nome = ""


# ==================================================
# ESTADOS DO JOGO
# ==================================================

# Define qual tela está sendo mostrada
estado = "nome"


# ==================================================
# MENU PRINCIPAL
# ==================================================

opcoes_menu = [
    "Jogar",
    "Ranking",
    "Alterar nome",
    "Creditos",
    "Sair"
]

# Opção atualmente selecionada
opcao_menu = 0


# ==================================================
# MENU DE FASES
# ==================================================

opcoes_fases = [
    "Fase 1",
    "Fase 2",
    "Fase 3",
    "Voltar"
]

# Fase atualmente selecionada no menu
opcao_fase = 0


# ==================================================
# LOOP PRINCIPAL
# ==================================================

rodando = True

while rodando:

    # Mantém o jogo na quantidade de FPS definida
    clock.tick(fps)

    # ==================================================
    # EVENTOS
    # ==================================================

    for evento in pygame.event.get():

        # Fecha o jogo
        if evento.type == pygame.QUIT:

            rodando = False

        # Verifica eventos de teclado
        if evento.type == pygame.KEYDOWN:


            # ==================================================
            # TELA DO NOME
            # ==================================================

            if estado == "nome":

                # Apaga uma letra
                if evento.key == pygame.K_BACKSPACE:

                    texto_nome = texto_nome[:-1]


                # Confirma o nome
                elif evento.key == pygame.K_RETURN:

                    # Não permite confirmar um nome vazio
                    if texto_nome.strip() != "":

                        nome_jogador = texto_nome.strip()

                        estado = "menu"


                # Digita o nome
                elif evento.key != pygame.K_ESCAPE:

                    # Limita o nome a 15 caracteres
                    if len(texto_nome) < 15:

                        # Verifica se o caractere pode ser escrito
                        if evento.unicode.isprintable():

                            texto_nome += evento.unicode


            # ==================================================
            # MENU PRINCIPAL
            # ==================================================

            elif estado == "menu":

                # Move a seleção para cima
                if evento.key == pygame.K_UP:

                    opcao_menu -= 1


                # Move a seleção para baixo
                elif evento.key == pygame.K_DOWN:

                    opcao_menu += 1


                # Faz a seleção voltar para o início
                # quando chega ao final
                opcao_menu %= len(opcoes_menu)


                # Confirma a opção selecionada
                if evento.key == pygame.K_RETURN:


                    # JOGAR
                    if opcao_menu == 0:

                        opcao_fase = 0

                        estado = "fases"


                    # RANKING
                    elif opcao_menu == 1:

                        estado = "ranking"


                    # ALTERAR NOME
                    elif opcao_menu == 2:

                        texto_nome = nome_jogador

                        estado = "nome"


                    # CREDITOS
                    elif opcao_menu == 3:

                        estado = "creditos"


                    # SAIR
                    elif opcao_menu == 4:

                        rodando = False


            # ==================================================
            # MENU DE FASES
            # ==================================================

            elif estado == "fases":

                # Move a seleção para cima
                if evento.key == pygame.K_UP:

                    opcao_fase -= 1


                # Move a seleção para baixo
                elif evento.key == pygame.K_DOWN:

                    opcao_fase += 1


                # Faz a seleção voltar para o início
                opcao_fase %= len(opcoes_fases)


                # Volta para o menu principal
                if evento.key == pygame.K_ESCAPE:

                    estado = "menu"


                # Confirma a fase escolhida
                if evento.key == pygame.K_RETURN:


                    # ==================================================
                    # FASE 1
                    # ==================================================

                    if opcao_fase == 0:

                        fase_atual = fase1

                        numero_fase = 1

                        player.resetar(
                            spawn_x,
                            spawn_y
                        )

                        camera_x = 0

                        tempo_inicio = (
                            pygame.time.get_ticks()
                        )

                        tempo_final = 0

                        estado = "jogo"


                    # ==================================================
                    # FASE 2
                    # ==================================================

                    elif opcao_fase == 1:

                        if fase_desbloqueada >= 2:

                            fase_atual = fase2

                            numero_fase = 2

                            player.resetar(
                                spawn_x,
                                spawn_y
                            )

                            camera_x = 0

                            tempo_inicio = (
                                pygame.time.get_ticks()
                            )

                            tempo_final = 0

                            estado = "jogo"


                    # ==================================================
                    # FASE 3
                    # ==================================================

                    elif opcao_fase == 2:

                        if fase_desbloqueada >= 3:

                            fase_atual = fase3

                            numero_fase = 3

                            player.resetar(
                                spawn_x,
                                spawn_y
                            )

                            camera_x = 0

                            tempo_inicio = (
                                pygame.time.get_ticks()
                            )

                            tempo_final = 0

                            estado = "jogo"


                    # ==================================================
                    # VOLTAR
                    # ==================================================

                    elif opcao_fase == 3:

                        estado = "menu"


            # ==================================================
            # RANKING
            # ==================================================

            elif estado == "ranking":

                # ESC volta para o menu
                if evento.key == pygame.K_ESCAPE:

                    estado = "menu"


            # ==================================================
            # CRÉDITOS
            # ==================================================

            elif estado == "creditos":

                # ESC volta para o menu
                if evento.key == pygame.K_ESCAPE:

                    estado = "menu"


            # ==================================================
            # JOGO
            # ==================================================

            elif estado == "jogo":

                # SPACE faz o jogador pular
                if evento.key == pygame.K_SPACE:

                    player.pular()


                # ESC volta para o menu
                if evento.key == pygame.K_ESCAPE:

                    estado = "menu"


            # ==================================================
            # VITÓRIA
            # ==================================================

            elif estado == "vitoria":

                # R volta para o menu de fases
                if evento.key == pygame.K_r:

                    estado = "fases"


            # ==================================================
            # CERTIFICADO
            # ==================================================

            elif estado == "certificado":

                # ENTER joga a fase secreta novamente
                if evento.key == pygame.K_RETURN:

                    fase_atual = fase_secreta

                    numero_fase = 4

                    player.resetar(
                        100,
                        300
                    )

                    camera_x = 0

                    tempo_inicio = (
                        pygame.time.get_ticks()
                    )

                    tempo_final = 0

                    estado = "jogo"


                # ESC volta para o menu
                elif evento.key == pygame.K_ESCAPE:

                    estado = "menu"


    # ==================================================
    # TECLAS PRESSIONADAS
    # ==================================================

    teclas = pygame.key.get_pressed()


    # ==================================================
    # LIMPA A TELA
    # ==================================================

    tela.fill(cor_fundo)


    # ==================================================
    # TELA DO NOME
    # ==================================================

    if estado == "nome":

        titulo = fonte_grande.render(
            "MESTRE DO PARKOUR",
            True,
            cor_texto
        )

        tela.blit(
            titulo,
            (
                largura // 2
                - titulo.get_width() // 2,
                100
            )
        )


        texto = fonte.render(
            "Digite seu nome:",
            True,
            cor_texto
        )

        tela.blit(
            texto,
            (
                largura // 2
                - texto.get_width() // 2,
                210
            )
        )


        nome = fonte.render(
            texto_nome + "_",
            True,
            cor_texto
        )

        tela.blit(
            nome,
            (
                largura // 2
                - nome.get_width() // 2,
                270
            )
        )


        continuar = fonte_pequena.render(
            "Pressione ENTER para continuar",
            True,
            cor_texto
        )

        tela.blit(
            continuar,
            (
                largura // 2
                - continuar.get_width() // 2,
                350
            )
        )


    # ==================================================
    # MENU PRINCIPAL
    # ==================================================

    elif estado == "menu":

        titulo = fonte_grande.render(
            "MESTRE DO PARKOUR",
            True,
            cor_texto
        )

        tela.blit(
            titulo,
            (
                largura // 2
                - titulo.get_width() // 2,
                70
            )
        )


        # Percorre todas as opções do menu
        for i, opcao in enumerate(opcoes_menu):

            # Mostra ">" na opção selecionada
            prefixo = "> " if i == opcao_menu else "  "

            texto = fonte.render(
                prefixo + opcao,
                True,
                cor_texto
            )

            tela.blit(
                texto,
                (
                    largura // 2
                    - texto.get_width() // 2,
                    190 + i * 55
                )
            )


        jogador = fonte_pequena.render(
            "Jogador: " + nome_jogador,
            True,
            cor_texto
        )

        tela.blit(
            jogador,
            (
                largura // 2
                - jogador.get_width() // 2,
                510
            )
        )


    # ==================================================
    # MENU DE FASES
    # ==================================================

    elif estado == "fases":

        titulo = fonte_grande.render(
            "ESCOLHA A FASE",
            True,
            cor_texto
        )

        tela.blit(
            titulo,
            (
                largura // 2
                - titulo.get_width() // 2,
                80
            )
        )


        # Percorre as opções de fase
        for i, opcao in enumerate(opcoes_fases):

            bloqueada = False


            # Verifica se a Fase 2 está bloqueada
            if i == 1 and fase_desbloqueada < 2:

                bloqueada = True


            # Verifica se a Fase 3 está bloqueada
            if i == 2 and fase_desbloqueada < 3:

                bloqueada = True


            # Mostra o texto da opção
            if bloqueada:

                texto_opcao = (
                    opcao
                    + " [BLOQUEADA]"
                )

            else:

                texto_opcao = opcao


            # Mostra ">" na opção selecionada
            prefixo = (
                "> "
                if i == opcao_fase
                else "  "
            )


            texto = fonte.render(
                prefixo + texto_opcao,
                True,
                cor_texto
            )

            tela.blit(
                texto,
                (
                    largura // 2
                    - texto.get_width() // 2,
                    190 + i * 65
                )
            )


    # ==================================================
    # JOGO
    # ==================================================

    elif estado == "jogo":

        # Movimenta o jogador
        player.mover(teclas)


        # Atualiza física e colisões
        resultado = player.atualizar(
            fase_atual.plataformas
        )


        # ==================================================
        # CÂMERA
        # ==================================================

        # Define onde a câmera deveria estar
        alvo_camera = (
            player.rect.x - 400
        )


        # Move a câmera suavemente até o alvo
        camera_x += (
            alvo_camera - camera_x
        ) * suavidade_camera


        # Impede a câmera de passar do início
        camera_x = max(
            0,
            camera_x
        )


        # ==================================================
        # CRONÔMETRO
        # ==================================================

        # Calcula o tempo desde o início da fase
        tempo_atual = (
            pygame.time.get_ticks()
            - tempo_inicio
        )


        # ==================================================
        # MORTE
        # ==================================================

        if resultado == "morreu":

            # Verifica se o jogador estava na Fase 1
            if numero_fase == 1:

                # Se caiu para trás do spawn,
                # acessa a fase secreta
                if player.rect.x < spawn_x:

                    fase_atual = fase_secreta

                    numero_fase = 4

                    player.resetar(
                        100,
                        300
                    )

                    camera_x = 0

                    tempo_inicio = (
                        pygame.time.get_ticks()
                    )

                    tempo_final = 0

                    estado = "jogo"

                else:

                    # Caso contrário, reinicia
                    # e volta ao menu
                    player.resetar(
                        spawn_x,
                        spawn_y
                    )

                    camera_x = 0

                    estado = "menu"

            else:

                # Nas outras fases, volta ao menu
                player.resetar(
                    spawn_x,
                    spawn_y
                )

                camera_x = 0

                estado = "menu"


        # ==================================================
        # VITÓRIA
        # ==================================================

        if player.rect.colliderect(
            fase_atual.chegada
        ):

            # Guarda o tempo final
            tempo_final = (
                pygame.time.get_ticks()
                - tempo_inicio
            )


            # ==================================================
            # FASE SECRETA
            # ==================================================

            if numero_fase == 4:

                # Para o jogador
                player.vel_x = 0
                player.vel_y = 0

                # Mostra o certificado
                estado = "certificado"


            # ==================================================
            # FASES NORMAIS
            # ==================================================

            else:

                # Salva o tempo no ranking
                adicionar_ranking(
                    numero_fase,
                    nome_jogador,
                    tempo_final
                )


                # Para o jogador
                player.vel_x = 0
                player.vel_y = 0


                # Libera a Fase 2
                if numero_fase == 1:

                    if fase_desbloqueada < 2:

                        fase_desbloqueada = 2


                # Libera a Fase 3
                elif numero_fase == 2:

                    if fase_desbloqueada < 3:

                        fase_desbloqueada = 3


                # Vai para a tela de vitória
                estado = "vitoria"


        # ==================================================
        # DESENHO DA FASE
        # ==================================================

        fase_atual.desenhar(
            tela,
            camera_x
        )


        # Desenha o jogador
        player.desenhar(
            tela,
            camera_x
        )


        # ==================================================
        # HUD - CRONÔMETRO
        # ==================================================

        texto_tempo = fonte.render(
            "Tempo: "
            + formatar_tempo(tempo_atual),
            True,
            cor_texto
        )

        tela.blit(
            texto_tempo,
            (20, 20)
        )


        # ==================================================
        # HUD - NOME
        # ==================================================

        texto_jogador = fonte_pequena.render(
            nome_jogador,
            True,
            cor_texto
        )

        tela.blit(
            texto_jogador,
            (20, 55)
        )


    # ==================================================
    # RANKING
    # ==================================================

    elif estado == "ranking":

        titulo = fonte_grande.render(
            "RANKING",
            True,
            cor_texto
        )

        tela.blit(
            titulo,
            (
                largura // 2
                - titulo.get_width() // 2,
                30
            )
        )


        # Carrega o ranking salvo
        ranking = carregar_ranking()


        # Define a posição de cada coluna
        posicoes = [
            170,
            500,
            830
        ]


        # Mostra Fase 1, 2 e 3
        for numero in range(1, 4):

            x = posicoes[numero - 1]


            titulo_fase = fonte.render(
                "FASE " + str(numero),
                True,
                cor_texto
            )

            tela.blit(
                titulo_fase,
                (
                    x
                    - titulo_fase.get_width() // 2,
                    100
                )
            )


            # Pega os jogadores daquela fase
            jogadores = ranking.get(
                str(numero),
                []
            )


            # Mostra os 10 melhores
            for i, jogador in enumerate(
                jogadores[:10]
            ):

                texto = fonte_pequena.render(
                    str(i + 1)
                    + ". "
                    + jogador["nome"]
                    + " "
                    + jogador["tempo"],
                    True,
                    cor_texto
                )

                tela.blit(
                    texto,
                    (
                        x
                        - texto.get_width() // 2,
                        150 + i * 35
                    )
                )


            # Caso não existam resultados
            if len(jogadores) == 0:

                vazio = fonte_pequena.render(
                    "Nenhum resultado",
                    True,
                    cor_texto
                )

                tela.blit(
                    vazio,
                    (
                        x
                        - vazio.get_width() // 2,
                        160
                    )
                )


    # ==================================================
    # CRÉDITOS
    # ==================================================

    elif estado == "creditos":

        titulo = fonte_grande.render(
            "CREDITOS",
            True,
            cor_texto
        )

        tela.blit(
            titulo,
            (
                largura // 2
                - titulo.get_width() // 2,
                100
            )
        )


        # Nomes dos integrantes do grupo
        nomes = [
            "Davi Araujo",
            "Ytalo Kaua",
            "Pablo Lorran"
        ]


        # Mostra os nomes na tela
        for i, nome in enumerate(nomes):

            texto = fonte.render(
                nome,
                True,
                cor_texto
            )

            tela.blit(
                texto,
                (
                    largura // 2
                    - texto.get_width() // 2,
                    200 + i * 50
                )
            )


    # ==================================================
    # TELA DE VITÓRIA
    # ==================================================

    elif estado == "vitoria":

        # Verifica se a vitória foi na fase secreta
        if numero_fase == 4:

            titulo = fonte_grande.render(
                "FASE SECRETA CONCLUIDA!",
                True,
                cor_texto
            )

            tela.blit(
                titulo,
                (
                    largura // 2
                    - titulo.get_width() // 2,
                    130
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
                    largura // 2
                    - segredo.get_width() // 2,
                    200
                )
            )

        else:

            # Tela de vitória das fases normais
            titulo = fonte_grande.render(
                "VOCE VENCEU!",
                True,
                cor_texto
            )

            tela.blit(
                titulo,
                (
                    largura // 2
                    - titulo.get_width() // 2,
                    130
                )
            )


            fase_vencida = fonte.render(
                "Fase "
                + str(numero_fase)
                + " concluida!",
                True,
                cor_texto
            )

            tela.blit(
                fase_vencida,
                (
                    largura // 2
                    - fase_vencida.get_width() // 2,
                    200
                )
            )


        # Mostra o nome do jogador
        nome_final = fonte.render(
            "Jogador: "
            + nome_jogador,
            True,
            cor_texto
        )

        tela.blit(
            nome_final,
            (
                largura // 2
                - nome_final.get_width() // 2,
                270
            )
        )


        # Mostra o tempo final
        tempo_final_texto = fonte_grande.render(
            "Tempo: "
            + formatar_tempo(tempo_final),
            True,
            cor_texto
        )

        tela.blit(
            tempo_final_texto,
            (
                largura // 2
                - tempo_final_texto.get_width() // 2,
                320
            )
        )


        # Instrução para voltar
        voltar = fonte.render(
            "Pressione R para voltar",
            True,
            cor_texto
        )

        tela.blit(
            voltar,
            (
                largura // 2
                - voltar.get_width() // 2,
                420
            )
        )


    # ==================================================
    # CERTIFICADO
    # ==================================================

    elif estado == "certificado":

        # Mostra a imagem do certificado
        tela.blit(
            certificado,
            (0, 0)
        )


        # Opção para jogar novamente
        texto = fonte_pequena.render(
            "ENTER - jogar novamente",
            True,
            cor_texto
        )

        tela.blit(
            texto,
            (
                largura // 2
                - texto.get_width() // 2,
                520
            )
        )


        # Opção para voltar ao menu
        texto = fonte_pequena.render(
            "ESC - voltar ao menu",
            True,
            cor_texto
        )

        tela.blit(
            texto,
            (
                largura // 2
                - texto.get_width() // 2,
                555
            )
        )


    # ==================================================
    # ATUALIZA A TELA
    # ==================================================

    pygame.display.update()


# Encerra o Pygame
pygame.quit()