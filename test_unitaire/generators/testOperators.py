import pandas as pd
from pathlib import Path
import random


def generateTestOperators(pathFile: Path):
    cols = ['x', 'y', 'res_add', 'res_mult', 'res_calculate']
    simulations = []
    for _ in range(100):
        x = random.randint(0,100)
        y = random.randint(0,100)
        simulations.append([x, y, x+y, x*y, x**2+y+x*y])
    res = pd.DataFrame(data=simulations, columns=cols)
    res.to_csv(pathFile, sep=',', index=False)


if __name__ == '__main__':
    path = Path('../testOperators.csv')
    generateTestOperators(path)
