import unittest
from format_price import format_price


class TestPriceFormatting(unittest.TestCase):

    def test_normal_value(self):
        self.assertEqual(format_price('323452436245.148999'), '323 452 436 245.15')

    def test_value_with_zero_floating_part(self):
        self.assertEqual(format_price('1001.0000'), '1 001')

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            format_price('-1.0')

    def test_bad_string_value(self):
        with self.assertRaises(ValueError):
            format_price('Bad value')

    def test_int_value(self):
        with self.assertRaises(TypeError):
            format_price(123456)

    def test_float_value(self):
        with self.assertRaises(TypeError):
            format_price(1.0)

    def test_bool_value(self):
        with self.assertRaises(TypeError):
            format_price(True)


if __name__=='__main__':
    unittest.main()

