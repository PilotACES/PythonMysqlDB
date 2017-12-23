# @Time     : 2017/12/23 14:34
# @Author   : Johnny Mo
# @File     : Console.py
class Console(object):
    def __init__(self):
        self._id = 0
        self._console = ''
        self._time = ''
        self._commit = ''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def console(self):
        return self._console

    @console.setter
    def console(self, value):
        self._console = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def commit(self):
        return self._commit

    @commit.setter
    def commit(self, value):
        self._commit = value
