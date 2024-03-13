import pygame,random
from pygame.locals import *


def PosisaoAleatoria():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def colisao(c1,c2):
    return (c1[0] == c2[0])and c1[1] == c2[1]

cima = 0
baixo = 1
direita = 2
esquerda = 3

pygame.init()

tela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Jogo da Cobrinha')

cobra = [(200,200),(210,200),(220,200)]
cobraCor = pygame.Surface((10,10))
cobraCor.fill((255,255,255))

posisaoMaca = PosisaoAleatoria()

maca = pygame.Surface((10,10))
maca.fill((255,0,0))

minhaDirecao = esquerda

clock = pygame.time.Clock()


font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

gameOver = False


while not gameOver : 

    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                minhaDirecao = cima
            if event.key == K_DOWN:
                minhaDirecao = baixo
            if event.key == K_LEFT:
                minhaDirecao = esquerda
            if event.key == K_RIGHT:
                minhaDirecao =direita
            

    if colisao(cobra[0],posisaoMaca):
        posisaoMaca = PosisaoAleatoria()
        cobra.append((0,0))
        score = score + 1

    if cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0:
        gameOver = True
        break
    
    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
                gameOver = True
                break

    if gameOver:
        break


    for i in range(len(cobra) -1,0,-1):
        cobra[i] = (cobra[i-1][0],cobra[i-1][1])
    
    if minhaDirecao == cima:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)

    if minhaDirecao == baixo:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)

    if minhaDirecao == esquerda:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    if minhaDirecao == direita:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])



    tela.fill((0,0,0))
    tela.blit(maca,posisaoMaca)

    for x in range(0, 600, 10): 
        pygame.draw.line(tela, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): 
        pygame.draw.line(tela, (40, 40, 40), (0, y), (600, y))
    
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    tela.blit(score_font, score_rect)

    for pos in cobra:
        tela.blit(cobraCor,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    tela.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
    