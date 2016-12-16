from persistent import Persistent
from ploy.githubevents import GithubEvents
from ploy.builds import Builds


class Root(Persistent):
    __parent__ = None
    __name__ = None

    def __init__(self):
        self.githubEvents = GithubEvents(self)
        self.builds = Builds(self)

    def __getitem__(self, key):
        if key == 'github-events':
            return self.githubEvents
        if key == 'builds':
            return self.builds
        raise IndexError