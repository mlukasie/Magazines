from Magazine import Magazine
import numpy as np
from Ware import Ware

def check_magazine():
    vertices = [(1, 1), (1, 4), (0, 4), (0, 5), (5, 5), (5, 1)]
    magazine = Magazine(vertices=vertices)
    print(magazine.matrix)


if __name__ == '__main__':
    check_magazine()