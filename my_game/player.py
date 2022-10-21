__author__ = "Johvany Gustave"
__copyright__ = "Copyright 2022, GP111 - Grand Projet Informatique INF2, IPSA 2022"
__credits__ = ["Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Johvany Gustave"
__email__ = "johvany.gustave@ipsa.fr"

#Importation des modules du meme package
from .gui import GUI
from .bot import ManualMove, RandomMove, DoNothing, SmartMove


class Player:
    def __init__(self, player_info, env, name="Player", mode="do_nothing"): #(DO NOT TOUCH!)
        """ Constructor of the class """
        self.name = name
        self.mode = mode
        self.env = env
        self.pose = player_info["pose"] #position du personnage (x, y)
        self.state = player_info["state"]   #continue, victory or defeat
        self.victory_rule = {"win": 2, "defeat": -2, "continue": -1}

        self.init_bot(mode)
        if mode in ["astar", "random"]:
            self.bot.set_config(env, self.pose)

        self.gui = GUI(self.pose, env, name)
        self.gui.on_init()

    
    def init_bot(self, mode):   #(DO NOT TOUCH!)
        """ Load the proper bot according to the mode selected by the player """
        if mode == "do_nothing":
            self.bot = DoNothing()
        elif mode == "manual":
            self.bot = ManualMove()
        elif mode == "random":
            self.bot = RandomMove()
        elif mode == "astar":
            self.bot = SmartMove()

    
    def set_player_info(self, info):    #(DO NOT TOUCH!)
        """ Set the pose and the state of the player """
        self.pose = info["pose"]
        self.state = info["state"]
        self.gui.set_player_pose(self.pose)

    
    def final_display(self):    #(DO NOT TOUCH!)
        """ Run the final GUI display to indicate whether or not the player won """
        if self.state == self.victory_rule["win"]:
            self.gui.set_player_state("victory")
        else:
            self.gui.set_player_state("defeat")
        self.gui.mode = "final"