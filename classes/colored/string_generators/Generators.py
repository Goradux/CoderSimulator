import random
import math

from colorama import Fore

variable_name_special = ['i', 'j', 'z', '_', 'count']
variable_name_main = ['main', 'count', 'size', 'width', 'height', 'area', 'volume', 'amount', 'cell', 'sum']
variable_name_secondary = ['builder', 'concurrent', 'today', 'old', 'new', 'another', 'server', 'client', 'remote']
variable_name_tertiary = ['brown', 'red', 'black', 'green', 'blue', 'red', 'white', 'yellow', 'rare', 'common', 'legendary', 'meme']
function_name_main = ['get', 'retrieve', 'add', 'multiply', 'count', 'size', 'check', 'zip', 'sum', 'text', 'string', 'str', 'make', 'build', 'standard', 'read', 'del', 'delete', 'remove']

strings = []

def generate_number():
    return str(random.choice([random.randint(0, 10000), str(round(random.random(), 3))]))

def generate_variable_name():
    roll = random.choice(['one_word', 'two_words', 'three_words', 'special', 'object'])
    if roll is 'one_word':
        choice = random.choice(variable_name_main)
        return choice
    elif roll is 'two_words':
        choice = random.choice(variable_name_secondary) + '_' + random.choice(variable_name_main)
        return choice
    elif roll is 'three_words':
        choice = random.choice(variable_name_tertiary) + '_' + random.choice(variable_name_secondary) + '_' + random.choice(variable_name_main)
        return choice
    elif roll is 'special':
        choice = random.choice(variable_name_special)
        return choice
    elif roll is 'object':
        choice = random.choice(variable_name_secondary) + '.' + random.choice(variable_name_main)
        return choice

def generate_string():
    roll = random.choice(['one_word', 'two_words', 'three_words'])
    if roll is 'one_word':
        choice = "'" + random.choice(variable_name_main) + "'"
        return choice
    elif roll is 'two_words':
        choice = "'" + random.choice(variable_name_secondary) + ' ' + random.choice(variable_name_main) + "'"
        return choice
    elif roll is 'three_words':
        choice = "'" + random.choice(variable_name_tertiary) + ' ' + random.choice(variable_name_secondary) + ' ' + random.choice(variable_name_main) + "'"
        return choice

def generate_value():
    return random.choice([generate_number(), generate_string()])

def generate_arguments():
    roll = random.choice(['zero', 'one', 'two'])
    if roll is 'zero':
        return []
    elif roll is 'one':
        first = random.choice([generate_variable_name(), generate_string(), generate_number()])
        # return first
        return random.choice([(Fore.LIGHTWHITE_EX, generate_variable_name()), (Fore.LIGHTYELLOW_EX, generate_string()), (Fore.LIGHTBLACK_EX, generate_number())])
    elif roll is 'two':
        # first =  random.choice([generate_variable_name(), generate_string(), generate_number()])
        # second = random.choice([generate_variable_name(), generate_string(), generate_number()])
        # return first + ', ' + second
        first = random.choice([(Fore.LIGHTWHITE_EX, generate_variable_name()), (Fore.LIGHTYELLOW_EX, generate_string()), (Fore.LIGHTBLACK_EX, generate_number())])
        second = random.choice([(Fore.LIGHTWHITE_EX, generate_variable_name()), (Fore.LIGHTYELLOW_EX, generate_string()), (Fore.LIGHTBLACK_EX, generate_number())])
        return [first, (Fore.LIGHTWHITE_EX, ', '), second]

def generate_function_name():
    roll = random.choice(['one_word', 'two_words', 'three_words'])
    if roll is 'one_word':
        # choice = random.choice(function_name_main) + '(' + generate_arguments() + ')'
        # return choice
        return [(Fore.LIGHTWHITE_EX, random.choice(function_name_main) + '('), generate_arguments(), (Fore.LIGHTWHITE_EX, ')')]
    elif roll is 'two_words':
        # choice = random.choice(function_name_main) + '_' + random.choice(variable_name_main) + '(' + generate_arguments() + ')'
        # return choice
        return [(Fore.LIGHTWHITE_EX, random.choice(function_name_main) + '_' + random.choice(variable_name_main) + '('), generate_arguments(), (Fore.LIGHTWHITE_EX, ')')]
    elif roll is 'three_words':
        # choice = random.choice(function_name_main) + '_' + random.choice(variable_name_secondary) + '_' + random.choice(variable_name_main) + '(' + generate_arguments() + ')'
        # return choice
        return [(Fore.LIGHTWHITE_EX, random.choice(function_name_main) + '_' + random.choice(variable_name_secondary) + '_' + random.choice(variable_name_main) + '('), generate_arguments(), (Fore.LIGHTWHITE_EX, ')')]

def get_statement():
    # cases:
    # comparing of values
    # comparing strings
    # comparing types
    # comparing lengths
    # comparing variables

    def get_symbol():
        return random.choice([(Fore.BLUE, ' is '), (Fore.BLUE, ' is not '), (Fore.LIGHTWHITE_EX, ' > '), (Fore.LIGHTWHITE_EX, ' >= '), (Fore.LIGHTWHITE_EX, ' <= '), (Fore.LIGHTWHITE_EX, ' == ')])

    # comparing expressions
    roll = random.randint(0, 9)
    # another expression, 30%
    if roll < 3:
        return [(Fore.LIGHTWHITE_EX, generate_variable_name()), get_symbol(), (Fore.LIGHTBLACK_EX, str(random.choice([random.randint(0, 1000), round(random.random(), 3)]))), (Fore.BLUE, random.choice([' or ', ' and '])), get_statement(), (Fore.LIGHTWHITE_EX, '')]
    # value 20%
    elif roll < 5:
        choice = random.choice([random.randint(0, 1000), round(random.random(), 3)])
        return (Fore.LIGHTWHITE_EX, str(choice if random.randint(0, 1) is 0 else choice * -1))
    # string 10%
    elif roll is 5:
        return [(Fore.LIGHTWHITE_EX, generate_variable_name()), get_symbol(), (Fore.YELLOW, generate_string())]
    # type() 10%
    elif roll is 6:
        return [(Fore.CYAN, 'type'), (Fore.LIGHTWHITE_EX, '(' + generate_variable_name() + ')'), get_symbol(), (Fore.CYAN, 'type'), (Fore.LIGHTWHITE_EX, '('), random.choice([(Fore.LIGHTWHITE_EX, generate_variable_name()), (Fore.LIGHTYELLOW_EX, generate_string())]), (Fore.LIGHTWHITE_EX, ')')]
    # len() 10%
    elif roll is 7:
        return [(Fore.CYAN, 'len'), (Fore.LIGHTWHITE_EX, '(' + generate_variable_name() + ')'), get_symbol(), (Fore.CYAN, 'len'), (Fore.LIGHTWHITE_EX, '('), random.choice([(Fore.LIGHTWHITE_EX, generate_variable_name()), (Fore.LIGHTYELLOW_EX, generate_string())]), (Fore.LIGHTWHITE_EX, ')')]
    # variables 20%
    elif roll >= 8:
        return [(Fore.LIGHTWHITE_EX, generate_variable_name()), get_symbol(), (Fore.LIGHTWHITE_EX, generate_variable_name())]

    # '''hi source code nerd :)'''
    

list_of_comments_type_one = ['The following code is responsible for', 'Check out:', 'Explaining', '!IMPORTANT', 'TODO', 'BUG']

list_of_comments_type_two = ['is the focus here', '- to finish', 'not generating then expected output', 'DON\'T TOUCH!']
list_of_comments_type_three = ['Important function:', 'Do not forget to declare:', 'Determines the outcome', 'Check the wiki:', 'BTW, www.github.com/Goradux']
def generate_comment():
    roll = random.randint(0, 2)
    if roll is 0:
        return '# ' + random.choice(list_of_comments_type_one) + ' ' + generate_value()
    elif roll is 1:
        # if roll is 1
        return '# ' + generate_value() + ' ' + random.choice(list_of_comments_type_two) 
    elif roll is 2:
        return '# ' + random.choice(list_of_comments_type_three)

list_of_errors = ['IndexError', 'ModuleNotFoundError', 'KeyError', 'ImportError', 'StopIteration', 'TypeError', 'ValueError', 'NameError', 'KeyboardInterrupt', 'TypeError', 'UnicodeError', 'TabError']
def generate_exception():
    return random.choice(list_of_errors)

def generate_iterable():
    roll = random.choice(['range', 'var'])
    if roll is 'range':
        return 'range(' + str(random.randint(0, 50)) + ', ' + str(random.randint(50, 250)) + ')'
    elif roll is 'var':
        return generate_variable_name()
    # cases:
    # range of numbers
    # in variable

def generate_loop():
    # loop = 'for ' + random.choice(list_of_vars) + ' in ' + self.generate_iterable() + ':'
    loop_type = 'for' if random.randint(0, 1) is 0 else 'while'
    if loop_type is 'for':
        # return 'for ' + generate_variable_name() + ' in ' + generate_iterable() + ':'
        return [(Fore.LIGHTMAGENTA_EX, 'for '), (Fore.LIGHTWHITE_EX, generate_variable_name()), (Fore.LIGHTMAGENTA_EX, ' in '), (Fore.LIGHTWHITE_EX, generate_iterable()), (Fore.LIGHTWHITE_EX, ':')]
    elif loop_type is 'while':
        # return 'while ' + get_statement() + ':'
        return [(Fore.LIGHTMAGENTA_EX, 'while '), get_statement(), (Fore.LIGHTWHITE_EX, ': ')]