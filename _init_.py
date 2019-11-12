__author__ = "Antoine Balouka, Lola Josseran, Marion Rault, Diana Ren, Coni Soret"

from cp2048 import Game2048
from evaluate import evaluate_strategy 
from strat_finale import strategy_2048

print(list(evaluate_strategy(strategy_2048)))