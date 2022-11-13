import random
import pygame
import time

pygame.init()

display_width = 400
display_height = 800

jump = pygame.mixer.Sound("C:\\Users\\p.mua\\Desktop\\pygame\\jump2.mp3")

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('dang dang')
clock = pygame.time.Clock()
dangimg = pygame.image.load("C:\\Users\\p.mua\\Desktop\\pygame\\dangwithred.png")
dangimg = pygame.transform.scale(dangimg, (20, 30))
black = (0,0,0)
white = (255,255,255)

largeText = pygame.font.Font('Minecraft.ttf',70)
smallText = pygame.font.Font('Minecraft.ttf',40)
menuText  = pygame.font.Font('Minecraft.ttf',50)

barx = [1,2,3,4,5,6,7,8]
bary = [1,100,200,300,400,500,600,700]
cy = 0
pause = False

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
    largeText = pygame.font.Font('Minecraft.ttf',50)
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
    font = pygame.font.SysFont('Minecraft.ttf', 25)
    text = font.render("Score: "+str(s), True, black)
    gameDisplay.blit(text,(0,0))
    pygame.display.update()

def game_intro():
    pygame.mixer.music.pause()
    pygame.mixer.music.load("C:\\Users\\p.mua\\Desktop\\pygame\\menu.mp3")
    pygame.mixer.music.play(-1)
    intro = True
    ychange = 1
    y = -50

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)

        TextSurf, TextRect = text_objects("Dang", largeText)
        TextRect.center = ((200),(120))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Dang", largeText)
        TextRect.center = ((200),(200))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Adventure", smallText)
        TextRect.center = ((200),(270))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play",150, 250, 325, 425, 200, 400)

        player(190, y)
                
        if y > 720:
            ychange = -3
        else:
            ychange += 0.03

        y = y + ychange

        pygame.display.update()
        clock.tick(60)


def button(msg,x1,x2,y1,y2, posx, posy):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x2 > mouse[0] > x1 and y2 > mouse[1] > y1:
        TextSurf, TextRect = text_objects(msg, menuText)
        TextRect.center = (posx,posy)
        gameDisplay.blit(TextSurf, TextRect)
        if click[0] == 1:
                gameloop()
    else:
        TextSurf, TextRect = text_objects(msg, smallText)
        TextRect.center = (posx,posy)
        gameDisplay.blit(TextSurf, TextRect)

def paused():
    pygame.mixer.music.pause()
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = (200,120)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("continue", menuText)
    TextRect.center = (200,400)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_objects("menu", menuText)
    TextRect.center = (200,500)
    gameDisplay.blit(TextSurf, TextRect)

    pause = True

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 250 > mouse[0] > 150 and 425 > mouse[1] > 325:
            if click[0] == 1:
                pause = False

        elif 250 > mouse[0] > 150 and 525 > mouse[1] > 425:
            if click[0] == 1:
                pause = False
                game_intro()

        pygame.display.update()
        clock.tick(15)  

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
    global pause
    cy = 0
    bary = [1,100,200,300,400,500,600,700]
    for b in range(8):
        xbar = random.randrange(0, 350)
        barx[b] = xbar
    
    pygame.mixer.music.pause()
    pygame.mixer.music.load("C:\\Users\\p.mua\\Desktop\\pygame\\play.mp3")
    pygame.mixer.music.play(-1)

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
                elif event.key == pygame.K_UP and doublejump == True:
                    ychange = -3
                    doublejump = False
                elif event.key == pygame.K_p:
                    paused()
                    pygame.mixer.music.unpause()
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
                    pygame.mixer.Sound.play(jump)

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

game_intro()
gameloop()
pygame.quit()
quit()
