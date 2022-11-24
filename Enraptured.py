import pygame, sys
import time
import os 

try:
    pygame.init()
    pygame.font.init()

    screenwidth = 672
    screenheight = 402

    text = 0

    ukrossspeed=0
    ukrossnum = 0
    ukrossjump = True

    display_e = 0

    root = pygame.display.set_mode((screenwidth, screenheight))
    pygame.display.set_caption("Enraptured Demo")

    talksound = pygame.mixer.Sound("texttalk.mp3")
    talksound.set_volume(0.25)
    talksound2 = pygame.mixer.Sound("orphtalk.mp3")
    talksound2.set_volume(0.25)

    walkLeft = [pygame.image.load('orph_l1.png'), pygame.image.load('orph_lidle.png'), pygame.image.load('orph_l2.png'), pygame.image.load('orph_lidle.png')]
    walkRight = [pygame.image.load('orph_r1.png'), pygame.image.load('orph_ridle.png'), pygame.image.load('orph_r2.png'), pygame.image.load('orph_ridle.png')]
    walkUp = [pygame.image.load('orph_u1.png'), pygame.image.load('orph_uidle.png'), pygame.image.load('orph_u2.png'), pygame.image.load('orph_uidle.png')]
    walkDown = [pygame.image.load('orph_d1.png'), pygame.image.load('orph_didle.png'), pygame.image.load('orph_d2.png'), pygame.image.load('orph_didle.png')]

    ukross_idleanim = [pygame.image.load('ukross_1_v2.png'), pygame.image.load('ukross_2_v2.png'), pygame.image.load('ukross_3_v2.png'), pygame.image.load('ukross_4_v2.png')]

    charLeft = pygame.image.load('orph_lidle.png')
    charRight = pygame.image.load('orph_ridle.png')
    charUp = pygame.image.load('orph_uidle.png')
    charDown = pygame.image.load('orph_didle.png')

    bg = pygame.image.load('backdrop.png')
    presse = pygame.image.load('presse.png')
    ubox = pygame.image.load('ukrossbox.png')
    obox = pygame.image.load('orphbox.png')
    drawers = pygame.image.load('drawers.png')
    clock = pygame.time.Clock()
    music = pygame.mixer.music.load('omusic.mp3')
    pygame.mixer.music.play(-1)

    class player(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.left = False
            self.right = False
            self.up = False
            self.down = False
            self.walkCount = 0
            self.direction = 1
            self.hitbox = (self.x + 35, self.y+54, 29, 36)

        def draw(self, root):
            if self.walkCount +1 >= 12:
                self.walkCount = 0
                
            if self.left:
                root.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.right:
                root.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.up:
                root.blit(walkUp[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            elif self.down:
                root.blit(walkDown[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                
            else:
                if self.direction == 1:
                    root.blit(charDown,(self.x,self.y))
                elif self.direction == 2:
                    root.blit(charUp,(self.x,self.y))
                elif self.direction == 3:
                    root.blit(charLeft,(self.x,self.y))
                elif self.direction == 4:
                    root.blit(charRight,(self.x,self.y))

    def redraw():
        global ukrossnum
        global ukrossspeed
        global ukrossjump
        global display_e
        root.blit(bg, (0,0))
        root.blit(drawers, (345,102))
        orph.draw(root)
        if orph.x > 270 and orph.y < 110:
                if display_e >= 9:
                    root.blit(presse,(632,360))
                    display_e = display_e + 1
                    if display_e == 18:
                        display_e = 0  
                elif display_e < 9:
                    display_e = display_e+1
        if orph.y > 123 and orph.x >= 445:
                if display_e >= 9:
                    root.blit(presse,(632,360))
                    display_e = display_e + 1
                    if display_e == 18:
                        display_e = 0  
                elif display_e < 9:
                    display_e = display_e+1
        if ukrossspeed == 1:
            if ukrossnum < 3:
                if ukrossjump == True:
                    ukrossnum += 1
            elif ukrossnum == 3:
                ukrossjump = False
            if ukrossjump == False:
                ukrossnum -= 1 
            if ukrossnum == 0:
                ukrossjump = True
            root.blit(ukross_idleanim[ukrossnum], (495,170))
            ukrossspeed = 0
        else:
            ukrossspeed=1
            root.blit(ukross_idleanim[ukrossnum], (495,170))
        pygame.display.update()

    #mainloop
    orph = player(-10, 55, 96, 96)
    game = True
    while game:
        clock.tick(18)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                    

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            orph.vel = 6
        else:
            orph.vel = 4
        
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and orph.x > -7:
            orph.x -= orph.vel
            orph.left = True
            orph.right = False
            orph.down = False
            orph.up = False
            orph.direction = 3
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            orph.left = True
            orph.right = False
            orph.down = False
            orph.up = False

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and orph.x < screenwidth-orph.width and orph.x < 416:
            if orph.x > 275 and orph.y < 100:
                pass
            else:
                orph.x += orph.vel
                orph.left = False
                orph.right = True
                orph.down = False
                orph.up = False
                orph.direction = 4
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and orph.x > 416 and orph.y < 231 and orph.x < 450:
            orph.x += orph.vel
            orph.left = False
            orph.right = True
            orph.down = False
            orph.up = False
            orph.direction = 4
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            orph.left = False
            orph.right = True
            orph.down = False
            orph.up = False

        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and orph.y > 45 and orph.x < 436:
            if orph.x >= 290 and orph.y <= 100:
                pass
            else:
                orph.y -= orph.vel
                orph.left = False
                orph.right = False
                orph.down = False
                orph.up = True
                orph.direction = 2
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and orph.y > 129 and orph.x > 436 and orph.y < 231:
            orph.y -= orph.vel
            orph.left = False
            orph.right = False
            orph.down = False
            orph.up = True
            orph.direction = 2
        elif (keys[pygame.K_UP] or keys[pygame.K_w]):
            orph.left = False
            orph.right = False
            orph.down = False
            orph.up = True

        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and orph.y < 280 and orph.x < 411:
            orph.y += orph.vel
            orph.left = False
            orph.right = False
            orph.down = True
            orph.up = False
            orph.direction = 1
            
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and orph.y < 230 and orph.x > 410:
            orph.y += orph.vel
            orph.left = False
            orph.right = False
            orph.down = True
            orph.up = False
            orph.direction = 1
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            orph.left = False
            orph.right = False
            orph.down = True
            orph.up = False
        else:
            orph.left = False
            orph.right = False
            orph.down = False
            orph.up = False
            orph.walkCount = 0
        redraw()
        if keys[pygame.K_e]:
            if orph.y > 123 and orph.x >= 445:
                text =  text+1
                if text == 1:
                    FONT = pygame.font.Font("yoster.ttf",20)

                    black = (255,255,255)
                    word = "How the hell did you get in here?"

                    previousWidth = 0
                    def getSurfaces(word,pos):
                        global previousWidth

                        surfaces = []
                        positions = []
                        for i in range(len(word)):
                            surf = FONT.render(f"{word[i]}", True, black)
                            surfaces.append(surf)
                        for i in range(len(surfaces)):
                            previousWidth += surfaces[i-1].get_rect().width
                            positions.append([previousWidth + pos[0], pos[1]])
                        return surfaces, positions

                    surfaces, positions = getSurfaces(word, [120,325])

                    start = time.time()
                    count = 0
                    def npc_one_dialogue(delay=0.002):
                        global count
                        global start
                        now = time.time()
                        if count < len(surfaces):
                            if now - start > delay:
                                count +=1
                                start = now
                                pygame.mixer.Sound.play(talksound)
                        for i in range(count):
                                       root.blit(surfaces[i], (positions[i][0], positions[i][1]))
                                       
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()


                        pygame.event.get()
                        
                        npc_one_dialogue()

                        pygame.display.flip()
                        clock.tick(18)
                        root.blit(bg, (0,0))
                        root.blit(drawers, (345,102))
                        orph.draw(root)
                        if ukrossspeed == 1:
                            if ukrossnum < 3:
                                if ukrossjump == True:
                                    ukrossnum += 1
                            elif ukrossnum == 3:
                                ukrossjump = False
                            if ukrossjump == False:
                                ukrossnum -= 1 
                            if ukrossnum == 0:
                                ukrossjump = True
                            root.blit(ukross_idleanim[ukrossnum], (495,170))
                            ukrossspeed = 0
                        else:
                            ukrossspeed=1
                            root.blit(ukross_idleanim[ukrossnum], (495,170))
                        root.blit(ubox, (0,0))
                        pygame.display.update()
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_q]:
                            break
                if orph.y > 123 and orph.x >= 445:
                    text = text+1
                if text == 2:
                    if orph.y > 123 and orph.x >= 445:

                        black = (255,255,255)
                        word = "This is no place for a human to be..."

                        previousWidth = 0
                        def getSurfaces(word,pos):
                            global previousWidth

                            surfaces = []
                            positions = []
                            for i in range(len(word)):
                                surf = FONT.render(f"{word[i]}", True, black)
                                surfaces.append(surf)
                            for i in range(len(surfaces)):
                                previousWidth += surfaces[i-1].get_rect().width
                                positions.append([previousWidth + pos[0], pos[1]])
                            return surfaces, positions

                        surfaces, positions = getSurfaces(word, [120,325])

                        start = time.time()
                        count = 0
                        def npc_one_dialogue(delay=0.002):
                            global count
                            global start
                            global delayspeed
                            now = time.time()
                            if count < len(surfaces):
                                if now - start > delay:
                                    count +=1
                                    start = now
                                    pygame.mixer.Sound.play(talksound)
                            for i in range(count):
                                           root.blit(surfaces[i], (positions[i][0], positions[i][1]))

                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()


                            pygame.event.get()
                            
                            npc_one_dialogue()

                            pygame.display.flip()
                            clock.tick(18)
                            root.blit(bg, (0,0))
                            root.blit(drawers, (345,102))
                            orph.draw(root)
                            if ukrossspeed == 1:
                                if ukrossnum < 3:
                                    if ukrossjump == True:
                                        ukrossnum += 1
                                elif ukrossnum == 3:
                                    ukrossjump = False
                                if ukrossjump == False:
                                    ukrossnum -= 1 
                                if ukrossnum == 0:
                                    ukrossjump = True
                                root.blit(ukross_idleanim[ukrossnum], (495,170))
                                ukrossspeed = 0
                            else:
                                ukrossspeed=1
                                root.blit(ukross_idleanim[ukrossnum], (495,170))
                            root.blit(ubox, (0,0))
                            pygame.display.update()
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_q]:
                                break
                if orph.y > 123 and orph.x >= 445:
                    text = text+1
                    if text == 3:
                        if orph.y > 123 and orph.x >= 445:

                            black = (255,255,255)
                            word = "Bah whatever! You first, them next."

                            previousWidth = 0
                            def getSurfaces(word,pos):
                                global previousWidth

                                surfaces = []
                                positions = []
                                for i in range(len(word)):
                                    surf = FONT.render(f"{word[i]}", True, black)
                                    surfaces.append(surf)
                                for i in range(len(surfaces)):
                                    previousWidth += surfaces[i-1].get_rect().width
                                    positions.append([previousWidth + pos[0], pos[1]])
                                return surfaces, positions

                            surfaces, positions = getSurfaces(word, [120,325])

                            start = time.time()
                            count = 0
                            def npc_one_dialogue(delay=0.002):
                                global count
                                global start
                                global delayspeed
                                now = time.time()
                                if count < len(surfaces):
                                    if now - start > delay:
                                        count +=1
                                        start = now
                                        pygame.mixer.Sound.play(talksound)
                                for i in range(count):
                                               root.blit(surfaces[i], (positions[i][0], positions[i][1]))

                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()


                                pygame.event.get()
                                
                                npc_one_dialogue()

                                pygame.display.flip()
                                clock.tick(18)
                                root.blit(bg, (0,0))
                                root.blit(drawers, (345,102))
                                orph.draw(root)
                                if ukrossspeed == 1:
                                    if ukrossnum < 3:
                                        if ukrossjump == True:
                                            ukrossnum += 1
                                    elif ukrossnum == 3:
                                        ukrossjump = False
                                    if ukrossjump == False:
                                        ukrossnum -= 1 
                                    if ukrossnum == 0:
                                        ukrossjump = True
                                    root.blit(ukross_idleanim[ukrossnum], (495,170))
                                    ukrossspeed = 0
                                else:
                                    ukrossspeed=1
                                    root.blit(ukross_idleanim[ukrossnum], (495,170))
                                root.blit(ubox, (0,0))
                                pygame.display.update()
                                keys = pygame.key.get_pressed()
                                if keys[pygame.K_q]:
                                    pygame.mixer.music.stop()
                                    exec(open('fight.py').read())
                                    pygame.quit()
            elif orph.x > 270 and orph.y < 110:
                FONT = pygame.font.Font("yoster.ttf",20)

                black = (255,255,255)
                word = "It's a set of drawers. Why? Not sure."

                previousWidth = 0
                def getSurfaces(word,pos):
                    global previousWidth

                    surfaces = []
                    positions = []
                    for i in range(len(word)):
                        surf = FONT.render(f"{word[i]}", True, black)
                        surfaces.append(surf)
                    for i in range(len(surfaces)):
                        previousWidth += surfaces[i-1].get_rect().width
                        positions.append([previousWidth + pos[0], pos[1]])
                    return surfaces, positions

                surfaces, positions = getSurfaces(word, [120,325])

                start = time.time()
                count = 0
                def npc_one_dialoguee(delay=0.002):
                    global count
                    global start
                    global delayspeed
                    now = time.time()
                    if count < len(surfaces):
                        if now - start > delay:
                            count +=1
                            start = now
                            pygame.mixer.Sound.play(talksound2)
                    for i in range(count):
                                   root.blit(surfaces[i], (positions[i][0], positions[i][1]))

                while True:
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                    pygame.event.get()
                    
                    npc_one_dialoguee()

                    pygame.display.flip()
                    clock.tick(18)
                    root.blit(bg, (0,0))
                    root.blit(drawers, (345,102))
                    orph.draw(root)
                    if ukrossspeed == 1:
                        if ukrossnum < 3:
                            if ukrossjump == True:
                                ukrossnum += 1
                        elif ukrossnum == 3:
                            ukrossjump = False
                        if ukrossjump == False:
                            ukrossnum -= 1 
                        if ukrossnum == 0:
                            ukrossjump = True
                        root.blit(ukross_idleanim[ukrossnum], (495,170))
                        ukrossspeed = 0
                    else:
                        ukrossspeed=1
                        root.blit(ukross_idleanim[ukrossnum], (495,170))
                    root.blit(obox, (0,0))
                    pygame.display.update()
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_q]:
                        break
        

                

    pygame.quit()                      
except:
    pass
