# This module contains functions that generate some basic building blocks
# for the Coder.py module. For example, it has functions that can create
# variable names, expressions for if statements, function names, etc.
# All of the functions return strings.

import random


variable_name_special = ['i', 'j', 'z', 'count', 'x', 'y', 'index', 'foo', 'bar', 'foobar', 'amount', 'width', 'height']
variable_name_main = ['main', 'count', 'size', 'width', 'height', 'area', 'volume', 'amount', 'cell', 'sum']
variable_name_secondary = ['builder', 'concurrent', 'today', 'old', 'new', 'another', 'server', 'client', 'remote']
variable_name_tertiary = ['brown', 'red', 'black', 'green', 'blue', 'red', 'white', 'yellow', 'rare', 'common', 'legendary', 'meme']
function_name_main = ['get', 'retrieve', 'add', 'multiply', 'count', 'size', 'check', 'zip', 'sum', 'text', 'string', 'str', 'make', 'build', 'standard', 'read', 'del', 'delete', 'remove']


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
        choice = random.choice(variable_name_main)
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
        return ''
    elif roll is 'one':
        first = random.choice([generate_variable_name(), generate_string(), generate_number()])
        return first
    elif roll is 'two':
        first =  random.choice([generate_variable_name(), generate_string(), generate_number()])
        second = random.choice([generate_variable_name(), generate_string(), generate_number()])
        return first + ', ' + second


def generate_function_name():
    roll = random.choice(['one_word', 'two_words', 'three_words'])
    if roll is 'one_word':
        choice = random.choice(function_name_main) + '(' + generate_arguments() + ')'
        return choice
    elif roll is 'two_words':
        choice = random.choice(function_name_main) + '_' + random.choice(variable_name_main) + '(' + generate_arguments() + ')'
        return choice
    elif roll is 'three_words':
        choice = random.choice(function_name_main) + '_' + random.choice(variable_name_secondary) + '_' + random.choice(variable_name_main) + '(' + generate_arguments() + ')'
        return choice


def get_statement():

    def get_symbol():
        return random.choice([' is ', ' is not ', ' > ', ' >= ', ' <= ', ' == '])


    roll = random.randint(0, 9)
    # comparing expressions to:
    # another expression, 40%
    if roll < 3:
        return generate_variable_name() + get_symbol() + str(random.choice([random.randint(0, 1000), round(random.random(), 3)])) +  random.choice([' or ', ' and ']) +  get_statement()
    # value 20%
    elif roll < 5:
        choice = random.choice([random.randint(0, 1000), round(random.random(), 3)])
        return str(choice if random.randint(0, 1) is 0 else choice * -1)
    # string 10%
    elif roll is 5:
        return generate_variable_name() + get_symbol() + generate_string()
    # type 10%
    elif roll is 6:
        return 'type(' + generate_variable_name() + ')' + get_symbol() + 'type(' + random.choice([generate_variable_name(), generate_string()]) + ')'
    # length 10%
    elif roll is 7:
        return 'len(' + generate_variable_name() + ')' + get_symbol() + 'len(' + random.choice([generate_variable_name(), generate_string()]) + ')'
    # variables 20%
    elif roll >= 8:
        return generate_variable_name() + get_symbol() + generate_variable_name()

    # 'hi source code nerd :)'
    

list_of_comments_type_one = ['The following code is responsible for', 'Check out:', 'Explaining', '!IMPORTANT', 'TODO', 'BUG']
list_of_comments_type_two = ['is the focus here', '- to finish', 'not generating then expected output', 'DON\'T TOUCH!']
list_of_comments_type_three = ['Important function:', 'Do not forget to declare:', 'Determines the outcome', 'Check the wiki:', 'BTW, www.github.com/Goradux']
def generate_comment():
    roll = random.randint(0, 2)
    if roll is 0:
        return '# ' + random.choice(list_of_comments_type_one) + ' ' + generate_value()
    elif roll is 1:
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


def generate_loop():
    loop_type = 'for' if random.randint(0, 1) is 0 else 'while'
    if loop_type is 'for':
        return 'for ' + generate_variable_name() + ' in ' + generate_iterable() + ':'
    elif loop_type is 'while':
        return 'while ' + get_statement() + ':'