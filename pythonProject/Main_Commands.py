import os
import sys

import RepositoryCmd
import Service_func
import hashlib
import Commits
from RepositoryCmd import *

'''
_Repo = None
_Add_Diffs = None
_Changes = None
_Commit_count = 0
'''
_working_dir = None
_index = None
_HEAD = None

def init(path):
    if os.listdir(path):
        sys.exit("To initialize a repository choose an empty folder")
    if not os.path.isdir(path):
        sys.exit("Incorrect path")

    _working_dir = os.path.join(path, "work_dir.txt")
    Service_func.init_dict_object(_working_dir)

    _index = os.path.join(path, "index.txt")
    Service_func.init_dict_object(_index)

    _HEAD = os.path.join(path, "HEAD.txt")
    Service_func.init_dict_object(_HEAD)

    Service_func.save_object("Repository", Repository(path), _HEAD)
    print("Repository initialized")


def add(*files):
    repo = Service_func.get_object("Repository", _HEAD)
    dict = Service_func.get_dict_objects(_working_dir)
    if not dict:
        print("Not changes to add")
        return None
    if files == '.':
        files = dict.keys()
    commit_dict = Service_func.get_dict_objects(_index)
    for file_name in files:
        if file_name in dict.keys():
            file = dict.pop(file_name)
            commit_dict[file_name] = repo.save_file(file)
        else:
            print("File {} is not change".format(file_name))
    Service_func.update_dict(commit_dict, _index)
    Service_func.update_dict(dict, _working_dir)


def commit(message):
    HEAD = Service_func.get_dict_objects(_HEAD)
    diffs = Service_func.get_dict_objects(_index)
    repo = HEAD["Repository"]
    commit = Commits.Commit(message, repo.head._head, repo.head, diffs)
    repo.add_log(Log("commit", commit))
    repo.head._head = commit
    Service_func.update_dict({}, _index)
    Service_func.save_object("Repository", repo, _HEAD)
    print("commit")


def reset():
    HEAD = Service_func.get_dict_objects(_HEAD)
    repo = HEAD["Repository"]
    commit = repo.head._head
    repo.add_log(Log("reset", commit))
    dict = Service_func.get_dict_objects(_index)["Changes"]
    for dif in commit.diffs:
        dict[dif.name] = dif.file
    Service_func.update_dict(dict, _index)
    repo.head._head = commit.prev_commit
    Service_func.save_object("Repository", repo, _HEAD)
    print("reset")


def status():
    repo = Service_func.get_object("Repository", _HEAD)
    dict = Service_func.get_dict_objects(_working_dir)
    commit_dict = Service_func.get_dict_objects(_index)
    if dict:
        print("You have unsaved changes:\n")
        for file_name in dict.keys():
            print(file_name)
        print('\n\nYou can add this files to repository and save it')

    elif not commit_dict:
        print("This changes prepare to commit")
        for file_name in commit_dict.keys():
            print(file_name)
    else:
        print("No changes to commit")


def log():
    repo = Service_func.get_object(_HEAD, "Repository")
    repo.get_log()


def check():
    print("check")
