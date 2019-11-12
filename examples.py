import numpy
import random

from module.cp2048 import Game2048, GameOverException
from module.strat_finale import strategy_2048


def test_strategy(fct_strategy, ntries=10):
    liste=[]
    for i in range(0, ntries):
        g = Game2048()
        while True:
            try:
                g.next_turn()
                #print(g.game)
            except (GameOverException, RuntimeError):
                break
            d = fct_strategy(g.game, g.moves)
            #print('choix:',d)
            g.play(d)
        yield g.score()
        liste.append(numpy.max(g.game))
        print(g.game)
    print(max(liste),"4096:",liste.count(4096),"2048:",liste.count(2048),"1024:",liste.count(1024),"512:",liste.count(512),"256:",liste.count(256),"128:",liste.count(128),"64:",liste.count(64),"32:",liste.count(32),"16:",liste.count(16))
    
scores = list(test_strategy(strategy_2048))