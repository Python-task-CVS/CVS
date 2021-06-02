import os, sys
import datetime
import Service_func
import Branches
from collections import deque


class Log:
    def __init__(self, command, cmd_object):
        self.command = command
        self.cmd_object = cmd_object
        self.date = cmd_object.date


class Repository:
    def __init__(self, path):
        self.path = path
        self.branches = Branches.BranchList(os.path.join(path, "branches"))
        self.head = Service_func.get_object(self.branches.branches, "main")
        self.log = os.path.join(path, "log.txt")
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
            return ["Log not found. Please, check repository. Call the command 'check out'"]

    def new_log(self, log):
        log_stack = Service_func.get_object(self.log, "log stack")
        log_stack.append(log)
        Service_func.save_object("log stack", log_stack, self.log)


