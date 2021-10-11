import Service_func
import os
import datetime
from Commits import Commit


class BranchList:
    ''' Здесь хранится путь на док, где хранится сериализованная инфа о ветках.
        Ветки сохраняются как эл-ты класса Branch в доке branches_info.txt '''
    def __init__(self, path):

        self.path = path
        self.branches = os.path.join(path, "branches_info.txt")
        Service_func.init_dict_object(self.branches)
        self.create_branch("main", None) #сразу создадим ветку main

    def create_branch(self, name, commit):
        """Добавление ветки в репозиторий"""
        path = os.path.join(self.path, name)
        branch = Branch(name, commit)
        Service_func.save_object(name, branch, self.branches)


class Branch:
    """ У Ветки есть головной коммит (текущее положение) и родительский (из него появилась ветка)"""
    def __init__(self, name, parent_commit):
        self.name = name
        self._parent = parent_commit
        self._head = self._parent
        #self._date_creation = datetime.datetime.now().strftime("%d, %B %Y, %I:%M%p")
        #self.commits = os.path.join(, "commits.txt")
        #Service_func.init_dict_object(self.commits)
        #if self._head is not None:
        #    Service_func.save_object(_head.number, _head, self.commits)

    def add_commit(self, commit):
        self._head = commit
        #Service_func.save_object(commit.number, commit, self.commits)

    def remove_commit(self):
        if self._head.prev_commit is None:
            return False
        self._head = self._head.prev_commit
        return True