import pygame, os, random


TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO =  pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','pipe.png')) ) 
IMAGEM_CHAO =  pygame.image.load(os.path.join('imgs','base.png'))
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs','bg.png'))
IMAGENS_PASSARO = [
                    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird1.png'))),
                    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird2.png'))),
                    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs','bird3.png')))
                    ]

pygame.font.init()

FONTE_PONTOS = pygame.font.SysFont('arial',50)

class Passaro():
    IMGS = IMAGENS_PASSARO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
    
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2)+ self.velocidade * self.tempo
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > - 90:
                self.altura-= self.VELOCIDADE_ROTACAO
        
    def desenhar(self,tela):
        self.contagem_imagem += 1 
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0
            
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]  #ajuste do passaro ao estar caindo
            self.contagem_imagem = self.TEMPO_ANIMACAO*2
            
        imagem_rotacionada= pygame.transform.rotate(self.imagem,self.angulo) #responsavel pela rotação da imagem do passaro
        posicao_centro_imagem = self.imagem.get_rect(topleft= (self.x, self.y)).center #posição em que o retangulo será posicionado
        retangulo = imagem_rotacionada.get_rect(center=posicao_centro_imagem) #cria a Hitbox do retangulo
        tela.blit(imagem_rotacionada, retangulo.topleft) #resposalvel por desenhar na tela
        
    def get_mask(self):
        return pygame.mask.from_surface(self.imagem) # Cria a mask


class Cano():
    DISTANCIA = 200
    VELOCIADE = 5
    

    def __init__(self,x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True) #flipa a imagem cano na vertical (horizontal = False)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()
    
    def definir_altura(self):
        self.altura = random.randrange(50,450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA 
    
    def mover(self):
        self.x -= self.VELOCIADE

    def desenhar(self,tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))
    
    def colidir(self,passaro):
        passaro_mask =  passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y)) #verificar colisão e os números precisam ser inteiro (pos isso o round, que arrendonda os valores,)
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        base_ponto = passaro_mask.overlap(base_mask, distancia_base)
        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)

        if base_ponto or topo_ponto:
            return True
        else:
            return False

class Chao():
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width() 
    IMAGEM = IMAGEM_CHAO

    def __init__(self,y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA
    
    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA
    
    def desenhar(self,tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))

def desenhar_tela(tela,passaro,canos,chao,pontos):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)
    
    texto = FONTE_PONTOS.render(f'Pontuação: {pontos}', 1, (255,255,255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()

def main():
    passaro = Passaro(230,350)
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()

    # Fazer o jogo rodar
    rodando = True
    while rodando:
        relogio.tick(30)

        # iteração com o usuário
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    passaro.pular()
        
        # Movimentar as coisas
        passaro.mover()
        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            if cano.colidir(passaro):
                del passaro
            if not cano.passou and passaro.x > cano.x:
                cano.passou = True
                adicionar_cano  = True
            cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)
        
        if adicionar_cano:
            pontos += 1
            canos.append(cano(600))
        for canos in remover_canos:
            canos.remove(cano)
        
        if passaro.y + passaro.imagem.get_height() > chao.y or passaro.y  < 0:
            del  passaro

        desenhar_tela(tela, passaro, canos, chao, pontos)

if __name__ == '__main__':
    main()