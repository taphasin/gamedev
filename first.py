import random
import pygame
import time

pygame.init()

display_width = 400
display_height = 700

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('dang dang')
crashed = False
clock = pygame.time.Clock()
dangimg = pygame.image.load("C:\\Users\\p.mua\\Desktop\\pygame\\dang.png")
dangimg = pygame.transform.scale(dangimg, (20, 30))

black = (0,0,0)
white = (255,255,255)
y = (display_height * 0.8)
x = 180
xchange = 0
ychange = 1
barx = [1,2,3,4,5,6,7,8]
doublejump = True
def player(x,y):
    gameDisplay.blit(dangimg, (x,y))

def bar(cx):
    for a in range(7):
        pygame.draw.line(gameDisplay, 0, (barx[a],(a*100)-cx) , ((barx[a]+50),(a*100)-cx))

for b in range(7):
        xbar = random.randrange(0, 350)
        barx[b] = xbar

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -1.3
            elif event.key == pygame.K_RIGHT:
                xchange = 1.3
            elif event.key == pygame.K_DOWN:
                xchange = 0
            elif event.key == pygame.K_UP and doublejump == True:
                ychange = -3
                doublejump = False
                
    x = x + xchange

    ychange += 0.08
    y = y + ychange

    if y > 650:
        ychange = -3
        doublejump = True
    if x > 380:
            xchange = 0
    elif x < 0:
            xchange = 0

    

    gameDisplay.fill(white)
    player(x, y)
    cx = (y - 640)*0.6
    bar(cx)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()