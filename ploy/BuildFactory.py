import datetime
import pkg_resources
from pkg_resources import resource_filename
import random
random.seed()
from ploy.Build import Build

class BuildFactory(object):

    def __init__(self, os):
        self.os = os

    def new(self):
        commit = self.os.run('git show-ref --heads -s')
        commit = commit.strip()
        name = self.generateName()
        initiated = datetime.datetime.now()
        return Build(name, initiated, commit)

    def generateName(self):
        with open(resource_filename('resources','firstnames.txt')) as fid:
            firstnames = fid.readlines()
        with open(resource_filename('resources','lastnames.txt')) as fid:
            lastnames = fid.readlines()
        firstname = firstnames[random.randint(0,len(firstnames)-1)]
        lastname = lastnames[random.randint(0,len(lastnames)-1)]
        name = '{0} {1}'.format(firstname, lastname)
        return name.replace('\n', '')

