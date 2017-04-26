from nose.tools import ok_
from nose.tools import eq_
from nose.tools import nottest
import unittest

import phoneid


class GeneratorTest(unittest.TestCase):

    @nottest
    def generate_test_(self, func, length, international_prefix):
        result = func(length, international_prefix)

        if not international_prefix:
            ok_(result.startswith('0'),
                msg='With international_prefix = False then it should be prefixed with 0')
        else:
            ok_(result.startswith('+62'),
                msg='With international_prefix = True then it should be prefixed with +62')

        cleaned = result[1:] if not international_prefix else result[3:]

        count = len(cleaned)
        count = count - 1 if cleaned.startswith('8315') else count
        count = count - 3

        eq_(count, length,
            msg='Length should be exactly as parameterized')

    def test_anything_with_length_not_internationally_prefixed(self):
        self.generate_test_(func=phoneid.anything,
                            length=8,
                            international_prefix=False)

    def test_anything_with_length_internationally_prefixed(self):
        self.generate_test_(func=phoneid.anything,
                            length=8,
                            international_prefix=True)

    def test_axis_with_length_not_internationally_prefixed(self):
        self.generate_test_(func=phoneid.axis,
                            length=8,
                            international_prefix=False)

    def test_axis_with_length_internationally_prefixed(self):
        self.generate_test_(func=phoneid.axis,
                            length=8,
                            international_prefix=True)

    def test_byru_with_length_not_internationally_prefixed(self):
        self.generate_test_(func=phoneid.byru,
                            length=8,
                            international_prefix=False)

    def test_byru_with_length_internationally_prefixed(self):
        self.generate_test_(func=phoneid.byru,
                            length=8,
                            international_prefix=True)

    def test_indosat_with_length_not_internationally_prefixed(self):
        self.generate_test_(func=phoneid.indosat,
                            length=8,
                            international_prefix=False)

    def test_indosat_with_length_internationally_prefixed(self):
        self.generate_test_(func=phoneid.indosat,
                            length=8,
                            international_prefix=True)

    def test_lippo_with_length_not_internationally_prefixed(self):
        self.generate_test_(func=phoneid.lippo,
                            length=8,
                            international_prefix=False)

    def test_lippo_with_length_internationally_prefixed(self):
        self.generate_test_(func=phoneid.lippo,
                            length=8,
                            international_prefix=True)

    def test_sampoerna_with_length_not_internationally_prefixed(self):
        self.generate_test_(func=phoneid.sampoerna,
                            length=8,
                            international_prefix=False)

    def test_sampoerna_with_length_internationally_prefixed(self):
        self.generate_test_(func=phoneid.sampoerna,
                            length=8,
                            international_prefix=True)

    def test_smartfren_with_length_not_internationally_prefixed(self):
        self.generate_test_(func=phoneid.smartfren,
                            length=8,
                            international_prefix=False)

    def test_smartfren_with_length_internationally_prefixed(self):
        self.generate_test_(func=phoneid.smartfren,
                            length=8,
                            international_prefix=True)

    def test_telkomsel_with_length_not_internationally_prefixed(self):
        self.generate_test_(func=phoneid.telkomsel,
                            length=8,
                            international_prefix=False)

    def test_telkomsel_with_length_internationally_prefixed(self):
        self.generate_test_(func=phoneid.telkomsel,
                            length=8,
                            international_prefix=True)

    def test_three_with_length_not_internationally_prefixed(self):
        self.generate_test_(func=phoneid.three,
                            length=8,
                            international_prefix=False)

    def test_three_with_length_internationally_prefixed(self):
        self.generate_test_(func=phoneid.three,
                            length=8,
                            international_prefix=True)

    def test_xl_with_length_not_internationally_prefixed(self):
        self.generate_test_(func=phoneid.xl,
                            length=8,
                            international_prefix=False)

    def test_xl_with_length_internationally_prefixed(self):
        self.generate_test_(func=phoneid.xl,
                            length=8,
                            international_prefix=True)

