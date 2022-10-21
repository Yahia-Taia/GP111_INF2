__author__ = "Johvany Gustave"
__copyright__ = "Copyright 2022, GP111 - Grand Projet Informatique INF2, IPSA 2022"
__credits__ = ["Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Johvany Gustave"
__email__ = "johvany.gustave@ipsa.fr"

#DO NOT MODIFY THIS FILE!!!!!

from random import randint
import json
import numpy as np

FLAG_VALUE = 8

class Env():
    def __init__(self, filename):
        """ Constructor """
        self.players = [None, None]
        self.pose_tresor = [None, None]
        self.walls = []
        self.json_loaded = {}
        self.width = -1
        self.height = -1
        self.id = -1
        self.choose_map(filename)


    def choose_map(self, json_filename):
        """ Load a json file containing several environments and choose one of them randomly """
        with open(json_filename, "r") as file:
            self.json_loaded = json.load(file)

        self.id = randint(1, len(self.json_loaded))
        self.width = self.json_loaded["map"+str(self.id)]["width"]
        self.height = self.json_loaded["map"+str(self.id)]["height"]
        self.walls = self.json_loaded["map"+str(self.id)]["obstacles"]
        self.apply_symetry()


    def apply_symetry(self):
        """ Create automatically the symetry of the obstacles wrt the center of the map """
        self.map = np.zeros((self.height, self.width), dtype=np.int8)
        for [i, j] in self.walls:
            sym = self.width-1-j
            self.map[i, j] = 1
            self.map[i, sym] = 1
        x_c, y_c = int(self.width/2), int(self.height/2)
        self.map[y_c, x_c] = FLAG_VALUE


    def get_env(self):
        """ Return the 2D matrix representing the environment and its properties (width and height) """
        return {"width": self.width, "height": self.height, "map": self.map}
