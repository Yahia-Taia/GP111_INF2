__author__ = "Johvany Gustave"
__copyright__ = "Copyright 2022, GP111 - Grand Projet Informatique INF2, IPSA 2022"
__credits__ = ["Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Johvany Gustave"
__email__ = "johvany.gustave@ipsa.fr"

#Importation d'un module externe
import pygame

#Importation du module du meme package
from .colors import *
from .items import Wall, Agent, Treasure, Text, img_folder


class GUI:
    def __init__(self, player_pose, env, player_name, fps=30, cell_size=35):
        """ Constructor of the class """
        self.cell_size = cell_size  #taille d'une case en pixel (NE PAS TOUCHER!)
        self.fps = fps  #nombre d'images par secondes dans la fenetre de jeu (NE PAS TOUCHER!)
        self.clock = pygame.time.Clock()    #variable utilisee afin de gerer le nombre de FPS dans la fenetre de jeu (NE PAS TOUCHER!)
        self.env = env  #l'environnement genere par le jeu est stocke dans cette variable (NE PAS TOUCHER!)
        self.player_pose = player_pose  #coordonnees (x,y) de la case sur laquelle se trouve actuellement le personnage (NE PAS TOUCHER!)
        self.right_panel_width = 300    #Largeur (en pixel) du paneau lateral droit de la fenetre de jeu
        self.screen_res = (self.env["width"]*self.cell_size + self.right_panel_width, self.env["height"]*self.cell_size + 20)   #resolution de la fenetre de jeu (en pixel)
        self.offset = 10    #Marges (en pixel) de la fenetre graphique
        self.inc = 0    #Nombre de movements realises par le personnage durant la partie (NE PAS TOUCHER!)
        self.player_state = "continue"  #etat actuel du personnage (NE PAS TOUCHER!)
        self.player_name = player_name  #nom du joueur (NE PAS TOUCHER!)
        self.mode = "party" #party: le jeu est en cours, final: affichage du message de fin (message de victoire ou de defaite) (NE PAS TOUCHER!)
        self.path = []

    
    def on_init(self):
        """ Initialize all the pygame stuffs """
        pygame.init()   #initialisation de pygame (NE PAS TOUCHER!)
        self.screen = pygame.display.set_mode(self.screen_res)  #creation de la fenetre de jeu avec une certaine resolution (NE PAS TOUCHER!)
        pygame.display.set_icon(pygame.image.load(img_folder + "/icon.png"))    #chargement de l'icone de la fentre de jeu
        pygame.display.set_caption("GP111 - Find the treasure") #titre de la fenetre de jeu
        self.running = True #Booleen indiquant si la partie est toujours en cours (NE PAS TOUCHER!)
        self.agent = Agent(self.player_pose[0]*self.cell_size + self.offset, self.player_pose[1]*self.cell_size + self.offset, self.cell_size)  #personnage (NE PAS TOUCHER!)
        self.player_name_text = Text(f"{self.player_name}", self.env["width"]*self.cell_size + self.right_panel_width//2 + self.offset, self.screen_res[1]//4, font_size=40, is_bold=True)  #texte contenant le nom du joueur, il sera affiche dans la fenetre de jeu
        self.cpt_text = Text(f"Moves: {self.inc}", self.env["width"]*self.cell_size + self.right_panel_width//2 + self.offset, self.screen_res[1]*3//4, font_size=40)   #texte contenant le nombre de coups realise par le personnage, il sera affiche dans la fenetre de jeu
        self.victory_text = Text("Congrats, you found the treasure!", self.screen_res[0]//2, self.screen_res[1]//2, color=GREEN, font_size=50, is_bold=True)    #texte contenant le message de victoire, il sera affiche en fin de partie si le joueur a gagne
        self.defeat_text = Text("Game over: you hit a wall...", self.screen_res[0]//2, self.screen_res[1]//2, color=RED, font_size=50, is_bold=True)    #texte contenant le message de defaite, il sera affiche en fin de partie si le joueur a perdu
        self.update_items() #positionnement des murs dans la fentre de jeu (NE PAS TOUCHER!)


    def on_event(self, event): #(NE PAS TOUCHER!)
        """ Check if the pygame window has been closed by the user """
        if event.type == pygame.QUIT:   #si le joueur ferme la fenetre de jeu
            self.running = False    #le jeu s'arrete 


    def on_cleanup(self):   #(NE PAS TOUCHER!)
        """ Properly stops pygame """
        pygame.event.pump()
        pygame.quit()

    
    def on_render(self):    #(NE PAS TOUCHER!)
        """ Method to call periodically to update the display """
        for event in pygame.event.get():    #gestion des evenements
            self.on_event(event)    
        self.draw() #mise a jour de la fenetre de jeu
        self.clock.tick(self.fps)   #permet de gerer le nombre de FPS du jeu


    def draw(self):
        """ Draw the adequate items based on the game state """
        if self.mode == "party":    #si la partie n'est pas finie (le tresor n'a pas encore ete trouve et le personnage n'est pas rentre dans un mur)
            self.screen.fill(BG_COLOR)  #couleur d'arriere plan de la fenetre de jeu

            #Trace de diverses formes
            pygame.draw.rect(self.screen, WHITE, (0, 0, self.env["width"]*self.cell_size + 2*self.offset, self.env["height"]*self.cell_size + 2*self.offset))   #rectangle plein (en blanc) correspondant a la couleur d'arriere plan du labyrinthe
            pygame.draw.rect(self.screen, BLACK, (0, 0, self.env["width"]*self.cell_size + 2*self.offset, self.env["height"]*self.cell_size + 2*self.offset), width=5)  #rectangle vide (en noir) faisant office de bordures du labyrinthe
            pygame.draw.line(self.screen, BLACK, (self.env["width"]*self.cell_size + 2*self.offset, (self.env["height"]*self.cell_size + self.offset) // 2), (self.env["width"]*self.cell_size + 2*self.offset + self.right_panel_width, (self.env["height"]*self.cell_size + self.offset) // 2), width=5)  #ligne horizontale presente sur la partie droite de la fenetre de jeu
            
            #Trace des murs (NE PAS TOUCHER!)
            for wall in self.walls:
                wall.draw(self.screen)
            self.treasure.draw(self.screen)

            for node in self.path:  #Trace du chemin
                pygame.draw.circle(self.screen, GREEN, (node[0]*self.cell_size + self.offset + self.cell_size//2, node[1]*self.cell_size + self.offset + self.cell_size//2), self.cell_size//4)
           
            self.agent.draw(self.screen)    #Affichage du personnage    (NE PAS TOUCHER!)
            self.cpt_text.draw(self.screen) #Affichage du nombre de coups realises par le personnage
            self.player_name_text.draw(self.screen) #Affichage du nom du joueur

        else:   #si le joueur a gagne ou perdu
            self.screen.fill(WHITE) #couleur d'arriere plan de la fenetre de jeu

            if self.player_state == "victory":  #si le joueur a gagne
                self.victory_text.draw(self.screen) #Affichage du message de victoire
            elif self.player_state == "defeat": #si le joueur a perdu
                self.defeat_text.draw(self.screen)  #Affichage du message de defaite

        pygame.display.update() #Mise a jour de la fenetre de jeu. Il s'agit de la derniere instruction de cette fonction !(NE PAS TOUCHER!)
    
    
    def set_player_pose(self, pose):
        """ Update the position of the player and the number of moves made """
        self.player_pose = pose #mise a jour de la position du personnage
        self.agent.set_pose((self.player_pose[0]*self.cell_size + self.offset, self.player_pose[1]*self.cell_size + self.offset))   #Deplacement du personnage dans la fenetre de jeu (NE PAS TOUCHER!)
        self.inc += 1   #Mise a jour du nombre de coups realises par le personnage
        self.cpt_text.set_content(f"Moves: {self.inc}") #Mise a jour du texte contenant le nombre de coups realises par le personnage


    def set_player_state(self, state):  #(NE PAS TOUCHER!)
        """ Update the player's state """
        self.player_state = state


    def update_items(self): #(NE PAS TOUCHER!)
        """ Update the environment """
        self.walls = []
        for row in range(self.env["height"]):
            for col in range(self.env["width"]):
                if self.env["map"][row, col] == 1:
                    self.walls.append(Wall(col*self.cell_size + self.offset, row*self.cell_size + self.offset, self.cell_size))
                elif self.env["map"][row, col] == 8:
                    self.treasure = Treasure(col*self.cell_size + self.offset, row*self.cell_size + self.offset, self.cell_size)