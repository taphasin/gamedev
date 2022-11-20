import pygame

display_width = 400
display_height = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))

black   = (0,0,0)
white   = (255,255,255)

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

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

        TextSurf, TextRect = text_objects("Dang", first.largeText, black)
        TextRect.center = (200),(120)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Dang", first.largeText, black)
        TextRect.center = (200),(200)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Adventure", first.smallText, black)
        TextRect.center = (200),(270)
        gameDisplay.blit(TextSurf, TextRect)

        #button("Play",150, 250, 325, 425, 200, 400)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 250 > mouse[0] > 150 and 425 > mouse[1] > 325:
            TextSurf, TextRect = text_objects("Play", first.menuText, black)
            TextRect.center = (200,380)
            gameDisplay.blit(TextSurf, TextRect)
            if click[0] == 1:
                gameloop()
        else:
            TextSurf, TextRect = text_objects("Play", first.smallText, black)
            TextRect.center = (200,380)
            gameDisplay.blit(TextSurf, TextRect)


        player(190, y)
                
        if y > 720:
            ychange = -3
        else:
            ychange += 0.03

        y = y + ychange

        pygame.display.update()