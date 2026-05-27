# 🏃 Mestre do Parkour

## 1. Título do Jogo

**Mestre do Parkour**
*Um jogo de plataforma focado em habilidade e precisão.*

---

## 2. Descrição Geral

* **Tipo de jogo:** Plataforma 2D
* **Ambiente:** Cidade com prédios e estruturas urbanas
* **Ideia principal:** O jogador deve pular entre plataformas (prédios) até alcançar o final da fase, evitando cair.

---

## 3. Objetivo do Jogo

O objetivo é chegar até a área final (linha de chegada) de cada fase.

* O jogador deve atravessar os obstáculos
* Evitar cair das plataformas
* Alcançar o final para vencer

---

## 4. Personagem Principal

* **Quem é:** Um praticante de parkour
* **Movimento:** Anda para esquerda/direita e pula
* **Atributos:**

  * Velocidade
  * Gravidade
  * Capacidade de pulo

---

## 5. Inimigos e Obstáculos

* **Inimigos:** Não há inimigos

* **Obstáculos:**

  * Quedas entre prédios
  * Diferenças de altura entre plataformas
  * Obstaculos nos predios e objetos para interação(futuramente)

* **Colisão:**

  * Se cair → jogador morre e o jogo reinicia

---

## 6. Cenário (Mapa)

* **Ambiente:** Cidade com prédios

* **Elementos:**

  * Plataformas (prédios)
  * Chão
  * Área de chegada

* **Objetivo final:** Localizado no final da fase

---

## 7. Sistema de Pontuação

* O jogo atualmente **não possui sistema de pontuação**
* Foco está na progressão e conclusão das fases

---

## 8. Sistema de Vida

* O jogador possui **1 vida**
* Ao cair:

  * Morre automaticamente
  * Retorna ao menu

---

## 9. Controles

| Tecla   | Função                 |
| ------- | ---------------------- |
| A / ←   | Mover para esquerda    |
| D / →   | Mover para direita     |
| ESPAÇO  | Pular                  |
| 1, 2, 3 | Escolher fase          |
| R       | Reiniciar (na vitória) |
| Q       | Dash                   |
---

## 10. Fluxo do Jogo

1. O jogo inicia no menu
2. O jogador escolhe uma fase
3. Durante a fase:

   * Move-se pelas plataformas
   * Evita cair
4. Condições:

   * **Vitória:** chegar ao final
   * **Derrota:** cair das plataformas

---

## 11. Regras do Jogo

* Não é possível atravessar plataformas
* O jogador sofre gravidade constante
* Só pode pular quando está no chão
* Cair de qualquer altura resulta em morte

---

## 12. Estrutura do Projeto

```
Mestre-do-Parkour/
├── assets/
│   └── fundo.jpeg
├── fases/
├── config.py
├── main.py
├── plataforma.py
├── player.py
└── README.md
```

---

## 13. Funcionalidades Mínimas

* Movimento do jogador
* Sistema de pulo
* Colisão com plataformas
* Sistema de morte ao cair
* Tela de menu
* Seleção de fases
* Tela de vitória
* Fundo com imagem

---

## 14. Melhorias Futuras

CRONOGRAMA

Semana 1 — Base do jogo
- melhorar colisão
- ajustar física
- melhorar câmera
- corrigir bugs
- estabilizar movimentação
- retirar a mecânica de dash (causa bugs e não se encaixa na proposta do jogo)

---

Semana 2 — Construção da fase
- aumentar mapa
- criar mais fases
- melhorar parkour
- ajustar dificuldade
- melhorar posicionamento dos prédios
- criar pulos mais interessantes

---

Semana 3 — Visual
- criar o personagem e suas animações(ainda não será adicionado no jogo)
- textura dos prédios
- criação do senário(ainda não vai estar no jogo)
- HUD
- melhorar tela inicial
- melhorar tela de vitória

---
 Semana 4 — Organização do código
- adicionar herança
- criar classe Objeto
- limpar código
- organizar melhor arquivos

---

Semana 5 — Nova mecânica: Pulo Duplo
- adicionar pulo duplo
- ajustar altura do segundo pulo
- equilibrar dificuldade da fase
- criar partes da fase usando o pulo duplo
- adicionar efeito visual simples no segundo pulo

---

Semana 6 — Polimento final
- corrigir bugs
- testar tudo
- melhorar detalhes
- organizar GitHub
- adicionar o personagem e o senário

---

## 🚀 Tecnologias Utilizadas

* Python(3.11)
* Pygame(2.6.1)

---

## 📌 Status do Projeto

Em desenvolvimento 🚧
