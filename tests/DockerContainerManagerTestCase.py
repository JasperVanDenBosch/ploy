from unittest import TestCase
from mock import Mock



class DockerContainerManagerTestCase(TestCase):

    def test_On_exit_kills_and_removes_added_containers(self):
        from ploy.DockerContainerManager import DockerContainerManager
        client = Mock()
        with DockerContainerManager(client) as manager:
            # When I add a container
            manager.add('my_container')
            # and exit the context
        # the container is killed and removed
        client.kill.assert_any_call('my_container')
        client.remove_container.assert_any_call('my_container')

    def test_On_exit_without_containers_exits_silently(self):
        from ploy.DockerContainerManager import DockerContainerManager
        client = Mock()
        with DockerContainerManager(client) as manager:
            # When I don't add a container
            pass
            # and exit the context
        # nothing happens

