# The program supports two main modes: multicolor and monochromatic
# The default preset is multicolor. To run the program in monochromatic
# mode, use '-m' argument in the command line.

import sys, argparse, signal

def command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mono', help="The output will be monochromatic.", action='store_true')
    parser.add_argument('-s', '--speed', help="Sets the speed of typing the text out. Default: 200. Minimum: 10. Maximum: 10000")
    args = parser.parse_args()
    # print(args)
    # print(MONOCHROMATIC)
    monochromatic = args.mono
    speed = args.speed
    if speed is None:
        speed = 200
    try:
        speed = int(speed)
        if speed < 10 or speed > 10000:
            raise ValueError
    except:
        print('Bad speed value. Speed should be in the interval [10, 10000].')
        print('Terminating.')
        sys.exit(1)
    return (monochromatic, speed)

def signal_handler(sig, frame):
    # print('\nsys.exit(0)')
    sys.exit(0)

def main():
    arguments = command_line_arguments()
    monochromatic, speed = arguments
    if monochromatic is False:
        from classes.colored.Coder import Coder
    else:
        from classes.default.Coder import Coder
    coder = Coder(speed)
    coder.start()

# Since the main method is invoked recursively forever,
# Python recursion limit has to be increased
sys.setrecursionlimit(10**6)

# Set up Ctrl + C interrupt handler
signal.signal(signal.SIGINT, signal_handler)

# Start the simulator
main()