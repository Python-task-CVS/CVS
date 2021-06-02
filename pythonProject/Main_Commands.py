import os
import sys
import Service_func
import Commits
from RepositoryCmd import *


_Repo = None
_Add_Diffs = None
_Changes = None
_Commit_count = 0


def init(path):
    if os.listdir(path):
        sys.exit("To initialize a repository choose an empty folder")
    if not os.path.isdir(path):
        sys.exit("Incorrect path")

    _Repo = os.path.join(path, "repo.txt")
    Service_func.init_dict_object(_Repo)

    _Add_Diffs = os.path.join(path, "added_diffs.txt")
    Service_func.init_dict_object(_Add_Diffs)

    _Changes = os.path.join(path, "changes.txt")
    Service_func.init_dict_object(_Changes)

    Service_func.save_object("Repository", Repository(path), _Repo)
    print("Repository initialized")


def add(*files):
    dict = Service_func.get_dict_objects(_Changes)
    if not files:
        print("Not changes to add")
    for file_name in files:
        if file_name in dict.keys():
            file = dict.pop(file_name)
            Service_func.save_object(file_name, file, _Add_Diffs)
        else:
            print("File {} is not exist".format(file_name))



def commit(message):
    repo = Service_func.get_object(_Repo, "Repository")
    diffs = Service_func.get_object(_Add_Diffs)
    commit = Commits.Commit(str(_Commit_count+1), message, repo.head._head, repo.head, _)
    print("commit")


def reset():
    print("reset")


def status():
    print("status")


def log():
    print("log")


def check():
    print("check")
