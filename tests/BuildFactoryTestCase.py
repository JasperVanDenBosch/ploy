from unittest import TestCase
from mock import Mock
import datetime



class BuildFactoryTestCase(TestCase):

    def test_New_build_has_git_commit_hash_of_head(self):
        from ploy.BuildFactory import BuildFactory
        os = Mock()
        os.run.return_value = '\tabcdef\n'
        factory = BuildFactory(os)
        build = factory.new()
        os.run.assert_called_with('git show-ref --heads -s')
        self.assertEqual(build.commit, 'abcdef')

    def test_New_build_has_a_unique_name(self):
        from ploy.BuildFactory import BuildFactory
        os = Mock()
        factory = BuildFactory(os)
        build1 = factory.new()
        build2 = factory.new()
        self.assertNotEqual(build1.name, build2.name)

    def test_New_build_knows_when_it_was_created(self):
        from ploy.BuildFactory import BuildFactory
        os = Mock()
        before = datetime.datetime.now()
        factory = BuildFactory(os)
        build = factory.new()
        after = datetime.datetime.now()
        self.assertLess(before, build.initiated)
        self.assertGreater(after, build.initiated)

    def test_Generate_name_creates_unique_names(self):
        from ploy.BuildFactory import BuildFactory
        factory = BuildFactory(Mock())
        names = set()
        for b in range(100):
            name = factory.generateName()
            self.assertNotIn('\n', name)
            names.add(name)
            #print(name)
        self.assertEqual(100, len(names))




