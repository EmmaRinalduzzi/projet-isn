import pygame
from pygame.locals import *
from pygame_functions import *
from random import randrange
pygame.init()


def LimiteScreen(x, y):
    if x >= 640:
        x = 40
    if x <= 30:
        x = 610
    if y >= 450:
        y = 450
    return (x, y)

# def fonction (x):
    
#     echelles = genereréchelles()

#     for i in range (0,34):             
#         if  x== echelles[i][1]+80:
#             x= echelles[i][1]+30
#     return (x)                    
    
    
       
    


def genereréchelles():

    rows, cols = (35, 35)
    TableauEchelles = [[0 for i in range(cols)] for j in range(rows)]
    y = 510
    for i in range(0, 34):

        echelles = makeSprite("echelle2.png")

        addSpriteImage(echelles, "echelle2.png")
        RandomX = randrange(0, 600)
        y = y-140

        TableauEchelles[i][0] = echelles
        TableauEchelles[i][1] = RandomX
        TableauEchelles[i][2] = y
        
    return TableauEchelles


def PlacerEchelle(echelle, x, y):
    showSprite(echelle)
    moveSprite(echelle, x, y, True)


def generersol():

    rows, cols = (35, 35)
    Tableausol = [[0 for i in range(cols)] for j in range(rows)]
    y = 480
    for i in range(0, 34):

        sol = makeSprite("sol.png")
        addSpriteImage(sol, "sol.png")
        x = 640
        y = y-140
        Tableausol[i][0] = sol
        Tableausol[i][1] = x
        Tableausol[i][2] = y
    return Tableausol


def PlacerSol(sol, x, y):
    showSprite(sol)
    moveSprite(sol, x, y, True)


def genererObstacles():
    rows, cols = (34, 3)
    TableauObstacle = [[0 for i in range(cols)] for j in range(rows)]
    y = 510
    for i in range(0, 34):
        obstacle = makeSprite("obstacle.png")
        addSpriteImage(obstacle, "obstacle.png")
       
        Xaleatoire = randrange(0, 600)

        y = y-140

        TableauObstacle[i][0] = obstacle
        TableauObstacle[i][1] = Xaleatoire
        TableauObstacle[i][2] = y


        showSprite(TableauObstacle[i][0])



        

    return TableauObstacle


def PlacerObstacles(obstacle, x, y):
    
    #showSprite(obstacle)
    moveSprite(obstacle, x, y, True)


def start():

        Victoire = False

        fenetre = pygame.display.set_mode((640, 480))
        TITLE = "Notre jeuuuu"
        pygame.display.set_caption(TITLE)

        Black = (0, 0, 0)
        PersoPosx = 320
        PersoPosy = 400
        # rectScreen = fenetre.get_rect()  # coordonnée du rectangle de l'écran
        #############################################################
        ## Gestion de la musique ####################################
        pygame.mixer.pre_init(44100, 4096)
        pygame.mixer.music.load("mario.mp3")
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play(1)

        TableauEchelles = []
        TableauSol = []
        screenSize(640, 480)
        
        PersoSprite = makeSprite("links.gif", 32)
        
        setBackgroundImage("ciel.JPG")

        moveSprite(PersoSprite, 300, 300, True)
        showSprite(PersoSprite)
        
        
        nextFrame = clock()
        frame = 0
        echelles = genereréchelles()
        sol = generersol()
        
        obstacle = genererObstacles()

        for i in range(0,34):
         
            
            print(i)
            print("mes coordo :"+str(obstacle[i][1]) +" et : "+str(obstacle[i][2]))
        for i in range(0, 34):
            if echelles[i][1] -65 <  obstacle[i][1] < echelles[i][1] + 50 or echelles[i][2] -100 <  obstacle[i][1] < echelles[i][2] + 100:
                obstacle[i][1] = 700
        
                       
        solsolPosx =0
        solsolPosy=440
        solsol = makeSprite("sol.png")        
        addSpriteImage(solsol,"sol.png")                 
        showSprite(solsol)

        drapeau = makeSprite("drapeau.png")        
        addSpriteImage(drapeau,"drapeau.png")                 
        drapeauposy =245
        drapeauposx= randrange(100,400)

        
        
        while True:
            if clock() > nextFrame:                         
                frame = (frame+1)%8                         
                nextFrame += 80 
                scrollBackground (0, +2)
                for i in range(0,len(echelles)-2):
                    echelles [i][2] += 2
            
                for i in range(0,len(sol)-2):
                    sol [i][2] += 2
                for i in range(0,34):
                    obstacle [i][2] += 2
                PersoPosy += 2
                solsolPosy +=2
                
            if nextFrame >10000:
                scrollBackground (0,+1) 
                PersoPosy += 0.20
                for i in range(0, len(echelles)-1):
                    echelles [i][2] += 1
                for i in range(0,len(sol)-1):
                    sol [i][2] += 1
                for i in range(0,34):
                    obstacle [i][2] += 1
                PersoPosy += 1
                # scrollEchelles ( 0, +1)
            if nextFrame >25000:
                scrollBackground (0,+1)
                PersoPosy += 0.25
                for i in range(0,len(echelles)-1):
                    echelles [i][2] += 1
                for i in range(0,len(sol)-1):
                    sol [i][2] += 1
                for i in range(0,34):
                    obstacle [i][2] += 1
                PersoPosy += 1
                # scrollEchelles ( 0, +1)
            if nextFrame >50000:
                scrollBackground (0,+1)
                PersoPosy += 0.25
                for i in range(0,len(echelles)-1):
                    echelles [i][2] += 1
                for i in range(0,len(sol)-1):
                    sol [i][2] += 1
                for i in range(0,34):
                    obstacle [i][2] += 1
                PersoPosy += 1

            

            if nextFrame >60000:
                scrollBackground (0,+1)
                PersoPosy += 0.25
                for i in range(0,len(echelles)-1):
                    echelles [i][2] += 1  
                for i in range(0,len(sol)-1):
                    sol [i][2] += 1  
                for i in range(0,34):
                     obstacle [i][2] += 1

            collisionObstacle= False
            for i in range (34):
                
                if touching(obstacle[i][0], PersoSprite) :
                    print("jejejee")
                    print(touching(obstacle[i][0], PersoSprite),obstacle[i], i)
                    collisionObstacle = True
                    gameover = makeSprite("gameover.png")        
                    addSpriteImage(gameover,"gameover.png")
                    moveSprite(gameover, 0, 0)                      
                    showSprite(gameover) 
                    pygame.mixer.music.set_volume(0.0)
                    moveSprite(PersoSprite,110,40,True)
                    showSprite(PersoSprite)
                    break

            if nextFrame > 70000 and Victoire == False:
               
                winner = makeSprite("winner.png")        
                addSpriteImage(winner,"winner.png")
                moveSprite(winner, 0, 0)                       
                showSprite(drapeau)
                drapeauposy +=1
                if touching (drapeau, PersoSprite):
                    PersoPosy = -5000
                    if(Victoire == False):
                         hideAll()
                         fond = pygame.image.load("noir.jpg").convert()
                    Victoire = True

                    setBackgroundColour(Black)
                
                   
                    showSprite(winner)
                 
                    while True:
                        if keyPressed("space"):
                            return 1

                        
                        
            if PersoPosy >= 450:
               
                gameover = makeSprite("gameover.png")        
                addSpriteImage(gameover,"gameover.png")
                moveSprite(gameover, 0, 0)                      
                showSprite(gameover) 
                pygame.mixer.music.set_volume(0.0)
                moveSprite(PersoSprite,110,40,True) 
                showSprite(PersoSprite)
                moveSprite(gameover, 0, 0)                      
                showSprite(gameover) 
                pygame.mixer.music.set_volume(0.0)
                moveSprite(PersoSprite,110,40,True)
                showSprite(PersoSprite)
                break

            
            
            if keyPressed("right"):
                changeSpriteImage(PersoSprite, 0*8+frame)    
                PersoPosx += 20
                allerDroite= True
                for i in range (0,34):
                    if echelles[i][1]<  PersoPosx < echelles[i][1] + 80:
                        allerDroite= False
                        

            # elif keyPressed("down"):
            #     changeSpriteImage(PersoSprite, 1*8+frame)   
            #     PersoPosy += 10

            elif keyPressed("left"):
                changeSpriteImage(PersoSprite, 2*8+frame)    
                PersoPosx -= 20
                
              
            elif keyPressed("up") :
                monterPossible= False
                for i in range (34):
                    if touching(echelles[i][0], PersoSprite) :
                        monterPossible = True
                    
                        
                if monterPossible: 
                    changeSpriteImage(PersoSprite, 3*8+frame)
                    PersoPosy -= 15
            

            else:
                changeSpriteImage(PersoSprite, 1 * 8 + 5)  
            
        

            TableauPositions = LimiteScreen(PersoPosx,PersoPosy) #verifier si le joueur ne sort pas de l'écran
            PersoPosx = TableauPositions[0]
            PersoPosy = TableauPositions[1]

            #fonction (PersoPosx)
            

            if Victoire == False:
                for i in range(0,len(echelles)-1):
                    PlacerEchelle(echelles[i][0],echelles[i][1],echelles[i][2])
                    

                for i in range(0,len(sol)-1):
                    PlacerSol(sol[i][0],sol[i][1],sol[i][2])
                    moveSprite(PersoSprite,PersoPosx,PersoPosy,True)
                    moveSprite(solsol, solsolPosx, solsolPosy) 

                for i in range(0,34):
                    PlacerObstacles(obstacle[i][0],obstacle[i][1],obstacle[i][2])
                    moveSprite(PersoSprite,PersoPosx,PersoPosy,True)
                    

                moveSprite(drapeau, drapeauposx, drapeauposy)  
                 
            
            tick(100)


        endWait()


