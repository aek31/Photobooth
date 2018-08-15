from picamera import PiCamera, Color
from time import sleep
from fractions import Fraction
import pygame
from gpiozero import Button
import os, sys, time


# ATTENTION : CLE USB A FORMATTER EN EXT4 + créer dossier "Photobooth" dans la racine du dossier (il faut 
# media/pi/cle_photos/Photobooth/ pour que ca fonctionne ou sinon renomer cette ligne pour que ca corresponde à la clé USB


button = Button(17)  # Bouton relie au GPIO 17
Numeral = ""
done = False

#initialise pygame
pygame.init()
screen = pygame.display.set_mode((1640, 922),pygame.FULLSCREEN)
background = pygame.Surface(screen.get_size())
background = background.convert()

# rend invisible le curseur de souris
pygame.mouse.set_visible(0)


def UpdateDisplay_vide():
    global Numeral # variable de chiffre de decompte
    Numeral = ""
    background.fill(pygame.Color("black"))
    # initialisation du chiffre 3,2,1
    font = pygame.font.Font(None, 300)
    font_surf = font.render(Numeral, 1, (62,246,19))
    font_rect = font_surf.get_rect()
    font_rect.left = 25
    font_rect.top = 1
    background.blit(font_surf, font_rect)
    screen.blit(background, (0,0))
    pygame.display.flip()
    return


def UpdateDisplay_decompteur():
    global Numeral # variable de chiffre de decompte
    
    # Reglage transparance pour afficher le 3,2,1
    # Transparency allows pigame to shine through ok 120
    camera.preview_alpha = 190
        
    background.fill(pygame.Color("black"))

    # initialisation du chiffre 3,2,1
    font = pygame.font.Font(None, 1200)
    font_surf = font.render(Numeral, 1, (62,246,19))
    #font_surf = font.render(Numeral, 1, (255,0,0))
    font_rect = font_surf.get_rect()
    font_rect.left = 600
    font_rect.top = 0
    background.blit(font_surf, font_rect)
    screen.blit(background, (0,0))
    #carre qui entoure le nombre
    #pygame.draw.rect(screen,pygame.Color("green"),(10,10,140,200),2) 
    pygame.display.flip()

    return

def UpdateCamera():              # parametre affichage 
    camera.vflip = False
    camera.hflip = True
    camera.rotation = 0

    #luminosite a garder a 50, si plus pose probleme avec lumiere
    camera.brightness = 50

    # mode auto d'exposition, avec lumiere ca ne change pas grand chose
    #camera.exposure_mode = 'auto'
    #camera.contrast = 8
    camera.resolution = (1640,922)

    return

def CanevasPhoto():

    #haut gauche
    pygame.draw.rect(screen, (62, 246, 19), pygame.Rect(0, 0, 300, 5))
    pygame.draw.rect(screen, (62, 246, 19), pygame.Rect(0, 0, 5, 300))

    #haut droit
    pygame.draw.rect(screen, (62, 246, 19), pygame.Rect(1635, 0, -300, 5))
    pygame.draw.rect(screen, (62, 246, 19), pygame.Rect(1635, 0, 5, 300))

    #bas gauche
    pygame.draw.rect(screen, (62, 246, 19), pygame.Rect(0, 918, 300, 5))
    pygame.draw.rect(screen, (62, 246, 19), pygame.Rect(0, 918, 5, -300))

    
    #bas droit
    pygame.draw.rect(screen, (62, 246, 19), pygame.Rect(1635, 918, -300, 5))
    pygame.draw.rect(screen, (62, 246, 19), pygame.Rect(1635, 921, 5, -300))

    
    #OVERLAY CAPTIONS AS TEXT
    text = "Chic Guinguette Chic - 30 ans"
    font = pygame.font.Font(None, 60)
    font_surf = font.render(text, 1, (62,246,19))
    font_rect = font_surf.get_rect()
    font_rect.left = 530
    font_rect.top = 850
    screen.blit(font_surf, font_rect)
    pygame.display.update()

    sleep(5)
    
    return




while(True):

    # Verification que la cle USB est montee et creation du dossier Photobooth sur la cle
    #usbcheck = False
    #rootdir = '/media/'

    #while not usbcheck:
    #    dirs = os.listdir(rootdir)
    #    for file in dirs:
    #        folder = os.path.join(rootdir,file)
    #        if not file == 'SETTINGS' and os.path.isdir(folder):
    #            usbcheck = True
    #            imagedrive = os.path.join(rootdir,file)
    #            imagefolder = os.path.join(imagedrive,'PhotoBooth')
                #If a photobooth folder on the usb doesn't exist create it
    #            if not os.path.isdir(imagefolder):
    #                os.makedirs(imagefolder)

    
        
    #Initialise the camera object
    camera = PiCamera()

    # Parametres de la camera 
    UpdateCamera()

    # Visualisation de la camera tant que le bouton n'a pas ete appuye
    camera.start_preview()
    
    while not done:
    
        # Bouton appuye, decompte puis prise de la photo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            exit()
        if button.is_pressed:
            for i in range(3, 0, -1):
                Numeral = "%s" % i
                UpdateDisplay_decompteur()
                sleep(1)
                
            UpdateDisplay_vide()



            
            # variale vaut la date du jour
            fname = (time.strftime("%d%b%y_%H:%M:%S"))
            variable = fname + ".jpg"
            
            # enregistrement de l'image
            #camera.capture(os.path.join(imagefolder,variable))
            camera.capture(os.path.join('/media/pi/cle_photos/Photobooth/',variable))
            camera.stop_preview()
            

            # ICI faire un updatedisplay vide sans texte et bord pour effecer le "1" et carre  qui restent trop longtemps
            #UpdateDisplay_vide()
    
            # ecran noir
            img = pygame.image.load('/home/pi/Documents/Tests/noir.jpg')
            screen.blit(img, (0, 0))
            pygame.display.flip()    # update l'affiche de la photo
            sleep(0.3)

            # ici mettre code led flash en meme temps que l'ecran noir
    
            # affiche pendant 5 secondes l'image
            img = pygame.image.load(os.path.join('/media/pi/cle_photos/Photobooth/',variable))
            screen.blit(img, (0, 0))

            
            # Incruste des textes et dessins sur la photo affichee
            CanevasPhoto()

            # On redemarre la camera
            camera.start_preview()
            

