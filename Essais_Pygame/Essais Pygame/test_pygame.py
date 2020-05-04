## Initialisation ###########################################


def LimiteScreen(x,y):
    if x >= 620:
        x = 40
    if x <=30:
        x = 610
    if y >= 450:
        y = 450
    return (x,y)

def genereréchelles():
    
    rows, cols = (35, 35) 
    TableauEchelles = [[0 for i in range(cols)] for j in range(rows)] 
    y= 510
    for i in range(0,34):
        
        echelles = makeSprite("echelle2.png")
        #objet_rect=echelles.get_rect() 
       # mon_rect=pygame.Rect(objet_rect)
        addSpriteImage(echelles,"echelle2.png")                
        RandomX = randrange(0,600)
        y= y-140
        
        TableauEchelles[i][0]=echelles
        TableauEchelles[i][1]=RandomX
        TableauEchelles[i][2]=y
    return TableauEchelles

def PlacerEchelle(echelle, x, y):
    showSprite(echelle) 
    moveSprite(echelle,x,y,True)
   

def generersol():
    
    rows, cols = (35, 35) 
    Tableausol = [[0 for i in range(cols)] for j in range(rows)] 
    y= 480
    for i in range(0,34):
        
        sol = makeSprite ("sol.png")
        addSpriteImage(sol,"sol.png")               
        x = 640
        y= y-140
        Tableausol[i][0]=sol
        Tableausol[i][1]=x
        Tableausol[i][2]=y
    return Tableausol

def PlacerSol(sol, x, y):
    showSprite(sol) 
    moveSprite(sol,x,y,True)


def genererObstacles():
    rows, cols = (35, 35) 
    TableauObstacle = [[0 for i in range(cols)] for j in range(rows)] 
    y= 510
    for i in range(0,34):
        obstacle= makeSprite("obstacle.png")
        addSpriteImage(obstacle, "obstacle.png")
        Xaleatoire= randrange(0,600)
        y= y-140
        
        TableauObstacle[i][0]=obstacle
        TableauObstacle[i][1]=Xaleatoire
        TableauObstacle[i][2]=y
    return TableauObstacle

def PlacerObstacles(obstacle, x, y):
    showSprite(obstacle) 
    moveSprite(obstacle,x,y,True)


import pygame
from start import *  
from pygame.locals import *
from pygame_functions import * 
from random import randrange 
if start()==1:
    hideAll()
    start()


# for event in pygame.event.get ():
#     if event.type == K_SPACE:
#         start ()


# pygame.init()
# fenetre = pygame.display.set_mode((640, 480))
# TITLE = "Notre jeuuuu"while lancement:

       
# pygame.display.set_caption(TITLE)

# Black = (0,0,0)
# PersoPosx = 320
# PersoPosy = 400
# #rectScreen = fenetre.get_rect()  # coordonnée du rectangle de l'écran
# #############################################################
# ## Gestion de la musique ####################################
# pygame.mixer.pre_init(44100, 4096)
# pygame.mixer.music.load("mario.mp3")
# pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play(-1)

# TableauEchelles = []

# screenSize(640, 480)
# PersoSprite  = makeSprite("links.gif", 32)  # links.gif contains 32 separate frames of animation.
# #EchelleSprite = makeSprite("echelle2.png")
# #addSpriteImage(EchelleSprite,"echelle2.png")
# setBackgroundImage("ciel.JPG")

# moveSprite(PersoSprite,300,300,True)
# showSprite(PersoSprite)
# #setEchellesImage ("echelle1.png")


# nextFrame = clock()
# frame = 0
# echelles = genereréchelles()
# sol = generersol()
# #print("Debug fonction")
# #print(echelles)
# solsolPosx =0
# solsolPosy=440
# solsol = makeSprite("sol.png")        
# addSpriteImage(solsol,"sol.png")                 
# showSprite(solsol)

# drapeau = makeSprite("drapeau.png")        
# addSpriteImage(drapeau,"drapeau.png")                 
# drapeauposy =345
# drapeauposx= randrange(100,400)
# while True:
 
#     if clock() > nextFrame:                         
#         frame = (frame+1)%8                         
#         nextFrame += 80 
#         scrollBackground (0, +1)
#         for i in range(0,len(echelles)-1):
#             echelles [i][2] += 1
       
#         for i in range(0,len(sol)-1):
#             sol [i][2] += 1
#         PersoPosy += 1
#         solsolPosy +=1
#         #scrollEchelles ( 0, +1)
        
#     if nextFrame >10000:
#         scrollBackground (0,+1) 
#         PersoPosy += 0.20
#         for i in range(0, len(echelles)-1):
#             echelles [i][2] += 1
#         for i in range(0,len(sol)-1):
#             sol [i][2] += 1
#         PersoPosy += 1
#         #scrollEchelles ( 0, +1)
#     if nextFrame >25000:
#         scrollBackground (0,+1)
#         PersoPosy += 0.25
#         for i in range(0,len(echelles)-1):
#             echelles [i][2] += 1
#         for i in range(0,len(sol)-1):
#             sol [i][2] += 1
#         PersoPosy += 1
#         #scrollEchelles ( 0, +1)
#     if nextFrame >50000:
#         scrollBackground (0,+1)
#         PersoPosy += 0.25
#         for i in range(0,len(echelles)-1):
#             echelles [i][2] += 1
#         for i in range(0,len(sol)-1):
#             sol [i][2] += 1
#         PersoPosy += 1

#     if nextFrame >60000:
#         scrollBackground (0,+1)
#         PersoPosy += 0.25
#         for i in range(0,len(echelles)-1):
#             echelles [i][2] += 1  
#         for i in range(0,len(sol)-1):
#             sol [i][2] += 1  
#     if nextFrame > 500:
#         winner = makeSprite("winner.png")        
#         addSpriteImage(winner,"winner.png")
#         moveSprite(winner, 0, 0)                       
#         showSprite(drapeau)
#         drapeauposy +=1
#         if touching (drapeau, PersoSprite):
#             setBackgroundColour(Black)
#            # hideSprite(echelles)
#             #hideSprite(solsol)
#             hideAll()
#             showSprite(winner)
#             if lancement == TRUE:
#                 start()


#                          #on change le drapeau Menu et on le met à 0 et le drapeau Jeu à 1 (par exemple) et a_propos à 0
#                             #recommencer = 0
                           
                        
                       
#             break 

#     if PersoPosy >= 450:

#         gameover = makeSprite("gameover.png")        
#         addSpriteImage(gameover,"gameover.png")
#         moveSprite(gameover, 0, 0)                      
#         showSprite(gameover) 
#         pygame.mixer.music.set_volume(0.0)
#         moveSprite(PersoSprite,110,40,True)
#         showSprite(PersoSprite)
#         break

#     if keyPressed("right"):
#         changeSpriteImage(PersoSprite, 0*8+frame)    
#         PersoPosx += 15
#     elif keyPressed("down"):
#         changeSpriteImage(PersoSprite, 1*8+frame)   
#         PersoPosy += 10
#     elif keyPressed("left"):
#         changeSpriteImage(PersoSprite, 2*8+frame)    
#         PersoPosx -= 15
        
#     elif keyPressed("up") :
#         monterPossible= False
#         for i in range (34):
#             if touching(echelles[i][0], PersoSprite) :
#                 monterPossible = True
#         if monterPossible: 
#             changeSpriteImage(PersoSprite, 3*8+frame)
#             PersoPosy -= 10
        
#     elif keyPressed("escape"):
#         pygame.quit()
#     else:
#         changeSpriteImage(PersoSprite, 1 * 8 + 5)  
    
   

#     TableauPositions = LimiteScreen(PersoPosx,PersoPosy) #verifier si le joueur ne sort pas de l'écran
#     PersoPosx = TableauPositions[0]
#     PersoPosy = TableauPositions[1]


#     for i in range(0,len(echelles)-1):
#         PlacerEchelle(echelles[i][0],echelles[i][1],echelles[i][2])
  

#     for i in range(0,len(sol)-1):
#         PlacerSol(sol[i][0],sol[i][1],sol[i][2])
#     moveSprite(PersoSprite,PersoPosx,PersoPosy,True)
#     moveSprite(solsol, solsolPosx, solsolPosy) 

#     moveSprite(drapeau, drapeauposx, drapeauposy)  
    
#     tick(100)


# endWait()
