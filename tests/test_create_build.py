import unittest
from mock import Mock


class CreateBuildTests(unittest.TestCase):
    def setUp(self):
        self.exampleMessage = {'payload': {'repository':{'git_url':'biz'}}}

    def tearDown(self):
        pass

    def test_created_with_uid(self):
        from ploy.build import createBuild
        dependencies = Mock()
        newBuild = createBuild(dependencies, self.exampleMessage)
        self.assertEqual(5, len(newBuild.id))
        newBuild2 = createBuild(dependencies, self.exampleMessage)
        newBuild3 = createBuild(dependencies, self.exampleMessage)
        newBuild4 = createBuild(dependencies, self.exampleMessage)
        ids = [b.id for b in (newBuild,newBuild2,newBuild3,newBuild4)]
        self.assertEqual(4, len(set(ids)))

    def test_sets_status_and_ts(self):
        from ploy.build import createBuild
        dependencies = Mock()
        self.clock = Mock()
        dependencies.getClock.return_value = self.clock
        newBuild = createBuild(dependencies, self.exampleMessage)
        self.assertEqual('created', newBuild.status)
        self.assertEqual(self.clock.now(), newBuild.created)

    def test_gets_info_from_github_event(self):
        from ploy.build import createBuild
        dependencies = Mock()
        newBuild = createBuild(dependencies, self.exampleMessage)
        self.assertEqual(self.exampleMessage['payload']['repository']['git_url'],
                         newBuild.repositoryGitUrl)