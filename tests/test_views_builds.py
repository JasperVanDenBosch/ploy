import unittest
from mock import Mock
from pyramid import testing


class BuildsViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_get_builds(self):
        from ploy.views import get_builds
        request = testing.DummyRequest()
        request.context = Mock()
        responseDict = get_builds(request)
        builds = responseDict['builds']
        self.assertEqual(request.context, builds)
