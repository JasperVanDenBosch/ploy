from persistent import Persistent
from ploy.githubevents import GithubEvents
from ploy.jobs import Jobs


class Root(Persistent):
    __parent__ = None
    __name__ = None

    def __init__(self):
        self.githubEvents = GithubEvents(self)
        self.jobs = Jobs(self)

    def __getitem__(self, key):
        if key == 'github-events':
            return self.githubEvents
        if key == 'jobs':
            return self.jobs
        raise IndexError