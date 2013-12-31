from unittest import TestCase
from mock import Mock
import datetime
from tests.OperatingSystemMock import OperatingSystemMock



class BuildTestCase(TestCase):

    def test_stampToFile(self):
        from ploy.Build import Build
        os = Mock()
        now = datetime.datetime.utcnow()
        build = Build('John', now, 'abc')
        build.stampToFile(os)
        expectedStamp = 'name=John\ninitiated={0}\ncommit=abc'.format(now.isoformat())
        os.writeToFile.assert_called_with('ploybuild', expectedStamp)




