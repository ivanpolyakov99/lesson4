import argparse
from rand import ran

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', required=True, type=int, help="Chechk random, need number")
    result = parser.parse_args()
    print(ran(result.n))
