

class Build(object):

    def __init__(self, name, initiated, commit):
        self.name = name
        self.commit = commit
        self.initiated = initiated

    def stampToFile(self, os):
        template = "name={0}\ninitiated={1}\ncommit={2}"
        os.writeToFile('ploybuild',
            template.format(self.name, self.initiated.isoformat(), self.commit))
