import unittest
from mock import Mock
from pyramid import testing


class JobsViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_get_job(self):
        from ploy.views import get_jobs
        request = testing.DummyRequest()
        request.context = Mock()
        responseDict = get_jobs(request)
        jobs = responseDict['jobs']
        self.assertEqual(request.context, jobs)
