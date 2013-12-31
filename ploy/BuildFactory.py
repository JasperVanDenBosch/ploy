import datetime
import random
random.seed()

class BuildFactory(object):

    def __init__(self, os):
        self.os = os

    def new(self):
        commit = self.os.run('git show-ref --heads -s')
        name = self.generateName()
        initiated = datetime.datetime.now()
        return Build(name, initiated, commit)

    def generateName(self):
        with open('resources/firstnames.txt') as fid:
            firstnames = fid.readlines()
        with open('resources/lastnames.txt') as fid:
            lastnames = fid.readlines()
        firstname = firstnames[random.randint(0,len(firstnames)-1)]
        lastname = lastnames[random.randint(0,len(lastnames)-1)]
        name = '{0} {1}'.format(firstname, lastname)
        return name.replace('\n', '')

class Build(object):

    def __init__(self, name, initiated, gitCommitHash):
        self.name = name
        self.gitCommitHash = gitCommitHash
        self.initiated = initiated
