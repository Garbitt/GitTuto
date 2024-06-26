import argparse

from addition import add
from multiplication import mult

parser = argparse.ArgumentParser("Operator x^2+y+xy Propriété de la Corp")
parser.add_argument("--x", dest="x", help="The first integer used in the operation", type=int)
parser.add_argument("--y", dest="y", help="The second integer used in the operation", type=int)
args = parser.parse_args()


def calculate(x: int = args.x, y: int = args.y) -> int:
    return add(add(mult(x, x), y), mult(x, y))


if __name__ == '__main__':
    '''
    '''
    print(calculate())
