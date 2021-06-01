import os
import Service_func
from Main_Commands import *




def cashing(func):
    computed_results = {}
    def func_with_cash(*args):
        if args not in computed_results:
            computed_results[args] = func(args)
        return computed_results[args]



commands = {"init": init,
            "add": add,
            "commit": commit,
            "reset": reset,
            "log": log}

command = input()
if command in commands:
    commands[command]()
else:
    print("command doesn't exist")