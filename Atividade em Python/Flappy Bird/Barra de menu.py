import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Definindo cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Dimensões da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Escolha de Personagem")

# Definindo fontes
fonte = pygame.font.Font(None, 74)

# Personagens
personagens = ["Arara Azul", "Flappy Bird", "Flappy red"]

# Função para desenhar o menu de personagens
def desenhar_menu_personagens(selecionado):
    tela.fill(BRANCO)
    
    # Desenhar botões dos personagens
    botoes = []
    for i, personagem in enumerate(personagens):
        cor = VERDE if i == selecionado else AZUL
        botao = pygame.draw.rect(tela, cor, [150, 150 + 100 * i, 500, 75])
        botoes.append(botao)
        
        texto = fonte.render(personagem, True, PRETO)
        tela.blit(texto, (botao.x + 50, botao.y + 10))
    
    return botoes

# Loop principal
selecionado = -1
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = evento.pos
            botoes = desenhar_menu_personagens(selecionado)
            for i, botao in enumerate(botoes):
                if botao.collidepoint(mouse_pos):
                    selecionado = i
                    print(f"{personagens[selecionado]} selecionado")
    
    botoes = desenhar_menu_personagens(selecionado)
    pygame.display.flip()


personagem_bt = (FONTE_GAME, 1 , (255,255,255))
tela.blit(personagem_bt,(personagem_bt.get_width() - 250 , personagem_bt.get_height() - 540))