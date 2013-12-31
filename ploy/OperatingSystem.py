import os, subprocess


class OperatingSystem(object):

    def writeToFile(self, filename, content):
        with open(filename, 'w') as fid:
            fid.write(content)

    def run(self, command):
        return subprocess.check_output(command, shell=True)

    def putenv(self, *args):
        os.putenv(*args)
