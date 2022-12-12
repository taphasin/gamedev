import random
import pygame
import time
import json
import datain

pygame.init()

display_width = 400
display_height = 800

jump = pygame.mixer.Sound("C:\\Users\\p.mua\\Desktop\\pygame\\BGM\\jump2.mp3")
coin = pygame.mixer.Sound("C:\\Users\\p.mua\\Desktop\\pygame\\BGM\\coin.wav")

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('dang dang')
clock   = pygame.time.Clock()

dangimg  = pygame.image.load("C:\\Users\\p.mua\\Desktop\\pygame\\IMG\\dangwithred.png")
dangimg  = pygame.transform.scale(dangimg, (20, 30))
barimg   = pygame.image.load("C:\\Users\\p.mua\\Desktop\\pygame\\IMG\\bar.png")
barimg   = pygame.transform.scale(barimg, (50, 5))
spikeimg = pygame.image.load("C:\\Users\\p.mua\\Desktop\\pygame\\IMG\\spike.png")
spikeimg = pygame.transform.scale(spikeimg, (21, 21))
starimg  = pygame.image.load("C:\\Users\\p.mua\\Desktop\\pygame\\IMG\\star.png")
starimg  = pygame.transform.scale(starimg, (20, 20))

black   = (0,0,0)
white   = (255,255,255)
grey    = (150,150,150)

largeText = pygame.font.Font('C:\\Users\\p.mua\\Desktop\\pygame\\font\\Minecraft.ttf',70)
menuText  = pygame.font.Font('C:\\Users\\p.mua\\Desktop\\pygame\\font\\Minecraft.ttf',50)
smallText = pygame.font.Font('C:\\Users\\p.mua\\Desktop\\pygame\\font\\Minecraft.ttf',40)
thinText  = pygame.font.Font('C:\\Users\\p.mua\\Desktop\\pygame\\font\\Minecraft.ttf',30)

barx = [1,2,3,4,5,6,7,8]
cy = 0


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def player(x,y):
    gameDisplay.blit(dangimg, (x,y))

def bar():
    for b in range(8):
        gameDisplay.blit(barimg, (barx[b],bary[b]+cy))


def spike(playx, y, x):
    diff = cy / 1000
    y+=diff
    if y+cy > 800:
        y = - cy
        x = playx
    gameDisplay.blit(spikeimg, (x,y+cy))

    return y, x

def star(x, y):
    gameDisplay.blit(starimg, (x,y+cy))
    

def score(count, bonus):
    s = int(count) + bonus
    font = pygame.font.Font('C:\\Users\\p.mua\\Desktop\\pygame\\font\\Minecraft.ttf', 15)
    sc = font.render("Score: "+str(s), True, black)
    gameDisplay.blit(sc,(10,10))
    pygame.display.update()

def board():

    gameDisplay.fill(white)

    with open('scoredata.txt') as datafile:
        data = json.load(datafile) 

    TextSurf, TextRect = text_objects("TOP 5", smallText, black)
    TextRect.center = (200,100)
    gameDisplay.blit(TextSurf, TextRect) 
    

    first = thinText.render("1. " + data["1"]["name"], True, black)
    gameDisplay.blit(first,(50,200))
    TextSurf, TextRect = text_objects(str(data["1"]["score"]), thinText, black)
    TextRect.center = (300,210)
    gameDisplay.blit(TextSurf, TextRect) 

    secon = thinText.render("2. " + data["2"]["name"], True, black)
    gameDisplay.blit(secon,(50,300))
    TextSurf, TextRect = text_objects(str(data["2"]["score"]), thinText, black)
    TextRect.center = (300,310)
    gameDisplay.blit(TextSurf, TextRect)

    thirt = thinText.render("3. " + data["3"]["name"], True, black)
    gameDisplay.blit(thirt,(50,400)) 
    TextSurf, TextRect = text_objects(str(data["3"]["score"]), thinText, black)
    TextRect.center = (300,410)
    gameDisplay.blit(TextSurf, TextRect)

    four = thinText.render("4. " + data["4"]["name"], True, black)
    gameDisplay.blit(four,(50,500))
    TextSurf, TextRect = text_objects(str(data["4"]["score"]), thinText, black)
    TextRect.center = (300,510)
    gameDisplay.blit(TextSurf, TextRect)

    five = thinText.render("5. " + data["5"]["name"], True, black)
    gameDisplay.blit(five,(50,600))
    TextSurf, TextRect = text_objects(str(data["5"]["score"]), thinText, black)
    TextRect.center = (300,610)
    gameDisplay.blit(TextSurf, TextRect)


    pygame.display.update()

    while True:
        for event in pygame.event.get():
            (event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_intro()

def crash():
    pygame.mixer.music.pause()
    pygame.mixer.music.load("C:\\Users\\p.mua\\Desktop\\pygame\\BGM\\miss.mp3")
    pygame.mixer.music.play(1)
    point = int(cy)

    datain.storedata(input, point)

    while True:
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
                gameloop()
        else:
            TextSurf, TextRect = text_objects("Play again", smallText, black)
            TextRect.center = (200,400)
            gameDisplay.blit(TextSurf, TextRect)


        if 250 > mouse[0] > 150 and 625 > mouse[1] > 525:
            TextSurf, TextRect = text_objects("menu", smallText, grey)
            TextRect.center = (200,600)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                game_intro()
        else:
            TextSurf, TextRect = text_objects("menu", smallText, black)
            TextRect.center = (200,600)
            gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(60)
        

def game_intro():
    pygame.mixer.music.pause()
    pygame.mixer.music.load("C:\\Users\\p.mua\\Desktop\\pygame\\BGM\\menu.mp3")
    pygame.mixer.music.play(-1)
    ychange = 1
    y = -50
    global input
    input = "null"

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input = input[:-1]
                elif len(input) < 8:
                    input += event.unicode
                
        gameDisplay.fill(white)

        font = pygame.font.Font('C:\\Users\\p.mua\\Desktop\\pygame\\font\\Minecraft.ttf', 15)
        credit = font.render("65010710 phasin muangmaiprae", True, black)
        gameDisplay.blit(credit,(80,10))

        TextSurf, TextRect = text_objects("Name:", smallText, black)
        TextRect.center = (200),(550)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(input, thinText, black)
        TextRect.center = (200),(600)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Dang", largeText, black)
        TextRect.center = (200),(100)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Dang", largeText, black)
        TextRect.center = (200),(180)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Adventure", smallText, black)
        TextRect.center = (200),(250)
        gameDisplay.blit(TextSurf, TextRect)


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 250 > mouse[0] > 150 and 425 > mouse[1] > 325:
            TextSurf, TextRect = text_objects("Play", menuText, black)
            TextRect.center = (200,360)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                    gameloop()
        else:
            TextSurf, TextRect = text_objects("Play", smallText, black)
            TextRect.center = (200,360)
            gameDisplay.blit(TextSurf, TextRect)
        if 250 > mouse[0] > 150 and 525 > mouse[1] > 425:
            TextSurf, TextRect = text_objects("Board", menuText, black)
            TextRect.center = (200,460)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                    board()
        else:
            TextSurf, TextRect = text_objects("Board", smallText, black)
            TextRect.center = (200,460)
            gameDisplay.blit(TextSurf, TextRect)

        player(190, y)
                
        if y > 720:
            ychange = -2
        else:
            ychange += 0.03

        y = y + ychange

        pygame.display.update()
        clock.tick(60)


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


        if 250 > mouse[0] > 150 and 625 > mouse[1] > 525:
            TextSurf, TextRect = text_objects("menu", smallText, grey)
            TextRect.center = (200,600)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                pause = False
                game_intro()
        else:
            TextSurf, TextRect = text_objects("menu", smallText, black)
            TextRect.center = (200,600)
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
    spiy = -50
    spix = 200
    starx = random.randrange(50, 350)
    stary = -200
    global cy
    cy = 0
    global bary
    bary = [1,100,200,300,400,500,600,700]
    bonus = 0

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
                bary[rm] = - cy
                xbar = random.randrange(0, 350)
                barx[rm] = xbar

        #spike
        if x > spix-25 and x <= spix+25:
            if y > spiy-25+cy and y <= spiy+25+cy:
                spiy = 0
                crash()

        #starhit
        if x > starx-20 and x <= starx+20:
            if y > stary-20+cy and y <= stary+20+cy:
                pygame.mixer.Sound.play(coin)
                bonus += 100
                starx = random.randrange(0, 350)
                stary = - cy - 50

        if stary+cy > 800:
            starx = random.randrange(0, 350)
            stary = - cy


        spiy, spix = spike(x, spiy, spix)
        star(starx, stary)
        bar()
        score(cy, bonus)
        pygame.display.update()
        clock.tick(60)

game_intro()
pygame.quit()
quit()
