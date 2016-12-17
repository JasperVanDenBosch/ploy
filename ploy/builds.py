from persistent import Persistent


class Builds(Persistent):
    def __init__(self, parent):
        self.__parent__ = parent
        self.__name__ = 'builds'
        self._inner = []

    def append(self, newChild):
        self._inner = self._inner + [newChild]

    def __iter__(self):
        return self._inner.__iter__()

    def __getitem__(self, item):
        for build in self._inner:
            if build.id == item:
                return build
