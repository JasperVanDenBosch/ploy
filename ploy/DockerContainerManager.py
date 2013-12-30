

class DockerContainerManager(object):

    def __init__(self, dockerClient):
        self.client = dockerClient
        self.container = None

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self.container:
            self.client.kill(self.container)
            self.client.remove_container(self.container)

    def add(self, container):
        self.container = container
