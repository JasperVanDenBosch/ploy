import unittest
from mock import Mock
from pyramid import testing


class RootTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_getitem_interface(self):
        from ploy.root import Root
        root = Root()
        self.assertEqual(root.githubEvents, root['github-events'])
        self.assertEqual(root.builds, root['builds'])
