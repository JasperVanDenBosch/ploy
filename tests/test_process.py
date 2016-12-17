import unittest
from mock import Mock, patch


class ProcessTests(unittest.TestCase):
    def setUp(self):
        self.filesys = Mock()
        self.dependencies = Mock()
        self.dependencies.getFilesystem.return_value = self.filesys
        self.filesys.readfile.return_value = ''

    def tearDown(self):
        pass

    def test_obtains_url_and_checks_out_in_temp_dir(self):
        from ploy.process import processBuild
        build = Mock()
        build.repositoryGitUrl = 'abc'
        build.id = 'abc123'
        with patch('ploy.process.git') as git:
            processBuild(build, self.dependencies)
            git.Repo.clone_from.assert_called_with('abc', '/tmp/abc123')

    def test_finds_yml_parses_it_and_stores_instructions(self):
        from ploy.process import processBuild
        build = Mock()
        build.repositoryGitUrl = 'abc'
        build.id = 'abc123'
        self.filesys.readfile.return_value = """
        - hello
        - world
        """
        with patch('ploy.process.git') as git:
            processBuild(build, self.dependencies)
        self.filesys.readfile.assert_called_with('/tmp/abc123/ploy.yml')
        self.assertEqual(2, len(build.steps))
        self.assertEqual('hello', build.steps[0])
        self.assertEqual('world', build.steps[1])



