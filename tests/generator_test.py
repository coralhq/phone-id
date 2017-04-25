from phoneid import anything

from nose.tools import ok_
from nose.tools import eq_
import unittest


class GeneratorTest(unittest.TestCase):

	def test_anything(self):
		length = 8
		international_prefix = False

		result = anything(length, international_prefix)

		ok_(result.startswith('0'),
			msg='With international_prefix = False then it should be prefixed with 0')

		cleaned = result[1:]

		count = len(cleaned)
		count = count - 1 if cleaned.startswith('8315') else count
		count = count - 3

		eq_(count, length,
			msg='Length should be exactly as parameterized')

