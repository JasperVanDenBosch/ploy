import unittest
from mock import Mock, patch


class ProcessTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_obtains_url_and_checks_out_in_temp_dir(self):
        from ploy.process import processJob
        job = Mock()
        job.repositoryGitUrl = 'abc'
        # make dir
        #repository->git_url
        #after = id of push commit
        with patch('ploy.process.git') as git:
            with patch('ploy.process.petname') as petname:
                petname.Generate.return_value = 'pet'
                processJob(job)
                git.Repo.clone_from.assert_called_with('abc', '/tmp/pet')
