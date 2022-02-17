"""
fnaf

Description:
"""

#import libraries
import pygame
import pygame.freetype
import random
import sys
import Cam
import Bonnie as bai
import Foxy as fai
import Chica as cai

#gameplay
nightone = False
gameover= False
poweroff = False
cams = False
win = False

#set up cams and AI
cam_bool = Cam.whatcam(True, False, False, False, False, False, False, False, False, False, False)
bonnie = bai.Bonnie_Move(True)
foxy = fai.Foxy_Move(True)
chica = cai.Chica_Move(True)





#Freddy phases
fhase0 = True



#door and light bools
dopen1 = False
dopen2 = False
light1 = False
light2 = False

#light timer
light_timer = 1000
light2_timer = 1000

#animatronic timers
freddy_timer = 10000
chica_timer = 3000

office_time = 0
power = 100000



#init pygame
pygame.init()
#keep time
c = pygame.time.Clock()


#setup display, fonts, and images
window = pygame.display.set_mode([1000, 600])
font = pygame.freetype.SysFont("Times New Roman", 0) 

#Freddy Fazbear *vine boom*
Freddy = pygame.image.load("BearPapa.png")
Freddy2 = pygame.image.load("BearBaby.png")
Freddy3 = pygame.image.load("BearMama.png")

#not Sir Fredrick Fitzgerald Fazbear III
Chica = pygame.image.load("Chick.png")
Bonnie = pygame.image.load("RabbitStand.png")
Foxy = pygame.image.load("DogCorgi.png")

#Freddy twitch timer
timer = 1000

#Time variable
time_passed = 0

#seconds in a minute
minute = 60

#main loop
game = True
while game:
    
    #title screen
    fnaf = True
    while fnaf:
        #scene setup
        window.fill((0, 0, 0))
        button = pygame.Rect(100, 430, 300, 50)
        button2 = pygame.Rect(100, 500, 300, 50)
        button3 = pygame.Rect(100, 0, 300, 50)
        button4 = pygame.Rect(100, 550, 300, 50)
        
        #event loop
        for event in pygame.event.get():
            #exit game
            if event.type == pygame.QUIT:
                    game = False
                        
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # gets mouse position
                mouse_pos = event.pos  
        
                #Check if quit button
        
                if button2.collidepoint(mouse_pos):
                    sys.exit()
                
                #if start game
                elif button.collidepoint(mouse_pos):
                    
                    #reset pygame time
                    pygame.init()
                    
                    #active animatronics
                    bonnie.reset_ai()
                    foxy.reset_ai()
                    chica.reset_ai()
                    
                    #reset power and hours
                    office_time = 0
                    power = 100000
                    
                    
                    #reset booleans
                    win = False
                    fnaf = False
                    nightone = True
                    poweroff = False
                    gameover = False

                    
                    
                
                #spare button
                elif button3.collidepoint(mouse_pos):
                    print("")
        
        #Title text
        font.size = 50
        font.fgcolor = (255, 255, 255)
        font.render_to(window, (100, 50), "Five")
        font.render_to(window, (100, 100), "Nights")
        font.render_to(window, (100, 150), "at")
        font.render_to(window, (100, 200), "Freddy's")
        
        #mouse not visable
        pygame.mouse.set_visible(False)
                
        #Text for buttons
        font.render_to(window, (100, 430), "New Game")
        font.render_to(window, (100, 500), "Quit")
        
        #get mouse position for cursor
        x, y = pygame.mouse.get_pos()
                 
        #If Freddy's twitch animation
        if timer == 0:
            window.blit(Freddy2, (450, 50))
            pygame.display.flip()
            
            pygame.time.wait(5)
            
            window.blit(Freddy3, (450, 50))
            pygame.display.flip()
            
            pygame.time.wait(5)
            
            window.blit(Freddy3, (455, 60))
            pygame.display.flip()
            
            window.blit(Freddy2, (480, 90))
            pygame.display.flip()
            timer = 1000
        
        #regular Freddy
        else:
            window.blit(Freddy, (450, 50))
                
        #cursor
        pygame.draw.circle(window, (0, 255, 0), (x, y), 5)
        
        
        #time freddy
        timer -= 10
        
        #flip!!
        pygame.display.flip()
        
    
    
    #night one (real)
    while nightone:
        
        
        #shorten cam booleans
        cam1a = cam_bool.c1a
        cam1b = cam_bool.c1b
        cam1c = cam_bool.c1c
        cam2a = cam_bool.c2a
        cam2b = cam_bool.c2b
        cam3 = cam_bool.c3
        cam4a = cam_bool.c4a
        cam4b = cam_bool.c4b
        cam5 = cam_bool.c5
        cam6 = cam_bool.c6
        cam7 = cam_bool.c7
        
        #shorten bonnie booleans
        bhase0 = bonnie.bhase0
        bhase1 = bonnie.bhase1
        bhase01 = bonnie.bhase01
        bhase2 = bonnie.bhase2
        bhase02 = bonnie.bhase02
        bhase3 = bonnie.bhase3
        blast = bonnie.blast
        bjump = bonnie.bjump
        
        #shorten foxy booleans
        xhase0 = foxy.xhase0
        xhase1 = foxy.xhase1
        xhase2 = foxy.xhase2
        xhase3 = foxy.xhase3
        xlast = foxy.xlast
        xjump = foxy.xjump

        #chica phases
        chase0 = chica.chase0
        chase1 = chica.chase1
        chase01 = chica.chase01 #chica bathroom
        chase02 = chica.chase02 #chica kitchen
        chase2 = chica.chase2
        chase3 = chica.chase3
        clast = chica.clast
        cjump = chica.cjump
        
        
        window.fill((0, 0, 0))
        
        #office buttons
        button = pygame.Rect(250, 225, 50, 50)
        button2 = pygame.Rect(250, 275, 50, 50)
        button3 = pygame.Rect(700, 225, 50, 50)
        button4 = pygame.Rect(700, 275, 50, 50)
        button5 = pygame.Rect(125, 500, 750, 50)
        
        #cam1a
        bam1 = pygame.Rect(700, 130, 60, 50)
        #cam1b
        bam2 = pygame.Rect(675, 210, 60, 50)
        #cam5
        bam3 = pygame.Rect(570, 200, 60, 50)
        #cam2a
        bam4 = pygame.Rect(715, 350, 60, 50)
        #cam1c
        bam5 = pygame.Rect(650, 270, 60, 50)
        #cam2b
        bam6 = pygame.Rect(715, 410, 60, 50)
        #cam3
        bam7 = pygame.Rect(650, 385, 60, 50)
        #cam4a
        bam8 = pygame.Rect(815, 350, 60, 50)
        #cam4b
        bam9 = pygame.Rect(815, 410, 60, 50)
        #cam7
        bam10 = pygame.Rect(920, 200, 60, 50)
        #cam6
        bam11 = pygame.Rect(920, 300, 60, 50)
        
        
        door1 = pygame.Rect(10, 75, 200, 400)
        door2 = pygame.Rect(800, 75, 200, 400)
        
        # Convert to seconds.
        time = (pygame.time.get_ticks()) / 1000

        # True every 60 seconds / 1 minute.
        if time > (time_passed + minute):
            time_passed = time
            office_time += 1
            
            if office_time == 6:
                win = True
                nightone = False
                
        
        #decrease timers
        bonnie.bonnie_timer -= 10
        foxy.foxy_timer -= 10
        chica.chica_timer -= 10
        power -= 1
        
        #foxy AI
        if foxy.foxy_timer <= 0:
            foxy.init()
            
            
            
            
        
        
        if bonnie.bonnie_timer <= 0:
        
            bonnie.init()
            
                 
        
        if chica.chica_timer <= 0:
            
            chica.init()
            
                    
            
            
            
        if power <= 0:
            cams = False
            nightone = False
            poweroff = True
            
        
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nightone = False
                game = False
            
            #check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #get mouse pos
                mos_pos = event.pos
                
                #door button
                if button.collidepoint(mos_pos):
                    if not cams:
                        if not dopen1:
                            dopen1 = True
                            
                        else:
                            dopen1 = False
                        
                #light button        
                if button2.collidepoint(mos_pos):
                    if not cams:
                        light1 = True  
                        
                if button3.collidepoint(mos_pos):
                    if not cams:
                        if not dopen2:
                            dopen2 = True
                            
                        else:
                            dopen2 = False
                
                #light button 2
                if button4.collidepoint(mos_pos):
                    if not cams:
                        light2 = True
                
                #camera button
                if button5.collidepoint(mos_pos):
                    
                    cam1_y = 600
                    
                    cam2_y = 0
                    
                    
                    if not cams:
                        while cam1_y > 0:
                            window.fill((0, 0, 0))
                            cam1_y -= 20
                            cam_square = pygame.Rect(0, cam1_y, 1000, 600)
                            pygame.draw.rect(window, (80, 80, 80), cam_square)
                            pygame.display.flip()
                        
                        cams = True
                        light1 = False
                        light2 = False
                        
                    else:
                        
                        while cam2_y < 600:
                            window.fill((0, 0, 0))
                            cam2_y += 20
                            cam_square2 = pygame.Rect(0, cam2_y, 1000, 600)
                            pygame.draw.rect(window, (80, 80, 80), cam_square2)
                            pygame.display.flip()
                            
                        cams = False
                
                
                #camera bools
                if cams:
                    
                    
                    
                    if bam1.collidepoint(mos_pos):
                        
                        cam_bool.one_A()
                        
                    if bam2.collidepoint(mos_pos):
                        
                        cam_bool.one_B()
                    
                    if bam3.collidepoint(mos_pos):
                        
                        cam_bool.five()
                        
                    if bam4.collidepoint(mos_pos):
                        
                        cam_bool.two_A()
                    
                    if bam5.collidepoint(mos_pos):
                        
                        cam_bool.one_C()
                        
                    if bam6.collidepoint(mos_pos):
                        
                        cam_bool.two_B()
                    
                    if bam7.collidepoint(mos_pos):
                        
                        cam_bool.three()
                        
                    if bam8.collidepoint(mos_pos):
                        
                        cam_bool.four_A()
                        
                    if bam9.collidepoint(mos_pos):
                        
                        cam_bool.four_B()
                        
                    if bam10.collidepoint(mos_pos):
                        
                        cam_bool.seven()
                        
                    if bam11.collidepoint(mos_pos):
                        
                        cam_bool.six()
        
                
            window.fill((0,0,0))
            
            
            
            
        
                
            
        
        #camera screen
        if cams:
            
            power -= 10
            
            if dopen1:
                power -= 100
                
            if dopen2:
                power -= 100
            
            
            #if foxy jumpscare
            if xjump and dopen1 == False:
                cams = False
                
            if cjump and dopen2 == False:
                cams == False
            
            
            window.fill((0, 0 ,0))
            
            #stage
            if cam1a:
                if chase0:
                    window.blit(Chica, (310, 100))
                    
                window.blit(Freddy2, (230, 150))
                
                if bhase0:
                    window.blit(Bonnie, (100, 250))
            
            #dining room
            elif cam1b:
                if chase1:
                    window.blit(Chica, (400, 300))
                    
                if bhase1:
                    window.blit(Bonnie, (150, 300))
            
            #Pirate cove
            elif cam1c:
                if not xlast and foxy.foxy_timer < 1000 and cams:
                    foxy.foxy_timer += 10
                    
                #foxy neutral phase
                if xhase0:
                    curtain1 = pygame.Rect(200, 20, 400, 500)
                    pygame.draw.rect(window, (64, 22, 160), curtain1)
                    
                #foxy phase 1
                elif xhase1:
                    
                    curtain1 = pygame.Rect(150, 20, 200, 500)
                    
                    curtain2 = pygame.Rect(450, 20, 200, 500)
                    
                    window.blit(Foxy, (200, 200))
                    pygame.draw.rect(window, (64, 22, 160), curtain1)
                    pygame.draw.rect(window, (64, 22, 160), curtain2)
                    
                
                #foxy phase 2
                elif xhase2:
                    curtain1 = pygame.Rect(150, 20, 200, 500)
                    window.blit(Foxy, (200, 200))
                    curtain2 = pygame.Rect(550, 20, 200, 500)
                    pygame.draw.rect(window, (64, 22, 160), curtain1)
                    pygame.draw.rect(window, (64, 22, 160), curtain2)
                
                #foxy phase 3
                elif xhase3:
                    curtain1 = pygame.Rect(150, 20, 200, 500)
                    curtain2 = pygame.Rect(500, 20, 200, 500)
                    
                    pygame.draw.rect(window, (64, 22, 160), curtain1)
                    pygame.draw.rect(window, (64, 22, 160), curtain2)
                    window.blit(Foxy, (200, 200))

                #Before jumpscare
                elif xlast:
                    curtain1 = pygame.Rect(150, 20, 200, 500)
                    curtain2 = pygame.Rect(500, 20, 200, 500)
                    
                    pygame.draw.rect(window, (64, 22, 160), curtain1)
                    pygame.draw.rect(window, (64, 22, 160), curtain2)
                
                
                    
            #Left hall
            elif cam2a:
                #bonnie during phase 2
                if bhase2:
                    window.blit(Bonnie, (500, 100))
            
            #Left door
            elif cam2b:
                
                if bhase3:
                    bonnie_door = pygame.transform.scale(Bonnie, (400, 600))
                    
                    window.blit(bonnie_door, (300, 300))
                    
            elif cam3:
                
                if bhase02:
                    
                    bonnie_closet = pygame.transform.scale(Bonnie, (500, 700))
                    
                    window.blit(bonnie_closet, (500, 300))
            
            elif cam4a:
                
                if chase2:
                    
                    chica_hall = pygame.transform.scale(Chica, (150, 200))
                    
                    window.blit(chica_hall, (475, 100))
                    
            elif cam4b:
                
                if chase3:
                    
                    chica_door = pygame.transform.scale(Chica, (400, 500))
                    
                    window.blit(chica_door, (400, 400))
                    
            #Parts and Service
            elif cam5:
                
                if bhase01:
                    window.blit(Bonnie, (300, 300))
            
            
            elif cam6:
                
                font.size = 50
                font.fgcolor = (255, 255, 255)
                font.render_to(window, (250, 300), "Audio only")
            
            
            elif cam7:
                
                if chase01:
                    window.blit(Chica, (300, 250))
            
            #camera buttons
            pygame.draw.rect(window, (192, 192, 192), bam1)
            pygame.draw.rect(window, (192, 192, 192), bam2)
            pygame.draw.rect(window, (192, 192, 192), bam3)
            pygame.draw.rect(window, (192, 192, 192), bam4)
            pygame.draw.rect(window, (192, 192, 192), bam5)
            pygame.draw.rect(window, (192, 192, 192), bam6)
            pygame.draw.rect(window, (192, 192, 192), bam7)
            pygame.draw.rect(window, (192, 192, 192), bam8)
            pygame.draw.rect(window, (192, 192, 192), bam9)
            pygame.draw.rect(window, (192, 192, 192), bam10)
            pygame.draw.rect(window, (192, 192, 192), bam11)
            
            #turn off camera
            pygame.draw.rect(window, (100, 100, 100), button5, 10)
        
            #Draw mouse
            x, y = pygame.mouse.get_pos()
            pygame.draw.circle(window, (0, 255, 0), (x, y), 5)
            
            
            
            pygame.display.flip()
            
        
        #main office loop
        else:
            
            #foxy jumpscare
            if cjump:
                if dopen2:
                    chica.reset_ai()
                
                else:
                    clast = False
                    jumpx = 300
                    jumpy = 400
                    timer = 0
                    while timer < 1000:
                        window.fill((0, 0, 0))
                        
                        
                        chica_scare = pygame.transform.scale(Chica, (500, 600))

                        window.blit(chica_scare, (jumpx, jumpy))
                        pygame.display.flip()
                        jumpx = random.randint(100, 300)
                        jumpy = random.randint(200, 400)
                        timer += 10
                        
                    
                        
                        
                        
                    cjump = False
                    nightone = False
                    gameover = True
                    break
                        
                        
                        
            if xjump:
                if dopen1:
                    foxy.reset_ai()
                        
                    
                
                else:
                    cams = False
                    xlast = False
                    jumpx = 0
                    while jumpx < 200:
                        window.fill((0,0,0))
                        window.blit(Foxy, (jumpx, 200))
                        jumpx+=10
                        pygame.display.flip()
                        
                    pygame.time.wait(1000)
                        
                    xjump = False
                    nightone = False
                    gameover = True
                    break
            
            
            #Bonnie jumpscare
            if bjump:
                if dopen1:
                    bonnie.reset_ai()
                        
                    
                
                else:
                    if not cams:
                        blast = False
                        jumpx = 300
                        jumpy = 200
                        timer = 0
                        while timer < 1000:
                            window.fill((0,0,0))
                            
                            bonnie_scare = pygame.transform.scale(Bonnie, (500, 600))

                            window.blit(bonnie_scare, (jumpx, jumpy))
                            jumpx = random.randint(100, 300)
                            jumpy = random.randint(100, 300)
                            timer += 10
                            pygame.display.flip()
                        
                        bjump = False
                        nightone = False
                        gameover = True
                        break
                    
            
            
            
            #Office buttons
            pygame.draw.rect(window, (255, 0, 0), button)
            pygame.draw.rect(window, (255, 255, 55), button2)
            pygame.draw.rect(window, (255, 0, 0), button3)
            pygame.draw.rect(window, (255, 255, 55), button4)
            pygame.draw.rect(window, (100, 100, 100), button5, 10)
            
            
            
            
            #Check if door open
            if dopen1:

                power -= 100
                light1 = False
                pygame.draw.rect(window, (192, 192, 192), door1)
                
                
            if dopen2:
                
                power -= 100
                light2 = False
                pygame.draw.rect(window, (192, 192, 192), door2)
            
            #Check if light on
            if light1:
                
                power -= 10
                
                pygame.draw.ellipse(window, (255, 255, 255), door1)
                
                #If Bonnie
                if blast:
                    if not dopen1:
                        window.blit(Bonnie, (10, 250))
                        
                    
                    
                    
                #light timer
                light_timer -= 10
                
                if light_timer <= 0:
                    
                    light1 = False
                    light_timer = 1000
                
            
            #Check if light on
            if light2:
                power -= 10
                
                pygame.draw.ellipse(window, (255, 255, 255), door2)
                
                if clast:
                    window.blit(Chica, (850, 250))
                
                #light2 timer
                light2_timer -= 10
                
                if light2_timer <= 0:
                    
                    light2 = False
                    light2_timer = 1000
                    
                
            
            
            font.size = 25
            font.fgcolor = (255, 255, 255)
            real_power = int(power / 1000)
            
            font.render_to(window, (500, 150), str(real_power) + "% power")
            
            if office_time != 0:
                font.render_to(window, (500, 100), str(office_time) + ":00 AM")
            
            else:
                font.render_to(window, (500, 100), "12:00 AM")
                
            
            #camera button
            pygame.draw.rect(window, (100, 100, 100), button5, 10)
            
            #Draw mouse
            x, y = pygame.mouse.get_pos()
            pygame.draw.circle(window, (0, 255, 0), (x, y), 5)
            
            #framerate
            c.tick(100)
            
            pygame.display.flip()
            
            
    
    
    r = 0
    g = 0
    b = 0
    while win:
        window.fill((0, 0, 0))
        
        
        r += 15
        g += 15
        b += 15
        
        if r == 255:
            pygame.time.wait(3000)
            fnaf = True
            win = False
        
        font.size = 50
        font.fgcolor = (r, g, b)
        
        font.render_to(window, (500, 200), "6:00")
        
        
    
        pygame.display.flip()
        pygame.time.wait(200)
        
    
    last_timer = 0
    while poweroff:
        time = (pygame.time.get_ticks()) / 1000
        
        if time > (time_passed + minute):
            time_passed = time
            office_time += 1
            
            if office_time == 6:
                
                win = True
                nightone = False
                poweroff = False
        
        
        if last_timer >= 1000:
            window.fill((0,0,0))
            pygame.display.flip()
            
            
            poweroff = False
            gameover = True
            break
            
        
        
        last_timer += 50
        window.fill((0, 0, 0))
        
        pygame.time.wait(100)
        
        freddy_power = pygame.transform.scale(Freddy, (100, 100))
        
        window.blit(freddy_power, (100, 300))
        pygame.display.flip()
            
        pygame.time.wait(100)
            
        window.fill((0, 0, 0))
        pygame.display.flip()
        pygame.time.wait(100)
            
        window.blit(freddy_power, (100, 300))
        pygame.display.flip()
        
            
        
            
            
    #Game over sceeen
    while gameover:
        window.fill((0, 0, 0))
        
        font.size = 50
        font.fgcolor = (255, 255, 255)
        font.render_to(window, (500, 200), "Game Over")
        
        
        pygame.display.flip()
        pygame.time.wait(2000)
        
        fnaf = True
        gameover = False
