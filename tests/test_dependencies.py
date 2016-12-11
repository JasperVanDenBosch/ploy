import unittest


class DependenciesTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_clock_returns_datetime(self):
        from ploy.dependencies import Dependencies
        dependencies = Dependencies()
        clock = dependencies.getClock()
        from datetime import datetime
        self.assertEqual(datetime, clock)