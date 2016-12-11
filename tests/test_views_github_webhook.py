import unittest

from pyramid import testing


class GithubEventsViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_posted_event_type_and_payload_stored(self):
        from ploy.views import post_github_events
        request = testing.DummyRequest()
        request.context = []
        request.headers['X-GitHub-Event'] = 'explosion'
        request.json_body = {'foo':'bar'}
        info = post_github_events(request)
        lastEvent = request.context[-1]
        self.assertIn('event', lastEvent)
        self.assertEqual('explosion', lastEvent['event'])
        self.assertIn('payload', lastEvent)
        self.assertEqual(request.json_body, lastEvent['payload'])