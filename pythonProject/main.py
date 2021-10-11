import os
import Service_func
import argparse
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
            "log": log,
            "check": check}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs='+', help="CVS command")
    parser.add_argument("--path", help="path to a folder with repository")
    parser.add_argument("-b", "--branchname", help="name of branch to create/checkout", required=False)
    parser.add_argument("-m", "--message", help="comment for new commit", required=False)
    parser.add_argument("-t", "--tag", help="tag of the commit", required=False)
    return parser.parse_args(sys.argv)




def main():
    args = parse_args()
    if args.command[0] == "init":
        init(args.path)
    elif args.command[0] == "add":
        add(args.path)
    elif args.command[0] == "commit":
        commit(args.message)
    elif args.command[0] == "reset":
        reset()
    elif args.command[0] == "status":
        status()
    elif args.command[0] == "log":
        log()
    else:
        sys.exit("Incorrect input. Call -h or --help to read manual.")


if __name__ == '__main__':
    main()