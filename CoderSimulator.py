# Supported modes: 'colored', 'default'
MODE = 'colored'

import time, datetime, sys

sys.setrecursionlimit(10**6)

if MODE is None or MODE is 'colored':
    from classes.colored.Coder import Coder
    coder = Coder()
    coder.start()
elif MODE is 'default':
    from classes.default.Coder import Coder
    coder = Coder()
    coder.start()
# coder.test()

# text = 'some string of text'
# coder.humanoid_print(text)