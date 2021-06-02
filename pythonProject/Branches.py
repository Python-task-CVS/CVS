import Service_func
import os
import datetime
from Commits import Commit


class BranchList:
    def __init__(self, path):
        self.path = path
        self.branches = os.path.join(path, "branches_info.txt")
        Service_func.init_dict_object(self.branches)
        self.create_branch("main", None)

    def create_branch(self, name, commit):
        """Добавление ветки в репозиторий"""
        path = os.path.join(self.path, name)
        branch = Branch(path, name, commit)
        Service_func.save_object(name, branch, self.branches)


class Branch:
    def __init__(self, path, name, head_commit):
        self.name = name
        self.path = path
        self._head = head_commit
        self._date_creation = datetime.datetime.now().strftime("%d, %B %Y, %I:%M%p")
        self.last_change = self._date_creation
        self.commits = os.path.join(path, "commits.txt")
        Service_func.init_dict_object(self.commits)
        if self._head is not None:
            Service_func.save_object(head_commit.number, head_commit, self.commits)

    def add_commit(self, commit):
        self._head = commit
        Service_func.save_object(commit.number, commit, self.commits)

    def remove_commit(self):
        if self._head.prev_commit is None:
            return False
        self._head = self._head.prev_commit
        return True
