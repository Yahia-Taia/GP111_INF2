__author__ = "Johvany Gustave"
__copyright__ = "Copyright 2022, GP111 - Grand Projet Informatique INF2, IPSA 2022"
__credits__ = ["Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Johvany Gustave"
__email__ = "johvany.gustave@ipsa.fr"

#Importation de modules externes
import pygame
import os

#Importation du module du meme package
from .colors import *   

img_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "img")   #chemin complet pour acceder au sous-dossier 'img' dans lequel se trouvent les images utilisees dans le jeu


class ItemPicture:  #(NE PAS TOUCHER!)
    """ Classe Mere contenant les elements necessaires pour charger une image """
    def __init__(self, x, y, size, filename):
        self.x, self.y = x, y   #coordonnees desirees (x, y) de l'image
        self.size = size    #taille (en pixel) de l'image (image carre)
        self.filename = filename    #Chemin menant a l'image a charger
        self.load_img() #chargement de l'image
        self.rect = self.img.get_rect().move(self.x, self.y)    #positionnement de l'image
    
    def set_pose(self, pose):
        """ Update the pose of the image """
        self.x, self.y = pose
        self.rect = self.img.get_rect().move(self.x, self.y)
    
    def load_img(self):
        """ Load the image """
        self.img = pygame.image.load(self.filename).convert()
        self.img.set_colorkey(BLACK)
        self.img = pygame.transform.scale(self.img, (self.size, self.size)) #redimmensionnement de l'image
    
    def draw(self, screen):
        """ Draw the image on the screen """
        screen.blit(self.img, self.rect)    #Affichage de l'image dans la fenetre de jeu


class Wall(ItemPicture):
    """ Class that inherits from the ItemPicture class. It allows you to load the image used to represent the walls """
    def __init__(self, x, y, size, filename=f"{img_folder}/wall.png"):
        super().__init__(x, y, size, filename)


class Agent(ItemPicture):
    """ Class that inherits from the ItemPicture class. It allows you to load the image used to represent the agent """
    def __init__(self, x, y, size, filename=f"{img_folder}/pirate.png"):
        super().__init__(x, y, size, filename)


class Treasure(ItemPicture):
    """ Class that inherits from the ItemPicture class. It allows you to load the image used to represent the treasure """
    def __init__(self, x, y, size, filename=f"{img_folder}/treasure.png"):
        super().__init__(x, y, size, filename)


class Text: #(NE PAS TOUCHER!)
    """ This class allows you to define text to display in the game window """
    def __init__(self, content, x, y, font_size=30, color=BLACK, is_bold=False):
        self.content = content
        self.x, self.y = x, y
        self.color = color
        self.font_text = pygame.font.SysFont("arial", font_size, bold=is_bold)  #Vous pouvez changer la police
    
    def draw(self, screen):
        """ Display the text in the """
        text = self.font_text.render(self.content, True, self.color)
        screen.blit(text, text.get_rect(center=(self.x, self.y)))

    def set_content(self, content):
        self.content = content