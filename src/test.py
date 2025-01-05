from Magazine import Magazine
import numpy as np
from Ware import Ware

def check_magazine():
    matrix = np.empty((3, 3))
    wares = [[0, 25, 52], [1, 762, 55], [2, 242, 32415], [3, 2345, 5546]]
    wares = [Ware(ware[0], ware[1], ware[2]) for ware in wares]
    magazine = Magazine(matrix=matrix)
    wares = magazine.generateMagazineWares(wares)
    for ware in wares:
        print(ware)


if __name__ == '__main__':
    check_magazine()