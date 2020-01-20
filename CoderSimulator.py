# The program supports two main modes: multicolor and monochromatic
# The default preset is multicolor. To run the program in monochromatic
# mode, use '-m' argument in the command line.

import sys, argparse, signal
sys.setrecursionlimit(10**6)

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mono', help="The output will be monochromatic.", action='store_true')
args = parser.parse_args()
# print(args)
# print(MONOCHROMATIC)
MONOCHROMATIC = args.mono

def signal_handler(sig, frame):
    print('\nsys.exit(0)')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

if MONOCHROMATIC is False:
    from classes.colored.Coder import Coder
    coder = Coder()
    coder.start()
else:
    from classes.default.Coder import Coder
    coder = Coder()
    coder.start()