import sys, time, random

list_of_vars = ['x', 'y', 'i', 'index', 'foo', 'bar', 'foobar', 'amount', 'width', 'height']

class Coder:
    action_choices = ['assign_var', 'create_loop', 'create_function']

    next_action = None
    nextnext_action = None
    tab = 0
    vars_in_use = []

    def humanoid_print(self, print_out):
        for i in range(self.tab):
                print('    ', end = '')
        for index in range(len(print_out)):
            print(print_out[index], end = '')
            sys.stdout.flush()
            time.sleep(random.randint(1, 10)/100)
            if index == len(print_out) - 1:
                print()

    def construct_loop(self, index):
        start = 'for ' + index + ' in range(0, 10):'
        self.humanoid_print(start)
        self.tab = self.tab + 1

    def assign_var(self):
        random_var = random.choice(list_of_vars)
        self.vars_in_use.append(random_var)
        output = random_var + ' = ' + str(random.randint(0, 10))
        self.humanoid_print(output)

    def choose_action(self):
        self.next = random.choice(self.action_choices)

    def do_next(self):
        pass

    def __init__(self):
        print('Coder init done')
        # self.humanoid_print('something')
        self.construct_loop('index')
        self.assign_var()



    def start(self):
        while True:
            # get_random_action()
            # perform_random_action()
            pass