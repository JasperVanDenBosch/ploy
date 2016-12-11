from persistent import Persistent
from persistent.list import PersistentList


class Root(Persistent):
    __parent__ = None
    __name__ = None

    def __init__(self):
        githubEvents = PersistentList()
        githubEvents.__parent__ = self
        githubEvents.__name__ = 'github-events'
        self.githubEvents = githubEvents

    def __getitem__(self, key):
        if key == 'github-events':
            return self.githubEvents
        raise IndexError