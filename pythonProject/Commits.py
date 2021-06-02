import Service_func
import datetime


class Commit:
    def __init__(self, name, description, prev_commit, branch, diffs):
        self.name = name
        self.description = description
        self.prev_commit = prev_commit
        self.branches = {branch.name: branch}
        self.diffs = diffs
        Service_func.init_dict_object(self.branches)
        self.date = datetime.datetime.now().strftime("%d, %B %Y, %I:%M%p")
