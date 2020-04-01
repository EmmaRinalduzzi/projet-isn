## Initialisation ###########################################


def LimiteScreen(x,y):
    if x >= 640 :
        x = 640
    if x <=30:
        x = 30
    if y >= 450:
        y = 450
    return (x,y)

import pygame
from pygame.locals import *
from pygame_functions import * 
pygame.init()
fenetre = pygame.display.set_mode((640, 480))
TITLE = "message emma"
pygame.display.set_caption(TITLE)

PersoPosx = 320
PersoPosy = 320
#rectScreen = fenetre.get_rect()  # coordonnée du rectangle de l'écran
#############################################################
## Gestion de la musique ####################################
pygame.mixer.pre_init(44100, 4096)
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
  
screenSize(640, 480)
PersoSprite  = makeSprite("links.gif", 32)  # links.gif contains 32 separate frames of animation.
setBackgroundImage("image.jpg")
moveSprite(PersoSprite,300,300,True)
showSprite(PersoSprite)

nextFrame = clock()
frame = 0
while True:
    if clock() > nextFrame:                         
        frame = (frame+1)%8                         
        nextFrame += 80                             

    if keyPressed("right"):
        changeSpriteImage(PersoSprite, 0*8+frame)    
        PersoPosx += 5
    elif keyPressed("down"):
        changeSpriteImage(PersoSprite, 1*8+frame)   
        PersoPosy += 5
    elif keyPressed("left"):
        changeSpriteImage(PersoSprite, 2*8+frame)    
        PersoPosx -= 5
    elif keyPressed("up"):
        changeSpriteImage(PersoSprite, 3*8+frame)
        PersoPosy -= 5
    elif keyPressed("escape"):
        pygame.quit()
    else:
        changeSpriteImage(PersoSprite, 1 * 8 + 5)  
   

    TableauPositions = LimiteScreen(PersoPosx,PersoPosy) #verifier si le joueur ne sort pas de l'écran
    PersoPosx = TableauPositions[0]
    PersoPosy = TableauPositions[1]
    moveSprite(PersoSprite,PersoPosx,PersoPosy,True)
  
    tick(120)

endWait()

## Boucle principale : gestion des évenements #############
# while True:
#     if clock()> nextFrame:
#         frame =(frame+1)%5
#         nextFrame +=80
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()  # Fermeture de la fenetre
#         elif event.type == KEYDOWN:          # Si on appuie sur une touche
#             if event.key == K_UP:  # si cette touche est "fleche haut"
#                 y -= 5
#             if event.key == K_RIGHT:
#                 x += 5
#                 changeSpriteImage(agent, 0*5+frame)
#             if event.key == K_LEFT:
#                 x -= 5
                
#                 changeSpriteImage(agent, 0*5+frame)
#             if event.key == K_ESCAPE:
#                 pygame.quit()
#         if event.type == MOUSEBUTTONDOWN:    # si on fait un clic souris
#             if event.button == 1:            # si c'est un clic gauche
#                 x, y = event.pos              # on recuoère la position du clic

#         ## Mise à joure de la flenetre avec perso #########
#         #on fait l'animation du perso
       



  
