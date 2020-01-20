import sys, time, random

# paths have to be relative to __main__ in Python, otherwise use sys.path
import classes.default.string_generators.Generators as Generators

# deque is faster O(1) than a list O(n)
# use it like this: stack = deque(); stack.append(var); var = stack.pop();
from collections import deque


class Coder:

    speed = 200                 # current printing speed
    next_action = None          # what is the next action to perform
    tab = 0                     # current indentation level (hardcoded to not exceed 5)
    tabs = deque()              # buffered indentations, for if/else else should be same lvl as if
    buffered_actions = deque()  # buffered actions, for if/else else goes to the buffer
    followup = False            # whether a followup action is required, for if: def: try:, etc


    def __init__(self, speed=200):
        self.speed = speed


    # function that simulates typing in code at human speeds.
    # Input: matching_indent - boolean, used only for else or except statements
    def humanoid_print(self, print_out, matching_indent=None):
        if matching_indent is None:
            matching_indent = False
        
        if matching_indent is False:
            pass
        else:
            self.tab = self.tabs.pop()
        for _ in range(self.tab):
            print('    ', end = '')

        for letter in print_out:
            print(letter, end='')
            sys.stdout.flush()
            time.sleep(random.randint(1, 10)/self.speed)
        print()


    # rolls dice to whether continue generating code on the current indentation
    # level, or go back 1 (or 2) tabs, if the code allows
    def roll_indent(self):
        # random roll for a chance to indent 1 level back
        if self.tab > 0 and self.followup == False:
            roll = random.randint(0, 99)
            if roll < 50:
                self.tab = self.tab - 1
                if len(self.buffered_actions) > 0:
                    self.buffered_actions.pop()()
                    self.followup = True
            elif roll < 85:
                # if there are no actions in the buffer, allow for a "-2 tabs" option
                if len(self.buffered_actions) == 0:
                    self.tab = self.tab - 2
            self.tab = 0 if self.tab < 0 else self.tab


    # Function that prints an empty line randomly (15% chance)
    def roll_space(self):
        roll = random.randint(0, 99)
        if roll < 15:
            print()


    def if_statement(self):
        self.humanoid_print('if ' + Generators.get_statement() + ':')
        self.tab = self.tab + 1
        self.followup = True


    def else_statement(self):
        self.humanoid_print('else:', matching_indent=True)
        self.tab = self.tab + 1
        self.followup = True


    def if_else_statement(self):
        self.tabs.append(self.tab)
        self.if_statement()


    def if_inline_statement(self):
        self.humanoid_print(Generators.generate_variable_name() + ' = ' + Generators.generate_value() + ' if (' + Generators.get_statement() + ') else ' + Generators.generate_value())
        self.followup = False


    def try_statement(self):
        self.tabs.append(self.tab)
        self.humanoid_print('try:')
        self.tab = self.tab + 1
        self.followup = True


    def except_statement(self):
        if random.randint(0, 1) is 0:
            self.humanoid_print('except:', matching_indent=True)
        else:
            self.humanoid_print('except ' + Generators.generate_exception() + ' as e:', matching_indent=True)
        self.tab = self.tab + 1
        self.followup = True


    def create_loop(self):
        loop = Generators.generate_loop()
        self.humanoid_print(loop)
        self.tab = self.tab + 1
        self.followup = True


    def create_function(self):
        self.humanoid_print('def ' + Generators.generate_function_name() + ':')
        self.tab = self.tab + 1
        self.followup = True


    def assign_var_value(self):
        random_var = Generators.generate_variable_name()
        output = random_var + ' = ' + Generators.generate_value()
        self.humanoid_print(output)
        self.followup = False
    

    def print_statement(self):
        self.humanoid_print('print(' + random.choice([Generators.get_statement(), Generators.generate_number(), Generators.generate_function_name(), Generators.generate_variable_name()]) + ')')
        self.followup = False
    

    def execute_function_statement(self):
        self.humanoid_print(Generators.generate_function_name())
        self.followup = False


    def comment_statement(self):
        comment = Generators.generate_comment()
        self.humanoid_print(comment)


    # a composite block that randomly executes 3 actions from a simple action list
    def code_block(self, size=None):
        if size is None:
            size = 3
        
        for _ in range(size):
            random.choice(self.action_choices_simple)(self)
        print()


    # a set of all possible actions
    action_choices = [if_else_statement, try_statement, create_loop, create_function,
        if_statement, if_inline_statement, print_statement, assign_var_value,
        execute_function_statement, comment_statement, code_block]
    # a set of actions that do not require indentation
    action_choices_simple = [assign_var_value, print_statement, execute_function_statement,
        comment_statement, code_block]
    # chooses randomly an action to perform from the list above and executes it.
    def choose_action(self):

        # choose the next action
        self.next_action = random.choice(self.action_choices) if self.tab < 5 else random.choice(self.action_choices_simple)
        
        #perform the next action
        self.next_action(self)


        # these following two actions are composite, and require a second part with
        # indentation that has to be properly aligned
        # NOTE: the if statement compares to the part of the action_choices and not the
        # functions themselves because their position in memory is different
        
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


    # The main action block of the simulation.
    # Rolls a random action.
    # Rolls a random indentation check.
    # Rolls a random extra new line.
    def do_next_action(self):
        self.choose_action()
        self.roll_indent()
        self.roll_space()


    # Call this to start the simulation.
    def start(self):
        while True:
            self.do_next_action()