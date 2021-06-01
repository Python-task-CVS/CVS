import os, sys
import queue
import datetime


class File():
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.lastChange = datetime.date

    def Update(self):

current = None
changes = {}

def init(path=os.getcwd()):
    try:
        os.chdir(path)
        os.mkdir('/CVS')
        current = open("zero_version.txt")
        current.close()
        print("Initialize success")
    except Exception:
        print("Initialize failed. Try again")


def add(*files):
    for file in files:

    print("add")
    return True


def commit():
    if len(changes) == 0:
        print("No changes to commit")
    else:

    print("commit")


def reset():
    print("reset")


def status():
    print("status")


def log():
    print("log")
