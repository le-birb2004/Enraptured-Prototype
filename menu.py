import pygame
import os
pygame.init()

try:
    MainMenu = pygame.display.set_mode((672, 402))
    pygame.display.set_caption("Menu")
    music = pygame.mixer.music.load('Melancholia.mp3')
    pygame.mixer.music.play(-1)

    bg = pygame.image.load('menu.png').convert_alpha()

    start_btn_image = pygame.image.load("play.png").convert_alpha()
    exit_btn_image = pygame.image.load("exit.png").convert_alpha()

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            action = False
            #mouse position
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            MainMenu.blit(self.image, (self.rect.x, self.rect.y))
            return action

    start_btn = Button(30, 300, start_btn_image)
    exit_btn = Button(497, 300, exit_btn_image)

    run = True
    while run:

        if exit_btn.draw() == True:
            pygame.quit()

        if start_btn.draw() == True:
            exec(open('Enraptured.py').read())
            pygame.quit()

        MainMenu.blit(bg, (0,0))

        pygame.display.update()

        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                run = False
           
    pygame.quit()
except:
    pass
