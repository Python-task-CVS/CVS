import os, sys
import datetime
import shutil

import Service_func
import Branches
from collections import deque
import hashlib



class Log:
    def __init__(self, command, cmd_object):
        self.command = command
        self.cmd_object = cmd_object
        self.date = cmd_object.date


class Repository:
    def __init__(self, path):
        self.path = path
        path = os.path.join(path, ".cvs")
        os.mkdir(path)
        os.mkdir(os.path.join(path, "branches"))
        os.mkdir(os.path.join(path, "service_files"))
        self.branches = Branches.BranchList(os.path.join(path, "branches"))
        self.head = Service_func.get_object(self.branches.branches, "main")
        self.log = os.path.join(path, "log.txt")
        self.files = os.path.join(path, "service_files")
        self.tags = os.path.join(path, "tags.txt")
        Service_func.init_dict_object(self.tags)
        Service_func.init_dict_object(self.log)
        Service_func.save_object("log stack", deque(), self.log)

    def get_log(self):
        """ Возвращает массив строк - описание лога"""
        try:
            log = Service_func.get_object(self.log, "log stack")
            if not log:
                return ["Log is empty. You took no action"]
            out = []
            for act in log:
                out.append(act)
            out.reverse()
            out_str = []
            for act in out:
                out_str.append("Command: {0} {1}\nDate{2}\n".format(act.command, act.cmd_object.name, act.date))
            return out_str
        except Exception:
            return ["Log not found. Please, check repository. Call the command 'check'"]

    def add_log(self, log):
        log_stack = Service_func.get_object(self.log, "log stack")
        log_stack.append(log)
        Service_func.save_object("log stack", log_stack, self.log)

    def add_tag(self, tag, commit):
        Service_func.save_object(tag, commit, self.tags)

    def tag_to_commit(self, tag):
        return Service_func.get_object(self.tags, tag)

    def checkout(self, step):
        commit = self.head._head
        for i in range(step):
            commit = commit.prev_commit
        return commit

    def choose_branch(self, branch_name):
        branch = Service_func.get_object(self.branches.branches, branch_name)
        if branch is not None:
            self.head = branch
        else:
            print("Branch doesn't exist. Do you want to create it?")

    def save_file(self, path):
        try:
            with open(path, 'rb') as file:
                m = hashlib.md5(file.read())
            name = m.hexdigest()
            shutil.copy(path, os.path.join(self.files, name))
            return name
        except FileNotFoundError:
            sys.exit("File {} not found. Please, check repository".format(path))




