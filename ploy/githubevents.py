from persistent import Persistent


class GithubEvents(Persistent):

    def __init__(self, parent):
        self.__parent__ = parent
        self.__name__ = 'github-events'
        self._inner = []

    def append(self, newChild):
        self._inner = self._inner + [newChild]

    def __iter__(self):
        return self._inner.__iter__()
