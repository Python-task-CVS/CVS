import os, sys
import datetime
import Service_func






class Repository:
    def __init__(self, path):
        self.path = path
        self.branches = os.path.join(path, "branches")
        Branches.__init__(self.branches)


class Branches:
    def __init__(self, path):
        self.path = path
        self._branches = os.path.join(path, "branches_info.txt")
        self.branches_info = os.path.join(path, "info.txt")
        self.create_branch("main")
        self.main = self.create_branch("main")

    def create_branch(self, name):
        """Добавление ветки в репозиторий"""
        path = os.path.join(self.path, name)
        branch = Branch.__init__(path, name)
        with open(self._branches, 'rb') as branches:
            dict_branches = pickle.load(branches)
        dict_branches[name] = name
        with open(self._branches, 'wb') as branches:
            pickle.dump(dict_branches, branches)
        with open(self.branches_info, 'a') as info:
            info.write("Name: {0} \n Date of creation: {1} \n \n".format(name, branch._date_creation_))
        return branch


class Branch:
    def __init__(self, path, name):
        self.name = name
        self.path = path
        self._head = os.path.join(path, "head.txt")
        self._date_creation = datetime.datetime.now().strftime("%d, %B %Y, %I:%M%p")
        self.last_change = self._date_creation
        self.commits_info = os.path.join(path, "commits.txt")
        self.commits = {}

