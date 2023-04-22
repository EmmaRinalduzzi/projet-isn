import pygame
from pygame.locals import *

#on utilise des drapeaux. C'est à dire des variables qui valent 0 ou 1 et qui permettent de déclencher des actions à l'aide de "si" : 

if Menu :  #si menu vaut 1

        #on crée un fond
        #fond = pygame.image.load("686fc664-cde4-4b03-b92f-4675314584f0.jpg").convert()

 

        #on sélectionne une police
        #font = pygame.font.SysFont('Helvetica', 24, bold=True)

        #on crée un rectangle de 100x20
        bouton1 = pygame.Surface((100, 20))

        #on le colorie

        couleur = (0, 200, 0)
        bouton1.fill(couleur)

        #on lui met le texte
               
        texte = font.render("JOUER", True, (0, 0, 0)) 
        bouton1.blit(texte, (0,0))

        #on affiche le fond et le bouton
        fenetre.blit(fond, (0, 0))
        fenetre.blit(bouton1, (320, 240))

 

        #ensuite il faut gérer les évenements
        
        for event in pygame.event.get():        #pour quitter la croix ou échappe
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                
                continuer = 0
            

            #on récupère la position du pointeur de la souris
            posPointeur = pygame.mouse.get_pos()

            #on récupère l'état des clicks de la souris (0,0,0) rien n'est cliqué (1,0,0) le click gauche est cliqué ...
            clicks= pygame.mouse.get_pressed()
            if clicks[0]==1 : #si le click gauche est cliqué

                #on regarde si la position du pointeur de la souris est dans le rectangle (320 et 240 étant les coordonées du coin supérieur gauche du bouton


                if 0<(posPointeur[0]-320) and (posPointeur[0]-320)<100 and posPointeur[1]-240<20 and 0<(posPointeur[1]-240) : 
                    print('click sur bouton')

                   #on change le drapeau Menu et on le met à 0 et le drapeau Jeu à 1 (par exemple) et a_propos à 0
                    Menu = 0
                    Jeu = 1
                    A_propos = 0
        
        
    if Jeu : #début de la boucle principale du jeu. On rentre dedans si Jeu vaut 1.
        fond = pygame.image.load("686fc664-cde4-4b03-b92f-4675314584f0.jpg").convert()
        perso1 = pygame.image.load("person.png").convert_alpha()