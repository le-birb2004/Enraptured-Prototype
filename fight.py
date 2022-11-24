import pygame, sys
import time
import os
import random
pygame.init()
pygame.font.init()

try:
        fightmenu = pygame.display.set_mode((672, 402))
        pygame.display.set_caption("Enraptured Fight Demo")
        clock = pygame.time.Clock()

        talksound = pygame.mixer.Sound("texttalk.mp3")
        talksound2 = pygame.mixer.Sound("orphtalk.mp3")
        talksound.set_volume(0.25)
        talksound2.set_volume(0.25)

        geq = pygame.mixer.Sound("gequip.mp3")
        hit = pygame.mixer.Sound("hit.wav")
        heal = pygame.mixer.Sound("heal.wav")
        death = pygame.mixer.Sound("death.wav")
        click = pygame.mixer.Sound("click.wav")
        fhit = pygame.mixer.Sound("finalhit.wav")
        bchord = pygame.mixer.Sound("brokenchord.wav")

        ohp = 250
        uhp = 250
        green = (0,255,0)
        white = (255,255,255)
        yellow = (255,255,0)
        black = (0,0,0)
        omod = 1
        guitarhp = 202
        previousWidth = 0
        count = 0
        ucount = 0
        start = 0
        compNum = 0

        transition = 0
        bcanim = 0
        ganim = 0
        gsanim = 0
        udieanim = 0
        odieanim = 0

        i1 = True
        i2 = True
        i3 = True
        i4 = True

        compResp1 = False
        compResp2 = False
        compResp3 = False
        compResp4 = False
        compResp5 = False

        bg = pygame.image.load('fightbg.png')
        dbg1 = pygame.image.load('deathbg1.png')
        dbg2 = pygame.image.load('deathbg2.png')

        overwrite = pygame.image.load('overwrite.png')

        wfg1 = pygame.image.load('winfg1.png')
        wfg2 = pygame.image.load('winfg2.png')

        orphf = pygame.image.load('orph_f1.png')
        orphf2 = pygame.image.load('orph_f2.png')
        ukrossf = pygame.image.load('ukross_f1.png')
        fbox = pygame.image.load('fightbox.png')
        ohpbar = pygame.image.load('ohpbar.png')
        uhpbar = pygame.image.load('uhpbar.png')
        orphbox = pygame.image.load('orphbox2.png')
        orphbox2 = pygame.image.load('orphbox3.png')
        ububble = pygame.image.load('speechbubble.png')
        winbox = pygame.image.load('winbox.png')

        odead1 = pygame.image.load('orphdead1.png')
        odead2 = pygame.image.load('orphdead2.png')
        odead3 = pygame.image.load('orphdead3.png')
        odead4 = pygame.image.load('orphdead4.png')

        udead1 = pygame.image.load('ukrossdead1.png')
        udead2 = pygame.image.load('ukrossdead2.png')

        fbtn = pygame.image.load('fight.png')
        ibtn = pygame.image.load('item.png')
        abtn = pygame.image.load('action.png')
        ebtn = pygame.image.load("exit.png")

        fbtn1 = pygame.image.load('fbtn1.png')
        fbtn2 = pygame.image.load('fbtn2.png')
        fbtn3 = pygame.image.load('fbtn3.png')
        fbtn4 = pygame.image.load('fbtn4.png')

        ibtn1 = pygame.image.load('ibtn1.png')
        ibtn2 = pygame.image.load('ibtn2.png')
        ibtn3 = pygame.image.load('ibtn3.png')

        abtn1 = pygame.image.load('abtn1.png')
        abtn2 = pygame.image.load('abtn2.png')
        abtn3 = pygame.image.load('abtn3.png')
        abtn4 = pygame.image.load('abtn4.png')

        bc1 = pygame.image.load('bc1.png')
        bc2 = pygame.image.load('bc2.png')
        bc3 = pygame.image.load('bc3.png')
        bc4 = pygame.image.load('bc4.png')
        bc5 = pygame.image.load('bc5.png')
        bc6 = pygame.image.load('bc6.png')
        bc7 = pygame.image.load('bc7.png')
        bc8 = pygame.image.load('bc8.png')

        gs1 = pygame.image.load('gs1.png')
        gs2 = pygame.image.load('gs2.png')
        gs3 = pygame.image.load('gs3.png')

        b1 = pygame.image.load('borgir1.png')
        b2 = pygame.image.load('borgir2.png')
        b3 = pygame.image.load('borgir3.png')
        b4 = pygame.image.load('borgir4.png')
        b5 = pygame.image.load('borgir5.png')

        c1 = pygame.image.load('cuppa1.png')
        c2 = pygame.image.load('cuppa2.png')

        pb1 = pygame.image.load('pborgir1.png')
        pb2 = pygame.image.load('pborgir2.png')
        pb3 = pygame.image.load('pborgir3.png')
        pb4 = pygame.image.load('pborgir4.png')
        pb5 = pygame.image.load('pborgir5.png')

        pc1 = pygame.image.load('pcuppa1.png')
        pc2 = pygame.image.load('pcuppa2.png')

        t1 = pygame.image.load('tune1.png')
        t2 = pygame.image.load('tune2.png')

        p1 = pygame.image.load('punch1.png')
        p2 = pygame.image.load('punch2.png')
        p3 = pygame.image.load('punch3.png')

        k1 = pygame.image.load('kick1.png')
        k2 = pygame.image.load('kick2.png')
        k3 = pygame.image.load('kick3.png')

        s1 = pygame.image.load('squish1.png')
        s2 = pygame.image.load('squish2.png')
        s3 = pygame.image.load('squish3.png')
        s4 = pygame.image.load('squish4.png')

        uh1 = pygame.image.load('uheal1.png')
        uh2 = pygame.image.load('uheal2.png')

        ub1 = pygame.image.load('bounce2.png')
        ub2 = pygame.image.load('bounce3.png')
        row = pygame.image.load('roverwrite.png')
        rw = pygame.image.load('Rwave.png')
        lw = pygame.image.load('Lwave.png')
        
        music = pygame.mixer.music.load('fmusic.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        class Button():
                def __init__(self, x, y, image):
                    self.image = image
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (x, y)
                    self.clicked = False

                def draw(self):
                    action = False
                    pos = pygame.mouse.get_pos()

                    if self.rect.collidepoint(pos):
                        for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    self.clicked = True
                                    action = True

                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

                    fightmenu.blit(self.image, (self.rect.x, self.rect.y))

                    return action

        def odie():
            global odieanim
            die = True
            pygame.mixer.Sound.play(fhit)
            pygame.mixer.music.stop()
            while die:
                clock.tick(60)
                if odieanim < 90:
                    odieanim = odieanim+1
                    fightmenu.blit(bg,(0,0))
                    if guitarhp > 0:
                        fightmenu.blit(orphf,(100,60))
                    elif guitarhp <= 0:
                         fightmenu.blit(orphf2,(100,60))
                    fightmenu.blit(ukrossf,(440,8))
                    fightmenu.blit(orphbox2,(0,261))        
                    fightmenu.blit(uhpbar,(387,25))
                    fightmenu.blit(ohpbar,(23,25))
                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))
                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                    if odieanim == 0:
                        pygame.mixer.Sound.play(fhit)

                elif odieanim >= 90 and odieanim < 180:
                    odieanim = odieanim+1
                    fightmenu.blit(bg,(0,0))
                    if guitarhp > 0:
                        fightmenu.blit(orphf,(100,60))
                    elif guitarhp <= 0:
                         fightmenu.blit(orphf2,(100,60))
                    fightmenu.blit(ukrossf,(440,8))
                    fightmenu.blit(orphbox2,(0,261))
                    if odieanim == 91:
                        pygame.mixer.Sound.play(hit)

                elif odieanim >= 180 and odieanim < 270:
                    odieanim = odieanim+1
                    fightmenu.blit(dbg1,(0,0))
                    if guitarhp > 0:
                        fightmenu.blit(odead1,(100,60))
                    elif guitarhp <= 0:
                         fightmenu.blit(odead3,(100,60))
                    fightmenu.blit(orphbox2,(0,261))
                    if odieanim == 181:
                        pygame.mixer.Sound.play(hit)

                elif odieanim >= 270 and odieanim < 375:
                    odieanim = odieanim+1
                    fightmenu.blit(dbg1,(0,0))
                    if guitarhp > 0:
                        fightmenu.blit(odead2,(100,60))
                    elif guitarhp <= 0:
                         fightmenu.blit(odead4,(100,60))
                    if odieanim == 271:
                        pygame.mixer.Sound.play(fhit)
                elif odieanim >= 375:
                    odieanim = odieanim+1
                    fightmenu.blit(dbg2,(0,0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                pygame.display.update()
                

        def udie():
            global udieanim
            count = 0
            pygame.mixer.music.stop()
            FONT = pygame.font.Font("yoster.ttf",14)
            die = True
            while die:
                clock.tick(60)

                fightmenu.blit(bg,(0,0))
                if guitarhp > 0:
                    fightmenu.blit(orphf,(100,60))
                elif guitarhp <= 0:
                    fightmenu.blit(orphf2,(100,60))
                fightmenu.blit(orphbox2,(0,261))        
                if udieanim > 0 and udieanim < 19:
                    udieanim = udieanim+1
                if udieanim < 20:
                    fightmenu.blit(ukrossf,(440,8))
                    udieanim = udieanim+1
                elif udieanim < 40 and udieanim >= 20:
                    fightmenu.blit(udead1,(440,8))
                    udieanim = udieanim+1
                elif udieanim == 40:
                    fightmenu.blit(udead1,(440,8))
                    fightmenu.blit(ububble,(225,120))

                    text = "A h-human k-kills me?"
                    count = 0
                    previousWidth = 0
                    def getSurfaces(text,pos):
                        global previousWidth
                        surfaces = []
                        positions = []
                        previousWidth = 0
                        for i in range(len(text)):
                            surf = FONT.render(f"{text[i]}", True, black)
                            surfaces.append(surf)
                        for i in range(len(surfaces)):
                            previousWidth += surfaces[i-1].get_rect().width
                            positions.append([previousWidth + pos[0], pos[1]])
                        return surfaces, positions

                    surfaces, positions = getSurfaces(text, [226,126])

                    start = time.time()
                    def npc_one_dialogue(delay=0.4):
                        global ucount
                        global start
                        now = time.time()
                        if ucount < len(surfaces):
                            if now - start > delay:
                                ucount +=1
                                start = now
                                pygame.mixer.Sound.play(talksound)
                        for i in range(ucount):
                            fightmenu.blit(surfaces[i], (positions[i][0], positions[i][1]))

                    anim = True
                    while anim:
                        npc_one_dialogue()
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                    anim = False
                                    udieanim = 2004
                                    pygame.mixer.Sound.play(death)
                    
                else:

                    fightmenu.blit(bg,(0,0))
                    if guitarhp > 0:
                         fightmenu.blit(orphf,(100,60))
                    elif guitarhp <= 0:
                        fightmenu.blit(orphf2,(100,60))
                    fightmenu.blit(winbox,(0,261))
                    
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                pygame.display.update()

        def forgive():
            forgiven = True
            pygame.mixer.music.stop()
            while forgiven:
                global transition
                clock.tick(60)
                if transition <= 20:
                    fightmenu.blit(wfg1,(0,0))
                elif transition > 20:
                    fightmenu.blit(wfg2,(0,0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                pygame.display.update()

        def uturn():
            global uhp,ohp
            uact = random.randint(1,5)
            if uact == 1 or uact == 2:
                    banim = 0
                    anim = True
                    while anim:
                        clock.tick(60)
                        banim = banim+1
                        fightmenu.blit(fbox,(0,261))
                        if banim < 10:
                            fightmenu.blit(row,(0,0))
                            fightmenu.blit(s1,(440,8))
                            fightmenu.blit(uhpbar,(387,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            fightmenu.blit(fbox,(0,261))
                        elif banim >= 10 and banim < 20:
                            fightmenu.blit(overwrite,(440,8))
                            fightmenu.blit(ub1,(440,-18))
                            fightmenu.blit(uhpbar,(387,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            fightmenu.blit(fbox,(0,261))
                        elif banim >= 20 and banim < 30:
                            fightmenu.blit(row,(0,0))
                            fightmenu.blit(ub2,(440,-28))
                            fightmenu.blit(uhpbar,(387,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            fightmenu.blit(fbox,(0,261))
                        elif banim >= 30 and banim < 40:
                            fightmenu.blit(overwrite,(440,8))
                            fightmenu.blit(ub1,(440,-18))
                            fightmenu.blit(uhpbar,(387,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            fightmenu.blit(fbox,(0,261))
                        elif banim >= 40 and banim < 50:
                            if banim == 41:
                                pygame.mixer.Sound.play(hit)
                            fightmenu.blit(row,(0,0))
                            fightmenu.blit(s1,(440,8))
                            fightmenu.blit(uhpbar,(387,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            fightmenu.blit(fbox,(0,261))
                            fightmenu.blit(lw,(380,170))
                            fightmenu.blit(rw,(540,170))
                        elif banim >= 50 and banim < 60:
                            fightmenu.blit(bg,(0,0))
                            fightmenu.blit(ukrossf,(440,8))
                            if guitarhp > 0:
                                fightmenu.blit(orphf,(100,60))
                            elif guitarhp <= 0:
                                fightmenu.blit(orphf2,(100,60))  
                            fightmenu.blit(fbox,(0,261))
                            fightmenu.blit(uhpbar,(387,25))
                            fightmenu.blit(ohpbar,(23,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                            fightmenu.blit(lw,(330,170))
                            fightmenu.blit(rw,(590,170))
                        elif banim >= 60 and banim < 70:
                            fightmenu.blit(bg,(0,0))
                            fightmenu.blit(ukrossf,(440,8))
                            if guitarhp > 0:
                                fightmenu.blit(orphf,(100,60))
                            elif guitarhp <= 0:
                                fightmenu.blit(orphf2,(100,60))  
                            fightmenu.blit(fbox,(0,261))
                            fightmenu.blit(uhpbar,(387,25))
                            fightmenu.blit(ohpbar,(23,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                            fightmenu.blit(lw,(280,170))
                            fightmenu.blit(rw,(640,170))
                        elif banim >= 70 and banim < 80:
                            fightmenu.blit(bg,(0,0))
                            fightmenu.blit(ukrossf,(440,8))
                            if guitarhp > 0:
                                fightmenu.blit(orphf,(100,60))
                            elif guitarhp <= 0:
                                fightmenu.blit(orphf2,(100,60))  
                            fightmenu.blit(fbox,(0,261))
                            fightmenu.blit(uhpbar,(387,25))
                            fightmenu.blit(ohpbar,(23,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                            fightmenu.blit(lw,(230,170))
                            fightmenu.blit(rw,(690,170))
                        elif banim >= 80 and banim < 90:
                            fightmenu.blit(bg,(0,0))
                            fightmenu.blit(ukrossf,(440,8))
                            if guitarhp > 0:
                                fightmenu.blit(orphf,(100,60))
                            elif guitarhp <= 0:
                                fightmenu.blit(orphf2,(100,60))  
                            fightmenu.blit(fbox,(0,261))
                            fightmenu.blit(uhpbar,(387,25))
                            fightmenu.blit(ohpbar,(23,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                            fightmenu.blit(lw,(180,170))
                            fightmenu.blit(rw,(740,170))
                        elif banim >= 90 and banim < 100:
                            fightmenu.blit(bg,(0,0))
                            fightmenu.blit(ukrossf,(440,8))
                            if guitarhp > 0:
                                fightmenu.blit(orphf,(100,60))
                            elif guitarhp <= 0:
                                fightmenu.blit(orphf2,(100,60))  
                            fightmenu.blit(fbox,(0,261))
                            fightmenu.blit(uhpbar,(387,25))
                            fightmenu.blit(ohpbar,(23,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                            fightmenu.blit(lw,(130,170))
                            fightmenu.blit(rw,(790,170))
                        elif banim >= 100 and banim < 110:
                            fightmenu.blit(bg,(0,0))
                            fightmenu.blit(ukrossf,(440,8))
                            if guitarhp > 0:
                                fightmenu.blit(orphf,(100,60))
                            elif guitarhp <= 0:
                                fightmenu.blit(orphf2,(100,60))  
                            fightmenu.blit(fbox,(0,261))
                            fightmenu.blit(uhpbar,(387,25))
                            fightmenu.blit(ohpbar,(23,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                            fightmenu.blit(lw,(100,170))
                            if banim == 102:
                                pygame.mixer.Sound.play(hit)
                        elif banim == 120:
                            anim = False
                        pygame.display.update()
                    ohp = ohp-(random.randint(26,32))
            elif uact == 3 or uact == 4:
                    sanim = 0
                    anim = True
                    while anim:
                        clock.tick(60)
                        sanim = sanim+1
                        fightmenu.blit(fbox,(0,261))
                        if sanim < 10:
                            fightmenu.blit(bg,(0,0))
                            if guitarhp > 0:
                                fightmenu.blit(orphf,(100,60))
                            elif guitarhp <= 0:
                                 fightmenu.blit(orphf2,(100,60))
                            fightmenu.blit(s1,(440,8))
                            fightmenu.blit(fbox,(0,261))        
                            fightmenu.blit(uhpbar,(387,25))
                            fightmenu.blit(ohpbar,(23,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                        elif sanim >= 10 and sanim < 20:
                            fightmenu.blit(bg,(0,0))
                            if guitarhp > 0:
                                fightmenu.blit(orphf,(100,60))
                            elif guitarhp <= 0:
                                 fightmenu.blit(orphf2,(100,60))
                            fightmenu.blit(s2,(345,-80))
                            fightmenu.blit(fbox,(0,261))        
                            fightmenu.blit(uhpbar,(387,25))
                            fightmenu.blit(ohpbar,(23,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                        elif sanim >= 20 and sanim < 30:
                            fightmenu.blit(bg,(0,0))
                            if guitarhp > 0:
                                fightmenu.blit(orphf,(100,60))
                            elif guitarhp <= 0:
                                 fightmenu.blit(orphf2,(100,60))
                            fightmenu.blit(s3,(190,-50))
                            fightmenu.blit(fbox,(0,261))        
                            fightmenu.blit(uhpbar,(387,25))
                            fightmenu.blit(ohpbar,(23,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                        elif sanim >= 30 and sanim < 40:
                            fightmenu.blit(bg,(0,0))
                            if sanim == 32:
                                pygame.mixer.Sound.play(hit)
                            fightmenu.blit(s4,(28,30))
                            fightmenu.blit(fbox,(0,261))        
                            fightmenu.blit(uhpbar,(387,25))
                            fightmenu.blit(ohpbar,(23,25))
                            pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                            pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                            pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                        elif sanim >= 70:
                            anim = False
                        pygame.display.update()
                    ohp = ohp-(random.randint(34,42))
            elif uact == 5:
                    if uhp <= 100:
                            hanim = 0
                            anim = True
                            while anim:
                                clock.tick(60)
                                hanim = hanim+1
                                fightmenu.blit(fbox,(0,261))
                                if hanim < 10:
                                    fightmenu.blit(overwrite,(440,8))
                                    fightmenu.blit(uh1,(440,8))
                                    fightmenu.blit(uhpbar,(387,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                elif hanim >= 10 and hanim < 20:
                                    if hanim == 12:
                                        pygame.mixer.Sound.play(heal)
                                    fightmenu.blit(overwrite,(440,8))
                                    fightmenu.blit(uh2,(440,8))
                                    fightmenu.blit(uhpbar,(387,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                elif hanim >= 20 and hanim < 30:
                                    fightmenu.blit(overwrite,(440,8))
                                    fightmenu.blit(uh1,(440,8))
                                    fightmenu.blit(uhpbar,(387,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                elif hanim >= 40:
                                    anim = False
                                pygame.display.update()
                            uhp = uhp+(random.randint(20,40))
                            
                    else:
                            uturn()
            if ohp <= 0:
                    odie()
            else:
                    oturn()

        def utext():
                global compResp1,compResp2,compResp3,compResp4,compResp5,count
                if uhp <= 0:
                        udie()
                count = 0
                FONT = pygame.font.Font("yoster.ttf",14)

                if compResp1 == True:
                    compResp1 = False
                    count = 0
                    text = "My name is Ukross."

                elif compResp2 == True:
                    compResp2 = False
                    count = 0
                    text = "That's 'cause it is."

                elif compResp3 == True:
                    compResp3 = False
                    count = 0
                    text = "I- Uh... Thanks."

                elif compResp4 == True:
                    compResp4 = False
                    count = 0
                    text = "Finally appreciated!"

                elif compResp5 == True:
                    compResp5 = False
                    count = 0
                    text = "You aren't so bad."
                
                else:
                    rantext = random.randint(1,7)
                    if rantext == 1:
                        text = "Gah! So much to do."
                        count = 0
                    elif rantext == 2:
                        text = "Ugh, just die please."
                        count = 0
                    elif rantext == 3:
                        text = "Polite-fully perish."
                        count = 0
                    elif rantext == 4:
                        text = "Bugger off, yeah?"
                        count = 0
                    elif rantext == 5:
                        text = "Nothing personal kid."
                        count = 0
                    elif rantext == 6:
                        text = "How aren't you dead?"
                        count = 0
                    elif rantext == 7:
                        text = "Kick the bucket. Now."
                        count = 0

                count = 0
                previousWidth = 0
                def getSurfaces(text,pos):
                    global previousWidth
                    surfaces = []
                    positions = []
                    previousWidth = 0
                    for i in range(len(text)):
                        surf = FONT.render(f"{text[i]}", True, black)
                        surfaces.append(surf)
                    for i in range(len(surfaces)):
                        previousWidth += surfaces[i-1].get_rect().width
                        positions.append([previousWidth + pos[0], pos[1]])
                    return surfaces, positions

                surfaces, positions = getSurfaces(text, [226,126])

                start = time.time()
                count = 0
                def npc_one_dialogue(delay=0.07):
                    global count
                    global start
                    now = time.time()
                    if count < len(surfaces):
                        if now - start > delay:
                            count +=1
                            start = now
                            pygame.mixer.Sound.play(talksound)
                    for i in range(count):
                            fightmenu.blit(surfaces[i], (positions[i][0], positions[i][1]))

                while True:
                    pygame.event.get()
                    fightmenu.blit(bg,(0,0))
                    if guitarhp > 0:
                            fightmenu.blit(orphf,(100,60))
                    elif guitarhp <= 0:
                            fightmenu.blit(orphf2,(100,60))
                    fightmenu.blit(ukrossf,(440,8))
                    fightmenu.blit(orphbox2,(0,261))        
                    fightmenu.blit(uhpbar,(387,25))
                    fightmenu.blit(ohpbar,(23,25))
                    fightmenu.blit(ububble,(225,120))
                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))

                    npc_one_dialogue()

                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                uturn()
                
                uturn()

        def fmenu():
            pygame.mixer.Sound.play(click)
            global uhp,ohp,omod,guitarhp,bcanim
            fopt = True
            while fopt:
              
                fightmenu.blit(bg,(0,0))
                if guitarhp > 0:
                        fightmenu.blit(orphf,(100,60))
                elif guitarhp <= 0:
                        fightmenu.blit(orphf2,(100,60))
                fightmenu.blit(ukrossf,(440,8))
                fightmenu.blit(fbox,(0,261))
                if guitarhp > 0:
                    fight_btn1 = Button(30, 300, fbtn1)
                    fight_btn2 = Button(264, 300, fbtn2)
                elif guitarhp <= 0:
                    fight_btn3 = Button(30, 300, fbtn3)
                    fight_btn4 = Button(264, 300, fbtn4)
                exit_btn = Button(497, 300, ebtn)
                fightmenu.blit(uhpbar,(387,25))
                fightmenu.blit(ohpbar,(23,25))
                pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))

                if guitarhp > 0:
                        if fight_btn1.draw() == True:
                            pygame.mixer.Sound.play(click)
                            bcanim = 0
                            anim = True
                            while anim:
                                clock.tick(60)
                                bcanim = bcanim+1
                                fightmenu.blit(fbox,(0,261))
                                if bcanim < 15:
                                    fightmenu.blit(overwrite,(100,60))
                                    fightmenu.blit(bc1,(100,60))
                                elif bcanim >= 15 and bcanim < 30:
                                    fightmenu.blit(overwrite,(100,60))
                                    fightmenu.blit(bc2,(100,60))
                                elif bcanim >= 30 and bcanim < 45:
                                    fightmenu.blit(overwrite,(100,60))
                                    fightmenu.blit(bc1,(100,60))
                                    if bcanim == 32:
                                        pygame.mixer.Sound.play(bchord)
                                elif bcanim >= 45 and bcanim < 60:
                                    fightmenu.blit(overwrite,(100,60))
                                    fightmenu.blit(bc3,(100,60))
                                elif bcanim >= 60 and bcanim < 75:
                                    fightmenu.blit(overwrite,(100,60))
                                    fightmenu.blit(bc4,(100,60))
                                elif bcanim >= 75 and bcanim < 90:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(bc5,(100,60))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                elif bcanim >= 90 and bcanim < 105:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(bc6,(100,60))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                elif bcanim >= 105 and bcanim < 120:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(bc7,(100,60))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                elif bcanim >= 135 and bcanim < 150:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(bc8,(100,60))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                elif bcanim >= 160:
                                    anim = False
                                pygame.display.update()
                            uhp = uhp-(round(random.randint(17,23)*omod))
                            pygame.mixer.Sound.play(hit)
                            utext()

                        if fight_btn2.draw() == True:
                            pygame.mixer.Sound.play(click)
                            anim = True
                            global gsanim
                            gsanim = 0
                            while anim:
                                clock.tick(60)
                                gsanim = gsanim+1
                                if gsanim < 15:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                    fightmenu.blit(gs1,(100,60))
                                    if gsanim == 2:
                                        pygame.mixer.Sound.play(geq)
                                elif gsanim >= 15 and gsanim < 30:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                    fightmenu.blit(gs2,(100,60))
                                elif gsanim >= 30 and gsanim < 45:
                                    fightmenu.blit(bg,(0,0)) 
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                    fightmenu.blit(gs3,(100,60))
                                    if gsanim == 43:
                                        pygame.mixer.Sound.play(hit)
                                elif gsanim >= 60:
                                    anim = False
                                pygame.display.update()
                            uhp = uhp-(random.randint(48,54))
                            omod = omod - random.uniform(0.1,0.3)
                            guitarhp = guitarhp-random.randint(40,60)
                            utext()

                if guitarhp <= 0:
                        if fight_btn3.draw() == True:
                            pygame.mixer.Sound.play(click)
                            panim = 0
                            anim = True
                            while anim:
                                clock.tick(60)
                                panim = panim+1
                                fightmenu.blit(fbox,(0,261))
                                if panim < 20:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(p1,(100,60))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                elif panim >= 20 and panim < 40:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(p2,(100,60))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                elif panim >= 40 and panim < 60:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(p3,(100,60))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                elif panim >= 70:
                                    anim = False
                                pygame.display.update()
                            uhp = uhp-(random.randint(7,12))
                            pygame.mixer.Sound.play(hit)
                            utext()

                        if fight_btn4.draw() == True:
                            pygame.mixer.Sound.play(click)
                            kanim = 0
                            anim = True
                            while anim:
                                clock.tick(60)
                                kanim = kanim+1
                                fightmenu.blit(fbox,(0,261))
                                if kanim < 20:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(k1,(100,60))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                elif kanim >= 20 and kanim < 40:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(k2,(100,60))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                elif kanim >= 40 and kanim < 60:
                                    fightmenu.blit(bg,(0,0))
                                    fightmenu.blit(ukrossf,(440,8))
                                    fightmenu.blit(k3,(100,60))
                                    fightmenu.blit(fbox,(0,261))
                                    fightmenu.blit(uhpbar,(387,25))
                                    fightmenu.blit(ohpbar,(23,25))
                                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                                elif kanim >= 70:
                                    anim = False
                                pygame.display.update()
                            uhp = uhp-(random.randint(7,12))
                            pygame.mixer.Sound.play(hit)
                            utext()

                if exit_btn.draw() == True:
                    pygame.mixer.Sound.play(click)
                    oturn()
                
                pygame.display.update()
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        pygame.quit()

        def imenu():
            global i1,i2,i3,i4
            global uhp,ohp,omod,guitarhp
            iopt = True
            while iopt:
              
                fightmenu.blit(bg,(0,0))
                if guitarhp > 0:
                    fightmenu.blit(orphf,(100,60))
                elif guitarhp <= 0:
                    fightmenu.blit(orphf2,(100,60))
                fightmenu.blit(ukrossf,(440,8))
                fightmenu.blit(fbox,(0,261))
                exit_btn = Button(497, 300, ebtn)
                fightmenu.blit(uhpbar,(387,25))
                fightmenu.blit(ohpbar,(23,25))
                pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))
                fightmenu.blit(ibtn3,(264,320))
                fightmenu.blit(ibtn3,(264,340))

                if i1 == True:
                    itm_btn1 = Button(30, 300, ibtn1)
                elif i1 == False:
                    itm_btn1 = Button(30, 300, ibtn3)

                if i2 == True:
                    itm_btn2 = Button(30, 320, ibtn1)
                elif i2 == False:
                    itm_btn2 = Button(30, 320, ibtn3)

                if i3 == True:
                    itm_btn3 = Button(30, 340, ibtn2)
                elif i3 == False:
                    itm_btn3 = Button(30, 340, ibtn3)

                if i4 == True:
                    itm_btn4 = Button(264, 300, ibtn2)
                elif i4 == False:
                    itm_btn4 = Button(264, 300, ibtn3)

                if (itm_btn1.draw() == True) and (i1 == True):
                        i1 = False
                        pygame.mixer.Sound.play(click)
                        if guitarhp > 0:
                                anim = True
                                canim = 0
                                while anim:
                                    clock.tick(60)
                                    canim = canim+1
                                    if canim < 10:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(c1,(100,60))
                                        fightmenu.blit(fbox,(0,261))
                                    elif canim >= 10 and canim < 20:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(c2,(100,60))
                                    elif canim >= 20 and canim < 30:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b5,(100,60))
                                        if canim == 22:
                                            pygame.mixer.Sound.play(heal)
                                    elif canim >= 30 and canim < 40:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b3,(100,60))
                                    elif canim >= 40 and canim < 50:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b4,(100,60))
                                    elif canim >= 50 and canim < 60:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b5,(100,60))
                                        
                                    elif canim >= 70:
                                        anim = False
                                    pygame.display.update()
                        elif guitarhp <= 0:
                                anim = True
                                canim = 0
                                while anim:
                                    clock.tick(60)
                                    canim = canim+1
                                    if canim < 10:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pc1,(100,60))
                                        fightmenu.blit(fbox,(0,261))
                                    elif canim >= 10 and canim < 20:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pc2,(100,60))
                                    elif canim >= 20 and canim < 30:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb5,(100,60))
                                        if canim == 22:
                                            pygame.mixer.Sound.play(heal)
                                    elif canim >= 30 and canim < 40:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb3,(100,60))
                                    elif canim >= 40 and canim < 50:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb4,(100,60))
                                    elif canim >= 50 and canim < 60:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb5,(100,60))
                                        
                                    elif canim >= 70:
                                        anim = False
                                    pygame.display.update()

                        ohp = ohp+75
                        if ohp > 250:
                            ohp = 250
                        utext()
                    
                if (itm_btn2.draw() == True) and (i2 == True):
                        i2 = False
                        pygame.mixer.Sound.play(click)
                        if guitarhp > 0:
                                anim = True
                                canim = 0
                                while anim:
                                    clock.tick(60)
                                    canim = canim+1
                                    if canim < 10:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(c1,(100,60))
                                        fightmenu.blit(fbox,(0,261))
                                    elif canim >= 10 and canim < 20:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(c2,(100,60))
                                    elif canim >= 20 and canim < 30:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b5,(100,60))
                                        if canim == 22:
                                            pygame.mixer.Sound.play(heal)
                                    elif canim >= 30 and canim < 40:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b3,(100,60))
                                    elif canim >= 40 and canim < 50:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b4,(100,60))
                                    elif canim >= 50 and canim < 60:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b5,(100,60))
                                        
                                    elif canim >= 70:
                                        anim = False
                                    pygame.display.update()
                        elif guitarhp <= 0:
                                anim = True
                                canim = 0
                                while anim:
                                    clock.tick(60)
                                    canim = canim+1
                                    if canim < 10:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pc1,(100,60))
                                        fightmenu.blit(fbox,(0,261))
                                    elif canim >= 10 and canim < 20:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pc2,(100,60))
                                    elif canim >= 20 and canim < 30:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb5,(100,60))
                                        if canim == 22:
                                            pygame.mixer.Sound.play(heal)
                                    elif canim >= 30 and canim < 40:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb3,(100,60))
                                    elif canim >= 40 and canim < 50:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb4,(100,60))
                                    elif canim >= 50 and canim < 60:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb5,(100,60))
                                        
                                    elif canim >= 70:
                                        anim = False
                                    pygame.display.update()

                        ohp = ohp+75
                        if ohp > 250:
                            ohp = 250
                        utext()

                if (itm_btn3.draw() == True) and (i3 == True):
                        i3 = False
                        pygame.mixer.Sound.play(click)
                        if guitarhp > 0:
                                anim = True
                                canim = 0
                                while anim:
                                    clock.tick(60)
                                    canim = canim+1
                                    if canim < 10:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b1,(100,60))
                                        fightmenu.blit(fbox,(0,261))
                                    elif canim >= 10 and canim < 20:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b2,(100,60))
                                    elif canim >= 20 and canim < 30:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b5,(100,60))
                                        if canim == 22:
                                            pygame.mixer.Sound.play(heal)
                                    elif canim >= 30 and canim < 40:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b3,(100,60))
                                    elif canim >= 40 and canim < 50:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b4,(100,60))
                                    elif canim >= 50 and canim < 60:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b5,(100,60))
                                        
                                    elif canim >= 70:
                                        anim = False
                                    pygame.display.update()
                        elif guitarhp <= 0:
                                anim = True
                                canim = 0
                                while anim:
                                    clock.tick(60)
                                    canim = canim+1
                                    if canim < 10:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb1,(100,60))
                                        fightmenu.blit(fbox,(0,261))
                                    elif canim >= 10 and canim < 20:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb2,(100,60))
                                    elif canim >= 20 and canim < 30:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb5,(100,60))
                                        if canim == 22:
                                            pygame.mixer.Sound.play(heal)
                                    elif canim >= 30 and canim < 40:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb3,(100,60))
                                    elif canim >= 40 and canim < 50:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb4,(100,60))
                                    elif canim >= 50 and canim < 60:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb5,(100,60))
                                        
                                    elif canim >= 70:
                                        anim = False
                                    pygame.display.update()

                        ohp = ohp+75
                        if ohp > 250:
                            ohp = 250
                        utext()

                if (itm_btn4.draw() == True) and (i4 == True):
                        i4 = False
                        pygame.mixer.Sound.play(click)
                        if guitarhp > 0:
                                anim = True
                                canim = 0
                                while anim:
                                    clock.tick(60)
                                    canim = canim+1
                                    if canim < 10:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b1,(100,60))
                                        fightmenu.blit(fbox,(0,261))
                                    elif canim >= 10 and canim < 20:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b2,(100,60))
                                    elif canim >= 20 and canim < 30:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b5,(100,60))
                                        if canim == 22:
                                            pygame.mixer.Sound.play(heal)
                                    elif canim >= 30 and canim < 40:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b3,(100,60))
                                    elif canim >= 40 and canim < 50:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b4,(100,60))
                                    elif canim >= 50 and canim < 60:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(b5,(100,60))
                                        
                                    elif canim >= 70:
                                        anim = False
                                    pygame.display.update()
                        elif guitarhp <= 0:
                                anim = True
                                canim = 0
                                while anim:
                                    clock.tick(60)
                                    canim = canim+1
                                    if canim < 10:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb1,(100,60))
                                        fightmenu.blit(fbox,(0,261))
                                    elif canim >= 10 and canim < 20:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb2,(100,60))
                                    elif canim >= 20 and canim < 30:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb5,(100,60))
                                        if canim == 22:
                                            pygame.mixer.Sound.play(heal)
                                    elif canim >= 30 and canim < 40:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb3,(100,60))
                                    elif canim >= 40 and canim < 50:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb4,(100,60))
                                    elif canim >= 50 and canim < 60:
                                        fightmenu.blit(overwrite,(100,60))
                                        fightmenu.blit(pb5,(100,60))
                                        
                                    elif canim >= 70:
                                        anim = False
                                    pygame.display.update()

                        ohp = ohp+75
                        if ohp > 250:
                            ohp = 250
                        utext()

                if exit_btn.draw() == True:
                    pygame.mixer.Sound.play(click)
                    oturn()
                
                pygame.display.update()
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        pygame.quit()

        def amenu():
            global uhp,ohp,omod,guitarhp
            aopt = True
            while aopt:
                fightmenu.blit(bg,(0,0))
                if guitarhp > 0:
                        fightmenu.blit(orphf,(100,60))
                elif guitarhp <= 0:
                        fightmenu.blit(orphf2,(100,60))
                fightmenu.blit(ukrossf,(440,8))
                fightmenu.blit(fbox,(0,261))
                if guitarhp > 0:
                    act_btn1 = Button(30, 300, abtn1)
                elif guitarhp <= 0:
                    fightmenu.blit(abtn4,(30,300))
                if compNum < 5:
                    act_btn2 = Button(264, 300, abtn2)
                elif compNum == 5:
                    act_btn3 = Button(264,300, abtn3)
                exit_btn = Button(497, 300, ebtn)
                fightmenu.blit(uhpbar,(387,25))
                fightmenu.blit(ohpbar,(23,25))
                pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))

                if guitarhp > 0:
                        if act_btn1.draw() == True:
                            pygame.mixer.Sound.play(click)
                            omod = omod+random.uniform(0.1,0.3)
                            anim = True
                            tanim = 0
                            while anim:
                                clock.tick(60)
                                tanim = tanim+1
                                fightmenu.blit(fbox,(0,261))
                                if tanim < 20:
                                    fightmenu.blit(overwrite,(100,60))
                                    fightmenu.blit(t1,(100,60))
                                elif tanim >= 20 and tanim < 40:
                                    fightmenu.blit(overwrite,(100,60))
                                    fightmenu.blit(t2,(100,60))
                                elif tanim >= 50:
                                    anim = False
                                pygame.display.update()
                            utext()

                try:
                    if act_btn2.draw() == True:
                            pygame.mixer.Sound.play(click)
                            text()
                except:
                    pass

                try:
                    if act_btn3.draw() == True:
                            pygame.mixer.Sound.play(click)
                            forgive()
                except:
                    pass
                        
                if exit_btn.draw() == True:
                    pygame.mixer.Sound.play(click)
                    oturn()
                
                pygame.display.update()
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        pygame.quit()

        def oturn():
            global uhp,ohp,omod,guitarhp
            run = True
            while run:
              
                fightmenu.blit(bg,(0,0))
                if guitarhp > 0:
                        fightmenu.blit(orphf,(100,60))
                elif guitarhp <= 0:
                        fightmenu.blit(orphf2,(100,60))
                fightmenu.blit(ukrossf,(440,8))
                fightmenu.blit(fbox,(0,261))
                fight_btn = Button(30, 300, fbtn)
                item_btn = Button(264, 300, ibtn)
                action_btn = Button(497, 300, abtn)
                fightmenu.blit(uhpbar,(387,25))
                fightmenu.blit(ohpbar,(23,25))
                pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))

                pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))

                if fight_btn.draw() == True:
                    pygame.mixer.Sound.play(click)
                    fmenu()

                if item_btn.draw() == True:
                    pygame.mixer.Sound.play(click)
                    imenu()

                if action_btn.draw() == True:
                    pygame.mixer.Sound.play(click)
                    amenu()
            
                pygame.display.update()
                for event in pygame.event.get ():
                        if event.type == pygame.QUIT:
                           pygame.quit()

        def text():
                global compNum
                global count
                global compResp1,compResp2,compResp3,compResp4,compResp5
                FONT = pygame.font.Font("yoster.ttf",20)

                if compNum == 0:
                        count = 0
                        text = "Hey, round guy! I like your um... circle-ness?"
                        compResp1 = True
                elif compNum == 1:
                        count = 0
                        text = "Ukross, I um, think your hat is... Nifty?"
                        compResp2 = True
                elif compNum == 2:
                        count = 0
                        text = "The red of your tie really makes your eye pop."
                        compResp3 = True
                elif compNum == 3:
                        count = 0
                        text = "You're a great fighter bud!"
                        compResp4 = True
                elif compNum == 4:
                        count = 0
                        text = "I admire your determination Ukross..."
                        compResp5 = True

                previousWidth = 0
                def getSurfaces(text,pos):
                    global previousWidth
                    surfaces = []
                    positions = []
                    previousWidth = 0
                    for i in range(len(text)):
                        surf = FONT.render(f"{text[i]}", True, white)
                        surfaces.append(surf)
                    for i in range(len(surfaces)):
                        previousWidth += surfaces[i-1].get_rect().width
                        positions.append([previousWidth + pos[0], pos[1]])
                    return surfaces, positions

                surfaces, positions = getSurfaces(text, [100,325])

                start = time.time()
                count = 0
                def npc_one_dialogue(delay=0.07):
                    global count
                    global start
                    now = time.time()
                    if count < len(surfaces):
                        if now - start > delay:
                            count +=1
                            start = now
                            pygame.mixer.Sound.play(talksound2)
                    for i in range(count):
                            fightmenu.blit(surfaces[i], (positions[i][0], positions[i][1]))

                while True:
                    pygame.event.get()
                    fightmenu.blit(bg,(0,0))
                    if guitarhp > 0:
                            fightmenu.blit(orphf,(100,60))
                    elif guitarhp <= 0:
                            fightmenu.blit(orphf2,(100,60))
                    fightmenu.blit(ukrossf,(440,8))
                    fightmenu.blit(orphbox,(0,261))        
                    fightmenu.blit(uhpbar,(387,25))
                    fightmenu.blit(ohpbar,(23,25))
                    pygame.draw.rect(fightmenu,green,pygame.Rect(30,30,ohp,25))
                    pygame.draw.rect(fightmenu,green,pygame.Rect(642-250,30,uhp,25))
                    pygame.draw.rect(fightmenu,yellow,pygame.Rect(33,57,guitarhp,7))

                    npc_one_dialogue()

                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_e: 
                                previousWidth = 0
                                count = 0
                                start = 0
                                compNum = compNum+1
                                utext()


        oturn()
        pygame.quit()
except:
        pass
