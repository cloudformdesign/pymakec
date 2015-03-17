
from os.path import join as pjoin
from unittest import TestCase
import pymakec


class TestCFiles(TestCase):
    def test_basic(self):
        path = 'tests/fakesrc'
        result = sorted(pymakec.cfiles(path))
        expected = sorted(pjoin(path, f) for f in ('foo.c', 'bar.c', 'main.c'))
        self.assertListEqual(result, expected)


class TestHFiles(TestCase):
    def test_basic(self):
        path = 'tests/fakesrc'
        result = sorted(pymakec.hfiles(path))
        expected = sorted(pjoin(path, f) for f in ('foo.h', 'bar.h'))
        self.assertListEqual(result, expected)
