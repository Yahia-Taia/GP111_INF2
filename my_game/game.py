__author__ = "Johvany Gustave"
__copyright__ = "Copyright 2022, GP111 - Grand Projet Informatique INF2, IPSA 2022"
__credits__ = ["Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Johvany Gustave"
__email__ = "johvany.gustave@ipsa.fr"

#DO NOT MODIFY THIS FILE!!!!!

import os
import numpy as np
from random import randrange, randint

if __name__ == "__main__":
    from env import Env
else:
    from .env import Env

maps_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "env", "maps.json")


class Game:
    def __init__(self, random_pose=False):
        self.env = Env(maps_file).get_env()
        self.allowed_moves = {"do_nothing": 0, "move_left": 1, "move_right": 2, "move_up": 3, "move_down": 4}
        self.victory_rule = {"win": 2, "defeat": -2, "continue": -1}
        self.__init_player(random=random_pose)

    
    def __init_player(self, random=False):
        if random:
            cell_zeros = np.argwhere(self.env["map"]==0)
            pose = cell_zeros[randrange(0, cell_zeros.shape[0])]
        else:
            side = randint(0, 1)
            if side == 0:
                pose = (self.env["height"]//2, 0)
            else:
                pose = (self.env["height"]//2, self.env["width"]-1)

        self.player_pose = [pose[1], pose[0]]
        self.player_state = self.victory_rule["continue"]

    
    def get_player_info(self):
        return {"pose": self.player_pose, "state": self.player_state}

    
    def get_env(self):
        return self.env

    
    def process(self, move):
        if move.type == self.allowed_moves["move_left"]:
            self.__move_left()
        elif move.type == self.allowed_moves["move_right"]:
            self.__move_right()
        elif move.type == self.allowed_moves["move_up"]:
            self.__move_up()
        elif move.type == self.allowed_moves["move_down"]:
            self.__move_down()
        else:
            self.__do_nothing()
        self.__check_win()
    

    def __move_left(self):
        self.player_pose[0] -= 1
        if self.player_pose[0] < 0:
            self.player_pose[0] = self.env["width"] - 1
    

    def __move_right(self):
        self.player_pose[0] += 1
        if self.player_pose[0] == self.env["width"]:
            self.player_pose[0] = 0

    
    def __move_up(self):
        self.player_pose[1] -= 1
        if self.player_pose[1] < 0:
            self.player_pose[1] = self.env["height"] - 1
    

    def __move_down(self):
        self.player_pose[1] += 1
        if self.player_pose[1] == self.env["height"]:
            self.player_pose[1] = 0


    def __do_nothing(self):
        pass


    def __check_win(self):
        if self.env["map"][self.player_pose[1], self.player_pose[0]] == 1:
            self.player_state = self.victory_rule["defeat"]
        elif self.env["map"][self.player_pose[1], self.player_pose[0]] == 8:
            self.player_state = self.victory_rule["win"]



#******************************************************************
if __name__ == "__main__":
    game = Game()
    print(game.env)
