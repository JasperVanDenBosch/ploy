import unittest
from mock import Mock, patch


class ProcessTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_obtains_url_and_checks_out_in_temp_dir(self):
        from ploy.process import processBuild
        build = Mock()
        build.repositoryGitUrl = 'abc'
        build.id = 'abc123'
        with patch('ploy.process.git') as git:
            processBuild(build)
            git.Repo.clone_from.assert_called_with('abc', '/tmp/abc123')
