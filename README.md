# Coder Simulator

### TL;DR:
A small program that simulates code writing process by generating and spewing out random lines of code in a semi-structured manner.

---

This program simulates coder's work by writing code indefinitely at a certain speed (can be specified as an argument). The program follows some general set of Python rules, such as matching indentations for try/catch blocks, or not unindenting after an empty function definition statement, etc. The code is generated randomly, which includes randomly generated variable names, function names, statements, if/else blocks, try/catch blocks, function definition blocks, as well as some in-built functions.

The program supports two output modes: colored and monochromatic. Colored mode highlights syntax of the program, as some IDEs would. Monochromatic mode would just stick to the default colors of the terminal window, which is used for running the program.

## Screenshots

Colored:

![alt text](./img/colored.jpg "Colored")

Monochromatic:

![alt text](./img/mono.jpg "Monochromatic")



## Requirements
1. Python 3
1. colorama (required only for the colored output mode)

    `pip install colorama`

## How To Run
In the project root directory:

`python CoderSimulator.py`

## Terminal arguments:

| Short | Long | Function |
| --- |--- | --- |
| -m | --mono | Runs in monochromatic mode |
| -s 200 | --speed 200 | Sets the speed. Default: 200. Min: 10. Max 10000. |

# Why?

Just looks nice. 😁 Start four instances of it, and all of a sudden you look like the baddest coder out there.