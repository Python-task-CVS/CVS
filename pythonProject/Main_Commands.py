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
    dict = Service_func.get_dict_objects(_Changes)["Changes"]
    if not files:
        print("Not changes to add")
    commit_dict = Service_func.get_dict_objects(_Add_Diffs)["Commit"]
    for file_name in files:
        if file_name in dict.keys():
            file = dict.pop(file_name)
            commit_dict[file_name] = file

        else:
            print("File {} is not exist".format(file_name))
    Service_func.save_object("Commit", commit_dict, _Add_Diffs)
    Service_func.save_object("Changes", dict, _Changes)


def commit(message):
    repo = Service_func.get_object(_Repo, "Repository")
    diffs = Service_func.get_object(_Add_Diffs)["Commit"]
    commit = Commits.Commit(str(_Commit_count+1), message, repo.head._head, repo.head, diffs)
    repo.add_log(Log("commit", commit))
    repo.head._head = commit
    Service_func.save_object("Commit", {}, _Add_Diffs)
    Service_func.save_object("Repository", repo, _Repo)
    print("commit")


def reset():
    repo = Service_func.get_object(_Repo, "Repository")
    commit = repo.head._head
    repo.add_log(Log("reset", commit))
    repo.head._head = commit.prev_commit
    Service_func.save_object("Repository", repo, _Repo)
    print("reset")


def status():
    print("status")


def log():
    print("log")


def check():
    print("check")
