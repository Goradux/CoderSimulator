import sys, time, random

# pip install colorama
# https://pypi.org/project/colorama/
from colorama import Fore, Back, Style
from colorama import init as coloramainit
coloramainit()

# paths have to be relative to __main__ in Python, otherwise use sys.path
import classes.colored.string_generators.Generators as Generators

# deque is faster with O(1) than a list with O(n)
# use it like this: stack = deque(); stack.append(var); var = stack.pop();
from collections import deque

class Coder:

    speed = 200
    next_action = None
    tab = 0
    tabs = deque()
    buffered_actions = deque()
    followup = False

    def __init__(self, speed=200):
        self.speed = speed

    def remove_nested(self, nested_list, output_list=None):
        if output_list is None:
            output_list = []
        for element in nested_list:
            if type(element) is list:
                self.remove_nested(element, output_list)
            else:
                output_list.append(element)
        return output_list

    # new format of print_outs is a list of tuples (color, string)
    def humanoid_print(self, print_out=None, matching_indent=None):
        if print_out is None:
            print_out = [(Fore.LIGHTWHITE_EX, ' ')]
        
        if matching_indent is None:
            matching_indent = False
        
        if matching_indent is False:
            pass
        else:
            self.tab = self.tabs.pop()
        for _ in range(self.tab):
            print('    ', end = '')

        for element in print_out:
            color, text = element
            print(color, end = '')
            for letter in text:
                print(letter, end = '')
                sys.stdout.flush()
                time.sleep(random.randint(1, 10) / self.speed)
        print()
        # time.sleep(1 if random.randint(0, 10) == 0 else 0)

    def roll_indent(self):
        # random roll for a chance to indent 1 level back
        if self.tab > 0 and self.followup == False:
            roll = random.randint(0, 99)
            if roll < 50:
                self.tab = self.tab - 1
                if len(self.buffered_actions) > 0:
                    self.buffered_actions.pop()()
                    self.followup = True
                    # deindent = self.buffered_actions.pop()
                    # print(deindent)
            elif roll < 85:

                #BUG THIS GOT BROKEN
                if len(self.buffered_actions) == 0:
                    self.tab = self.tab - 2
                    # self.buffered_actions.pop()()
                    # self.followup = True
                    # deindent = self.buffered_actions.pop()
                    # print(deindent)
            self.tab = 0 if self.tab < 0 else self.tab 
        # 25% chance to go back one level
        # # 10% chance to go back two levels

    def roll_space(self):
        roll = random.randint(0, 99)
        if roll < 15:
            print()

    def generate_statement(self):
        return Generators.get_statement()

    def generate_value(self):
        return Generators.generate_value()

    # def generate_iterable(self):
    #     iterable = 'range(' + str(random.randint(0, 50)) + ', ' + str(random.randint(50, 250)) + ')'
    #     return '(ITERABLE)'
    
    def generate_function_name(self):
        return Generators.generate_function_name()

    def if_statement(self):
        if_list = [(Fore.LIGHTMAGENTA_EX, 'if '), Generators.get_statement(), (Fore.LIGHTWHITE_EX, ':')]
        # self.humanoid_print('if ' + self.generate_statement() + ':')
        self.humanoid_print(self.remove_nested(if_list))
        self.tab = self.tab + 1
        self.followup = True

    def else_statement(self):
        else_list = [(Fore.LIGHTMAGENTA_EX, 'else'), (Fore.LIGHTWHITE_EX, ':')]
        # self.humanoid_print('else:', matching_indent=True)
        self.humanoid_print(self.remove_nested(else_list), matching_indent=True)
        self.tab = self.tab + 1
        self.followup = True

    def if_else_statement(self):
        self.tabs.append(self.tab)
        self.if_statement()
        # self.humanoid_print('if else')

    def if_inline_statement(self):
        if_inline_list = [(Fore.LIGHTWHITE_EX, Generators.generate_variable_name() + ' = '), random.choice([(Fore.LIGHTBLACK_EX, Generators.generate_number()), (Fore.LIGHTYELLOW_EX, Generators.generate_string())]), (Fore.LIGHTMAGENTA_EX, ' if '), (Fore.LIGHTWHITE_EX, '('), Generators.get_statement(), (Fore.LIGHTWHITE_EX, ')'), (Fore.LIGHTMAGENTA_EX, ' else '), random.choice([(Fore.LIGHTBLACK_EX, Generators.generate_number()), (Fore.LIGHTYELLOW_EX, Generators.generate_string())]), (Fore.LIGHTWHITE_EX, ' ')]
        self.humanoid_print(self.remove_nested(if_inline_list))
        self.followup = False

    def try_statement(self):
        self.tabs.append(self.tab)
        try_list = [(Fore.LIGHTMAGENTA_EX, 'try'), (Fore.LIGHTWHITE_EX, ':')]
        # self.humanoid_print('try:')
        self.humanoid_print(self.remove_nested(try_list))
        self.tab = self.tab + 1
        self.followup = True

    def except_statement(self):
        if random.randint(0, 1) is 0:
            except_list = [(Fore.LIGHTMAGENTA_EX, 'except'), (Fore.LIGHTWHITE_EX, ':')]
            # self.humanoid_print('except:', matching_indent=True)
        else:
            except_list = [(Fore.LIGHTMAGENTA_EX, 'except '), (Fore.CYAN, Generators.generate_exception()), (Fore.LIGHTMAGENTA_EX, ' as'), (Fore.LIGHTWHITE_EX, ' e:')]
            # self.humanoid_print('except ' + Generators.generate_exception() + ' as e:', matching_indent=True)
        self.humanoid_print(self.remove_nested(except_list), matching_indent=True)
        self.tab = self.tab + 1
        self.followup = True

    def create_loop(self):
        loop = Generators.generate_loop()
        self.humanoid_print(self.remove_nested(loop))
        self.tab = self.tab + 1
        self.followup = True

    def create_function(self):
        function_list = [(Fore.BLUE, 'def '), Generators.generate_function_name(), (Fore.LIGHTWHITE_EX, ':')]
        self.humanoid_print(self.remove_nested(function_list))
        self.tab = self.tab + 1
        self.followup = True

    def assign_var_value(self):
        random_var = Generators.generate_variable_name()
        assign_var_list = [(Fore.LIGHTWHITE_EX, random_var + ' = '), random.choice([(Fore.LIGHTBLACK_EX, Generators.generate_number()), (Fore.LIGHTYELLOW_EX, Generators.generate_string())])]
        self.humanoid_print(self.remove_nested(assign_var_list))
        self.followup = False
    
    def print_statement(self):
        print_list = [(Fore.CYAN, 'print'), (Fore.LIGHTWHITE_EX, '('), random.choice([(Fore.LIGHTBLACK_EX, Generators.generate_number()), Generators.generate_function_name(), (Fore.LIGHTWHITE_EX, Generators.generate_variable_name())]), (Fore.LIGHTWHITE_EX, ')'),]
        self.humanoid_print(self.remove_nested(print_list))
        self.followup = False
    
    def execute_function_statement(self):
        self.humanoid_print(self.remove_nested([Generators.generate_function_name()]))
        self.followup = False

    def comment_statement(self):
        comment = Generators.generate_comment()
        self.humanoid_print(self.remove_nested([(Fore.GREEN, comment)]))

    # def pass_statement(self):
    #     self.humanoid_print('pass')

    def code_block(self, size=None):
        if size is None:
            size = 3
        
        for _ in range(size):
            # self.humanoid_print('a line of a code_block')
            random.choice(self.action_choices_simple)(self)
        
        print()

    # def code_block_bigger(self):
    #     self.code_block(5)
    #     pass

    # def code_block_biggest(self):
    #     self.code_block(7)
    #     pass

    # a set of all possible actions
    action_choices = [if_else_statement, try_statement, create_loop, create_function,
        if_statement, if_inline_statement, print_statement, assign_var_value,
        execute_function_statement, comment_statement, code_block]
    # a set of actions that do not require indentation
    action_choices_simple = [assign_var_value, print_statement, execute_function_statement,
        comment_statement, code_block]
    def choose_action(self):
        
        # choose the next action
        self.next_action = random.choice(self.action_choices) if self.tab < 5 else random.choice(self.action_choices_simple)
        
        #perform the next action
        self.next_action(self)
        


        # these following two actions are composite, and require a second part with
        # indentation back and forth
        # NOTE: compared to the part of the action_choices and not the
        # functions themselves because the memory slots are different
        
        # at least one statement is required so that it wont indent back on empty line

        # if_else_statement
        if self.next_action == self.action_choices[0]:
            self.buffered_actions.append(self.else_statement)
            self.next_action = random.choice(self.action_choices_simple)
            self.next_action(self)
        # try_statement
        if self.next_action == self.action_choices[1]:
            self.buffered_actions.append(self.except_statement)
            self.next_action = random.choice(self.action_choices_simple)
            self.next_action(self)

    def action_cleanup(self):
        self.next_action = None

    # the main action loop, recursive
    def do_next_action(self):
        self.choose_action()
        self.roll_indent()
        self.roll_space()
        self.action_cleanup()

        self.do_next_action()

    def start(self):
        self.do_next_action()

    # a test method. Executes an action block once
    def test(self):
        self.choose_action()
        self.roll_indent()
        self.roll_space()
        self.action_cleanup()