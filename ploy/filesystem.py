

class Filesystem(object):
    
    def readfile(self, fpath):
        with open(fpath) as fhandle:
            contents = fhandle.read()
        return contents