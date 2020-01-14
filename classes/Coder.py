import sys, time, random

# deque is faster O(1) than a list O(n)
# use it like this: stack = deque(); stack.append(var); var = stack.pop();
from collections import deque

list_of_vars = ['x', 'y', 'i', 'index', 'foo', 'bar', 'foobar', 'amount', 'width', 'height']

class Coder:

    next_action = None
    # buffered_action = None
    tab = 0
    vars_in_use = []
    buffered_actions = deque()

    def humanoid_print(self, print_out):
        for _ in range(self.tab):
                print('    ', end = '')
        for index in range(len(print_out)):
            print(print_out[index], end = '')
            sys.stdout.flush()
            time.sleep(random.randint(1, 10)/100)
            if index == len(print_out) - 1:
                print()

    def roll_indent(self):
        # random roll for a chance to indent 1 level back
        pass

    def if_statement(self):
        self.humanoid_print('if')

    def else_statement(self):
        self.humanoid_print('else')

    def if_else_statement(self):
        # self.if_statement()
        self.humanoid_print('if else')

    def try_statement(self):
        self.humanoid_print('try')

    def except_statement(self):
        self.humanoid_print('except')

    def create_loop(self):
        start = 'for ' + random.choice(self.vars_in_use) + ' in range(0, 10):'
        self.humanoid_print(start)
        self.tab = self.tab + 1

    def create_function(self):
        self.humanoid_print('function')

    def assign_var(self):
        random_var = random.choice(list_of_vars)
        self.vars_in_use.append(random_var)
        output = random_var + ' = ' + str(random.randint(0, 10))
        self.humanoid_print(output)

    action_choices = [assign_var, create_loop, create_function, if_statement,
        if_else_statement]

    def choose_action(self):
        self.next_action = random.choice(self.action_choices)
        
        # these two actions are composite, and require a second part with
        # indentation back and forth
        if self.next_action == self.if_else_statement:
            self.buffered_actions.append(self.else_statement)
        if self.next_action == self.try_statement:
            self.buffered_actions.append(self.except_statement)

    def action_cleanup(self):
        self.next_action = None
        # self.buffered_action = None

    def do_next_action(self):
        self.choose_action()
        self.next_action(self)

        # self.buffered_actions.pop()()             #execute else: or except:

        # if self.buffered_action is not None:
        #     self.tab = self.tab - 1
        #     self.buffered_action()
        self.action_cleanup()

        self.do_next_action()

    def __init__(self):
        print('Coder init done')
        # self.humanoid_print('something')
        # self.create_loop()
        # self.assign_var()

    def start(self):
        self.do_next_action()