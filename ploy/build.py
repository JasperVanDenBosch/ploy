import string, random
from persistent import Persistent
alphabet = string.ascii_lowercase + string.ascii_uppercase + '0123456789'
IDLENGTH = 5


class Build(Persistent):

    @property
    def __name__(self):
        return self.id


def createBuild(dependencies, message):
    clock = dependencies.getClock()
    build = Build()
    uid = ''.join(random.choice(alphabet) for i in range(IDLENGTH))
    build.id = uid
    build.status = 'created'
    build.created = clock.now()
    build.repositoryGitUrl = message['payload']['repository']['git_url']
    return build