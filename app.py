__author__ = "Johvany Gustave"
__copyright__ = "Copyright 2022, GP111 - Grand Projet Informatique INF2, IPSA 2022"
__credits__ = ["Johvany Gustave"]
__license__ = "Apache License 2.0"
__version__ = "1.0.0"
__maintainer__ = "Johvany Gustave"
__email__ = "johvany.gustave@ipsa.fr"

from my_game.player import Player
from my_game.game import Game
from time import sleep
from threading import Thread


def thread_function(p, g):
    """ 
        Function that runs in background when step 1 of the project has been validated by the teacher
        In this function, the game handler gets the player move through and update its state and pose accordingly.
        Then, the game window is updated.
        Once the game is over (wall hit or treasure found), a final display appears on the game window.
        3 seconds later, the game is completely stopped.
    """
    while p.state == g.victory_rule["continue"]:
        g.process(p.bot.play())
        p.set_player_info(g.get_player_info())
        
        #TODO: some instructions might be missing here for the random and smart moves

        sleep(1.0)

    p.final_display()
    sleep(3)
    p.gui.running = False


if __name__ == "__main__":
    import os
    if os.name == "nt": #if you are on Windows
        screen_resolution_to_fix = False  #Set this boolean to True if you face window resolution issues
        if screen_resolution_to_fix:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)  #Resolve the window resolution issue
    
    game = Game()   #Creation d'une instance de la classe Game, elle gere le fonctionnenement du jeu
    player = Player(game.get_player_info(), game.get_env(), name="Jack", mode="do_nothing") #Creation d'une instance de la classe Player, elle permet de controler le comportement du personnage

    #TODO : Decommenter les 2 lignes suivantes uniquement apres validation de l'etape 1!
    # t = Thread(target=thread_function, daemon=True, args=(player, game))
    # t.start()
    
    try:
        while player.gui.running:   #Tant que la partie n'est pas finie ou que le joueur ne ferme pas la fenetre de jeu
            player.gui.on_render()  #On rafraichit la fenetre de jeu
    except KeyboardInterrupt:
        print("Ctrl+C pressed, shutting down the process...")
    finally:
        player.gui.on_cleanup()
