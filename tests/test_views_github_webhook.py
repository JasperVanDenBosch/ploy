import unittest
from mock import Mock, patch
from pyramid import testing


class GithubEventsViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_posted_event_type_and_payload_and_timestamp_stored(self):
        from ploy.views import post_github_events
        request = testing.DummyRequest()
        request.root = Mock()
        request.root.builds = []
        self.clock = Mock()
        request.dependencies = Mock()
        request.dependencies.getClock.return_value = self.clock
        request.context = []
        request.headers['X-GitHub-Event'] = 'explosion'
        request.json_body = {'foo': 'bar', 'repository':{'git_url':'biz'}}
        info = post_github_events(request)
        lastEvent = request.context[-1]
        self.assertIn('event', lastEvent)
        self.assertEqual('explosion', lastEvent['event'])
        self.assertIn('payload', lastEvent)
        self.assertEqual(request.json_body, lastEvent['payload'])
        self.assertIn('received', lastEvent)
        self.assertEqual(self.clock.now(), lastEvent['received'])


    def test_creates_build(self):
        from ploy.views import post_github_events
        request = testing.DummyRequest()
        request.root = Mock()
        request.root.builds = []
        request.dependencies = Mock()
        request.context = []
        request.json_body = {'foo': 'bar'}
        with patch('ploy.views.createBuild') as createBuild:
            info = post_github_events(request)
            event = request.context[-1]
            createBuild.assert_called_with(request.dependencies, event)
            self.assertEqual(1, len(request.root.builds))
            newbuild = request.root.builds[0]
            self.assertEqual(createBuild(), newbuild)
            self.assertEqual(request.root.builds, newbuild.__parent__)
