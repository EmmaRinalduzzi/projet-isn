## Initialisation ###########################################
import pygame
from pygame.locals import *
pygame.init()
fenetre = pygame.display.set_mode((640, 480))
TITLE = "message emma"
pygame.display.set_caption(TITLE)
rectScreen = fenetre.get_rect()  # coordonnée du rectangle de l'écran
#############################################################
## Gestion de la musique ####################################
pygame.mixer.pre_init(44100, 4096)
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(2)
pygame.mixer.music.play(-1)
####################################Gestion de la police####
police = pygame.font.Font(None, 24)
texte = police.render(
    "Flèche du haut pour monter, bouton gauche pour placer ou on veut", True, pygame.Color("#FFFF00"))
rectTexte = texte.get_rect()
# donne au centre du rectangle contenant le texte, les coordonnées du centre de l'écran
rectTexte.center = rectScreen.center

#############################################################
## On pose le fond ##########################################
fond = pygame.image.load('image.jpg').convert()
fenetre.blit(fond, (0, 0))
pygame.display.flip()
############################################################
## Initialisation du perso #################################
perso = pygame.image.load('perso.png').convert_alpha()
x = 320
y = 320
###########################################################
## Boucle principale : gestion des évenements #############
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  # Fermeture de la fenetre
        elif event.type == KEYDOWN:          # Si on appuie sur une touche
            if event.key == K_UP:  # si cette touche est "fleche haut"
                y -= 5
            if event.key == K_ESCAPE:
                pygame.quit()
        if event.type == MOUSEBUTTONDOWN:    # si on fait un clic souris
            if event.button == 1:            # si c'est un clic gauche
                x, y = event.pos              # on recuoère la position du clic

        ## Mise à joure de la flenetre avec perso #########

        fenetre.blit(fond, (0, 0))
        fenetre.blit(perso, (x, y))
        # fenetre.fill(pygame.Color("#FF0000"))
        fenetre.blit(texte, rectTexte)

        pygame.display.flip()
