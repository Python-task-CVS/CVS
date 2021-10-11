import Service_func
import datetime
import hashlib
import shutil

class Commit:
    def __init__(self, description, prev_commit, branch, diffs):
        #self.name = name
        self.description = description
        self.prev_commit = prev_commit
        self.branch = branch #ветка, в которой создан коммит
        self.diffs = diffs
        #Service_func.init_dict_object(self.branche)
        self.date = datetime.datetime.now().strftime("%d, %B %Y, %I:%M%p")

