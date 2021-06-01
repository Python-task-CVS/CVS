import difflib
import Service_func



class Difference():
    def __init__(self, changes, version, date):
        self.changes = changes
        self.version = version
        self.date = date


def Get_Difference(old, new):
    diff = difflib.ndiff()


class Branch():
    def __init__(self, rollback, ):
