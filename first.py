import random
import pygame
import time
import menu_game

pygame.init()

display_width = 400
display_height = 800

jump = pygame.mixer.Sound("C:\\Users\\p.mua\\Desktop\\pygame\\BGM\\jump2.mp3")

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('dang dang')
clock   = pygame.time.Clock()

dangimg = pygame.image.load("C:\\Users\\p.mua\\Desktop\\pygame\\IMG\\dangwithred.png")
dangimg = pygame.transform.scale(dangimg, (20, 30))
barimg  = pygame.image.load("C:\\Users\\p.mua\\Desktop\\pygame\\IMG\\bar.png")
barimg  = pygame.transform.scale(barimg, (50, 5))

black   = (0,0,0)
white   = (255,255,255)
grey    = (150,150,150)

largeText = pygame.font.Font('Minecraft.ttf',70)
smallText = pygame.font.Font('Minecraft.ttf',40)
menuText  = pygame.font.Font('Minecraft.ttf',50)

barx = [1,2,3,4,5,6,7,8]
bary = [1,100,200,300,400,500,600,700]
cy = 0
pause = False

def player(x,y):
    global cy
    gameDisplay.blit(dangimg, (x,y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def bar():
    for b in range(8):
        gameDisplay.blit(barimg, (barx[b],bary[b]+cy))
#       pygame.draw.line(gameDisplay, 0, (barx[b],bary[b]+cy) , ((barx[b]+50),bary[b]+cy))

def score(count):
    s = int(count)
    font = pygame.font.Font('Minecraft.ttf', 15)
    sc = font.render("Score: "+str(s), True, black)
    gameDisplay.blit(sc,(10,10))
    pygame.display.update()


def crash():
    pygame.mixer.music.pause()
    pygame.mixer.music.load("C:\\Users\\p.mua\\Desktop\\pygame\\BGM\\miss.mp3")
    pygame.mixer.music.play(1)
    over = True

    while over:
        for event in pygame.event.get():
            (event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        TextSurf, TextRect = text_objects("GAME OVER", menuText, black)
        TextRect.center = (200,200)
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 250 > mouse[0] > 150 and 425 > mouse[1] > 325:
            TextSurf, TextRect = text_objects("Play again", smallText, grey)
            TextRect.center = (200,400)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                over = False
                gameloop()
        else:
            TextSurf, TextRect = text_objects("Play again", smallText, black)
            TextRect.center = (200,400)
            gameDisplay.blit(TextSurf, TextRect)


        if 250 > mouse[0] > 150 and 525 > mouse[1] > 425:
            TextSurf, TextRect = text_objects("menu", smallText, grey)
            TextRect.center = (200,500)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                over = False
                game_intro()
        else:
            TextSurf, TextRect = text_objects("menu", smallText, black)
            TextRect.center = (200,500)
            gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(60)
        

def game_intro():
    pygame.mixer.music.pause()
    pygame.mixer.music.load("C:\\Users\\p.mua\\Desktop\\pygame\\BGM\\menu.mp3")
    pygame.mixer.music.play(-1)
    intro = True
    ychange = 1
    y = -50

    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)

        TextSurf, TextRect = text_objects("Dang", largeText, black)
        TextRect.center = (200),(120)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Dang", largeText, black)
        TextRect.center = (200),(200)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Adventure", smallText, black)
        TextRect.center = (200),(270)
        gameDisplay.blit(TextSurf, TextRect)

        #button("Play",150, 250, 325, 425, 200, 400)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 250 > mouse[0] > 150 and 425 > mouse[1] > 325:
            TextSurf, TextRect = text_objects("Play", menuText, black)
            TextRect.center = (200,380)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                    gameloop()
        else:
            TextSurf, TextRect = text_objects("Play", smallText, black)
            TextRect.center = (200,380)
            gameDisplay.blit(TextSurf, TextRect)

        if 250 > mouse[0] > 150 and 525 > mouse[1] > 425:
            TextSurf, TextRect = text_objects("Board", menuText, black)
            TextRect.center = (200,480)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                    pass
        else:
            TextSurf, TextRect = text_objects("Board", smallText, black)
            TextRect.center = (200,480)
            gameDisplay.blit(TextSurf, TextRect)


        player(190, y)
                
        if y > 720:
            ychange = -3
        else:
            ychange += 0.03

        y = y + ychange

        pygame.display.update()
        clock.tick(60)
        
'''
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
'''


def paused():
    pygame.mixer.music.pause()
    TextSurf, TextRect = text_objects("Paused", largeText, black)
    TextRect.center = (200,120)
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
            TextSurf, TextRect = text_objects("continue", smallText, grey)
            TextRect.center = (200,400)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                pause = False

        else:
            TextSurf, TextRect = text_objects("continue", smallText, black)
            TextRect.center = (200,400)
            gameDisplay.blit(TextSurf, TextRect)


        if 250 > mouse[0] > 150 and 525 > mouse[1] > 425:
            TextSurf, TextRect = text_objects("menu", smallText, grey)
            TextRect.center = (200,500)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                pause = False
                game_intro()
        else:
            TextSurf, TextRect = text_objects("menu", smallText, black)
            TextRect.center = (200,500)
            gameDisplay.blit(TextSurf, TextRect)

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
    pygame.mixer.music.load("C:\\Users\\p.mua\\Desktop\\pygame\\BGM\\play.mp3")
    pygame.mixer.music.play(-1)

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xchange = - 2.5
                elif event.key == pygame.K_RIGHT:
                    xchange =  2.5
                elif event.key == pygame.K_UP and doublejump == True:
                    pygame.mixer.Sound.play(jump)
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
                
        ychange += 0.08
        x = x + xchange
        
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
            if x+15 > barx[i] and x <= barx[i]+45 and ychange > 0:
                z += 1
                if y+30 <= bary[i]+4+cy and y+30 >= bary[i]-4+cy:
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
