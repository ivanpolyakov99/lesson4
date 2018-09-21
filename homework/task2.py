import argparse
from circle import sqc
from triangle import sqt
from rectangle import sqr

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-figure', required=True, type=str, help="circle / triangle / rectangle")
    parser.add_argument('-r', type=float, help="Radius of circle")
    parser.add_argument('-a', type=float, help="1st side of triangle")
    parser.add_argument('-b', type=float, help="2nd side of triangle")
    parser.add_argument('-c', type=float, help="3rd side of triangle")
    parser.add_argument('-len', type=float, help="Length of rectangle")
    parser.add_argument('-wid', type=float, help="Width of rectangle")
    result = parser.parse_args()
    if result.figure == 'circle':
        print("Square of circle:", str(sqc(result.r)))
    elif result.figure == 'triangle':
        print("Square of triangle:", str(sqt(result.a, result.b, result.c)))
    elif result.figure == 'rectangle':
        print("Square of rectangle:", str(sqr(result.len, result.wid)))
        
