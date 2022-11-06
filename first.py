import random
import pygame
import time

pygame.init()

display_width = 400
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('dang dang')
clock = pygame.time.Clock()
dangimg = pygame.image.load("C:\\Users\\p.mua\\Desktop\\pygame\\dangwithred.png")
dangimg = pygame.transform.scale(dangimg, (20, 30))
black = (0,0,0)
white = (255,255,255)
barx = [1,2,3,4,5,6,7,8]
bary = [1,100,200,300,400,500,600,700]
cy = 0

def player(x,y):
    gameDisplay.blit(dangimg, (x,y))

def bar():
    global cy
    for b in range(8):
        pygame.draw.line(gameDisplay, 0, (barx[b],bary[b]+cy) , ((barx[b]+50),bary[b]+cy))

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
    gameloop()

def crash():
    message_display('GAME OVER')

def score(count):
    s = int(count)
    font = pygame.font.SysFont(None, 25)
    text = font.render("Distance: "+str(s)+" m", True, black)
    gameDisplay.blit(text,(0,0))
    pygame.display.update()


def gameloop():
    z = 1
    a = 0
    y = 301
    x = 180
    xchange = 0
    ychange = 1
    doublejump = True
    crashed = False
    global cy
    global barx
    global bary
    cy = 0
    bary = [1,100,200,300,400,500,600,700]
    for b in range(8):
        xbar = random.randrange(0, 350)
        barx[b] = xbar

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()
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
            
        #ychange
        if y <= 300:
            if ychange < 0:
                a -= ychange
                cy = a
            elif ychange > 0:
                y += 0.5
        if y > 300:
            y = y + ychange
            
        x = x + xchange    
        ychange += 0.08

        #ขอบเช็ค    
        if x > 380:
            xchange = 0
        elif x < 0:
            xchange = 0
        if y > 800:
            crash()
            
        gameDisplay.fill(white)
        player(x, y)
            
        #เช็คbarhit
        for i in range(8):
            if y+30 <= bary[i]+4+cy and y+30 >= bary[i]-4+cy:
                z += 1
                if x+15 >= barx[i] and x <= barx[i]+45:
                    ychange = -3.5
                    doublejump = True
                    print(i+1)

        #เช็คbarout of frame
        for rm in range(8):
            if bary[rm]+cy >= 800:
                bary[rm] = 1 - cy
                xbar = random.randrange(0, 350)
                barx[rm] = xbar

        bar()
        score(cy)
        pygame.display.update()
        clock.tick(60)

gameloop()
pygame.quit()
quit()
