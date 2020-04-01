## Initialisation ###########################################
import pygame
from pygame.locals import *
from pygame_functions import * 
pygame.init()
fenetre = pygame.display.set_mode((640, 480))
TITLE = "message emma"
pygame.display.set_caption(TITLE)
#rectScreen = fenetre.get_rect()  # coordonnée du rectangle de l'écran
#############################################################
## Gestion de la musique ####################################
pygame.mixer.pre_init(44100, 4096)
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
  ################################ on fait l'animation du perso
#  walkright = pygame.image.load('personnage0D.png'), pygame.image.load('personnage1D.png'),pygame.image.load('personnage2D.png'),pygame.image.load('personnage3D.png'),pygame.image.load('personnage4D.png')
 # walkleft = pygame.image.load('personnage0G.png'),pygame.image.load('personnage1G.png'),pygame.image.load('personnage2G.png'),pygame.image.load('personnage3G.png'),pygame.image.load('personnage4G.png'),
# agent = makeSprite("personnage0D.jpg")
# addSpriteImage (agent, "personnage0D.jpg")
# addSpriteImage (agent, "personnage1D.jpg")
# addSpriteImage (agent, "personnage2D.jpg")
# addSpriteImage (agent, "personnage3D.jpg")
# addSpriteImage (agent, "personnage4D.jpg")
# addSpriteImage (agent, "alaid.jpg")
# addSpriteImage (agent, "personnage1G.jpg")
# addSpriteImage (agent, "personnage2G.jpg")
# addSpriteImage (agent, "personnage3G.jpg")
# addSpriteImage (agent, "personnage4G.jpg")
#pygame.sprite

screenSize(640, 480)
PersoSprite  = makeSprite("links.gif", 32)  # links.gif contains 32 separate frames of animation.
setBackgroundImage("image.jpg")

#################################### Gestion de la police####   
# police = pygame.font.Font(None, 24)
# texte = police.render(
#     "Flèche du haut pour monter, bouton gauche pour placer ou on veut", True, pygame.Color("#FFFF00"))
# rectTexte = texte.get_rect()
# donne au centre du rectangle contenant le texte, les coordonnées du centre de l'écran
#rectTexte.center = rectScreen.center

#############################################################
## On pose le FondSprite ##########################################

############################################################
## Initialisation du perso #################################
#perso = pygame.image.load('perso.png').convert_alpha()
PersoPosx = 320
PersoPosy = 320
###########################################################

# setBackgroundColour("pink")
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
   
    if PersoPosx >= 640 :
        PersoPosx = 640
    if PersoPosx <=30:
        PersoPosx = 30


    #fenetre.blit(PersoSprite, (x, y))
    #pygame.display.flip()
    moveSprite(PersoSprite,PersoPosx,PersoPosy,True)
    # fenetre.fill(pygame.Color("#FF0000"))
    #fenetre.blit(texte, rectTexte)
  
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
       



  
