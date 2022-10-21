__author__ = "Johvany Gustave"
__copyright__ = "Copyright 2022, GP111 - Grand Projet Informatique INF2, IPSA 2022"
__credits__ = ["Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Johvany Gustave"
__email__ = "johvany.gustave@ipsa.fr"


class Move:
    def __init__(self, type, value=-1):
        self.type = type
        self.value = value


#---------------------------------------------------------------------------#
class Bot:  #(DO NOT TOUCH!)
    def __init__(self):
        self.allowed_moves = {"do_nothing": 0, "move_left": 1, "move_right": 2, "move_up": 3, "move_down": 4}   #dictionnaire contenant les differents coups possibles

    def play(self):
        pass


#---------------------------------------------------------------------------#
class DoNothing(Bot):
    """ Le personnage restera sur place a chaque iteration """
    def __init__(self):
        super().__init__()  #Initialisation de la classe mere
    
    def play(self):
        pass
        #TODO


#---------------------------------------------------------------------------#
class ManualMove(Bot):
    """ Le personnage sera controle par le joueur """
    def __init__(self):
        super().__init__()

    def play(self):
        pass
        #TODO


#---------------------------------------------------------------------------#
class RandomMove(Bot):
    """ Le personnage se deplacera de maniere aleatoire dans le labyrinthe tout en evitant les obstacles """
    def __init__(self):
        super().__init__()
    
    def set_config(self, env, pose):
        """ Get the current map to explore, the agent and target poses """
        self.x, self.y = pose   #coordonnees (x,y) de la case sur laquelle se trouve actuellement le personnage
        self.width_map, self.height_map, self.map = env["width"], env["height"], env["map"] #largeur et hauteur du labyrinthe. La matrice 2D representant le labyrinthe est egalement fournie

    def play(self):
        pass
        #TODO


#---------------------------------------------------------------------------#
class SmartMove(Bot):
    """Agent implementing the classic A* algorithm"""
    def __init__(self):
        Bot.__init__(self)
        self.move = Move("do_nothing")

    
    def set_config(self, env, start):
        """ Get the current map to explore, the agent and target poses """
        self.x, self.y = start
        self.width_map, self.height_map, self.map = env["width"], env["height"], env["map"]


    def play(self):
        pass
        #TODO