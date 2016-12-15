import unittest
from mock import Mock
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
        request.root.jobs = []
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


    def test_creates_job(self):
        from ploy.views import post_github_events
        request = testing.DummyRequest()
        request.root = Mock()
        request.root.jobs = []
        self.clock = Mock()
        request.dependencies = Mock()
        request.dependencies.getClock.return_value = self.clock
        request.context = []
        request.json_body = {'foo': 'bar', 'repository':{'git_url':'baz'}}
        info = post_github_events(request)
        self.assertEqual(1, len(request.root.jobs))
        newjob = request.root.jobs[0]
        self.assertEqual('queued', newjob.status)
        self.assertEqual(self.clock.now(), newjob.queued)
        self.assertEqual('baz', newjob.repositoryGitUrl)
