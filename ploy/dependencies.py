from ploy.filesystem import Filesystem


class Dependencies(object):

    def getClock(self):
        from datetime import datetime
        return datetime

    def getFilesystem(self):
        return Filesystem()