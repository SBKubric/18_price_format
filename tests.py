import unittest
from format_price import format_price


class TestPriceFormatting(unittest.TestCase):

    def test_normal_value(self):
        self.assertEqual(format_price('323452436245.148999'), '323 452 436 245.15')

    def test_value_with_zero_floating_part(self):
        self.assertEqual(format_price('1001.0000'), '1 001')

    def test_value_with_9999_ending(self):
        self.assertEqual((format_price('1,999999')), '2')

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            format_price('-1.0')

    def test_bad_string_value(self):
        with self.assertRaises(ValueError):
            format_price('Bad value')

    def test_bool_value(self):
        with self.assertRaises(ValueError):
            format_price(True)


if __name__=='__main__':
    unittest.main()

