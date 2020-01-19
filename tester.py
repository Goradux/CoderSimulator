# import sys, time, random

# text  = 'some test text'
# text2 = 'more test text'

# big = [text, text2]

# for element in big:
#     for letter in text:
#         print(letter, end='')
#         sys.stdout.flush()
#         time.sleep(random.randint(1, 10)/200)
#     # print('\n', end='')
#     print()

# =======================

GREEN = None
BLUE = None
RED = None

def another_function():
    return [(GREEN, 'text'), (BLUE, 'text')]

def some_function():
    return [(GREEN, 'text'), (BLUE, 'text'), another_function()]

some_list = [(GREEN, 'text'), (BLUE, 'text'), some_function(), some_function(), (RED, 'text')]

# print(some_list)
# flat_list = [item for sublist in some_list for item in sublist]

# output = []
# def removeNestings(l): 
#     for i in l: 
#         if type(i) == list: 
#             removeNestings(i) 
#         else: 
#             output.append(i) 


# def remove_nested(nested_list, output_list=[]):
#     for element in nested_list:
#         if type(element) is list:
#             remove_nested(element, output_list)
#         else:
#             output_list.append(element)
#     return output_list

# print(remove_nested(some_list))

# removeNestings(some_list)
# print(output)

# try:
#     pass
# except Exception as e:
#     pass

import colorama
from colorama import Fore

colorama.init()

print(Fore.BLACK + 'test')
print(Fore.BLUE + 'test')
print(Fore.CYAN + 'test')
print(Fore.GREEN + 'test')
print(Fore.LIGHTBLACK_EX + 'test')
print(Fore.LIGHTCYAN_EX + 'test')
print(Fore.LIGHTGREEN_EX + 'test')
print(Fore.LIGHTMAGENTA_EX + 'test')
print(Fore.LIGHTRED_EX + 'test')
print(Fore.LIGHTWHITE_EX + 'test')
print(Fore.LIGHTYELLOW_EX + 'test')
print(Fore.MAGENTA + 'test')
print(Fore.RED + 'test')
print(Fore.RESET + 'test')
print(Fore.WHITE + 'test')
print(Fore.YELLOW + 'test')
