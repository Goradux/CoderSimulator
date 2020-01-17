import sys, time, random

# pip install colorama
# https://pypi.org/project/colorama/
from colorama import Fore, Back, Style
from colorama import init as coloramainit
coloramainit()
#a way to reset the colors is to call print(Style.RESET_ALL, end='')

# deque is faster O(1) than a list O(n)
# use it like this: stack = deque(); stack.append(var); var = stack.pop();
from collections import deque

list_of_vars = ['x', '_', 'y', 'i', 'index', 'foo', 'bar', 'foobar', 'amount', 'width', 'height']
list_of_functions = ['add', 'remove']

class Coder:

    next_action = None
    # buffered_action = None
    tab = 0
    vars_in_use = []
    buffered_actions = deque()
    followup = False

    def humanoid_print(self, print_out):
        # print(self.tab)
        for _ in range(self.tab):
                print('    ', end = '')
        for index in range(len(print_out)):
            print(print_out[index], end = '')
            sys.stdout.flush()
            time.sleep(random.randint(1, 10)/100)
            if index == len(print_out) - 1:
                print()
        # time.sleep(0.05)
        time.sleep(1 if random.randint(0, 10) == 0 else 0)

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

    def if_statement(self):
        self.humanoid_print('if (STATEMENT):')
        self.tab = self.tab + 1
        self.followup = True

    def else_statement(self):
        self.humanoid_print('else:')
        self.tab = self.tab + 1
        self.followup = True

    def if_else_statement(self):
        self.if_statement()
        # self.humanoid_print('if else')

    def if_inline_statement(self):
        self.humanoid_print(random.choice(list_of_vars) + ' = ' + '(STATEMENT) if (STATEMENT) else 0')
        self.followup = False


    def try_statement(self):
        self.humanoid_print('try:')
        self.tab = self.tab + 1
        self.followup = True

    def except_statement(self):
        if random.randint(0, 1) is 0:
            self.humanoid_print('except:')
        else:
            self.humanoid_print('except Exception as e:')
        self.tab = self.tab + 1
        self.followup = True

    def create_loop(self):
        loop = 'for ' + random.choice(list_of_vars) + ' in range(' + str(random.randint(0, 50)) + ', ' + str(random.randint(50, 250)) + '):'
        self.humanoid_print(loop)
        self.tab = self.tab + 1
        self.followup = True

    def create_function(self):
        self.humanoid_print('function (FUNCTION):')
        self.tab = self.tab + 1
        self.followup = True

    def assign_var_value(self):
        random_var = random.choice(list_of_vars)
        self.vars_in_use.append(random_var)
        output = random_var + ' = ' + str(random.randint(0, 10))
        self.humanoid_print(output)
        self.followup = False

    
    def print_statement(self):
        self.humanoid_print('print(' + random.choice(list_of_vars) + ')')
        self.followup = False
    
    def execute_function_statement(self):
        self.humanoid_print(random.choice(list_of_functions) + '(' + random.choice(list_of_vars) +')')
        self.followup = False

    def comment_statement(self):
        comment = '# some comment'
        self.humanoid_print(comment)

    # def pass_statement(self):
    #     self.humanoid_print('pass')

    action_choices = [if_else_statement, try_statement, create_loop, create_function,
        if_statement, if_inline_statement, print_statement, assign_var_value,
        execute_function_statement, comment_statement]
    action_choices_simple = [assign_var_value, print_statement, execute_function_statement,
        comment_statement]
    def choose_action(self):
        self.next_action = random.choice(self.action_choices) if self.tab < 5 else random.choice(self.action_choices_simple)
        # print(self.next_action)
        self.next_action(self)
        
        # these two actions are composite, and require a second part with
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
        # self.buffered_action = None

    def do_next_action(self):
        self.choose_action()
        self.roll_indent()
        self.roll_space()
        self.action_cleanup()

        self.do_next_action()

    # def __init__(self):
    #     print('Coder init done')

    def start(self):
        self.do_next_action()