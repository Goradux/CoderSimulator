# The program supports two output modes: multicolor and monochromatic
# The default is set to multicolor.
# To run the program in monochromatic mode:
# python CoderSimulator.py -m
# To specify speed of typing out the text (between 10 and 10000), run:
# python CoderSimulator.py -s 200

import sys, argparse, signal


def command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mono', help="The output will be monochromatic.", action='store_true')
    parser.add_argument('-s', '--speed', help="Sets the speed of typing the text out. Default: 200. Minimum: 10. Maximum: 10000.")
    args = parser.parse_args()
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
    return monochromatic, speed


def signal_handler(sig, frame):
    # print('\nsys.exit(0)')
    sys.exit(0)


def main():
    monochromatic, speed = command_line_arguments()
    if monochromatic is False:
        from classes.colored.Coder import Coder
    else:
        from classes.default.Coder import Coder
    coder = Coder(speed)
    coder.start()


# Set up Ctrl + C interrupt handler
signal.signal(signal.SIGINT, signal_handler)


# Start the simulator
main()