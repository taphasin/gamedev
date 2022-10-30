import random
import pygame
import time

pygame.init()

display_width = 400
display_height = 750

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('dang dang')
crashed = False
clock = pygame.time.Clock()
dangimg = pygame.image.load("C:\\Users\\p.mua\\Desktop\\pygame\\dang.png")
dangimg = pygame.transform.scale(dangimg, (20, 30))

black = (0,0,0)
white = (255,255,255)
y = 301
x = 180
xchange = 0
ychange = 1
cy = 0
barx = [1,2,3,4,5,6,7,8]
bary = [1,100,200,300,400,500,600,700]
z = 1
a = 0
doublejump = True

for b in range(8):
        xbar = random.randrange(0, 350)
        barx[b] = xbar

def player(x,y):
    gameDisplay.blit(dangimg, (x,y))

def bar(cx):
    for b in range(8):
        pygame.draw.line(gameDisplay, 0, (barx[b],bary[b]+cx) , ((barx[b]+50),bary[b]+cx))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)

def crash():
    message_display('GAME OVER')


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = - 3
            elif event.key == pygame.K_RIGHT:
                xchange =  3
            elif event.key == pygame.K_DOWN:
                xchange = 0
            elif event.key == pygame.K_UP and doublejump == True:
                ychange = -3
                doublejump = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xchange = 0
            
    x = x + xchange    
        
    ychange += 0.08
        
    #ขอบเช็ค    
    if x > 380:
        xchange = 0
    elif x < 0:
        xchange = 0
    if y > 750:
        crash()
        crashed = True
        
    #ychange
    if y <= 300:
        if ychange < 0:
            a -= ychange
            cy = a
        elif ychange > 0:
            y += 0.5
    if y > 300:
        y = y + ychange
        
        
    gameDisplay.fill(white)
    player(x, y)
        
    for i in range(8):
        if y+30 <= bary[i]+4+cy and y+30 >= bary[i]-4+cy:
            z += 1
            if x+15 >= barx[i] and x <= barx[i]+45:
                ychange = -3.5
                doublejump = True


    for rm in range(8):
        if bary[rm]+cy >= 750:
            bary[rm] = 1 - cy
            xbar = random.randrange(0, 350)
            barx[rm] = xbar

    bar(cy)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
