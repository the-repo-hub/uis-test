import unittest
from days import get_days


class TestDays(unittest.TestCase):

    def test_days(self):
        self.assertEqual(get_days('2020-05-03') - get_days('2019-05-03'), 366)
        self.assertEqual(get_days('2019-05-03') - get_days('2018-05-03'), 365)
        self.assertEqual(get_days('2018-05-03') - get_days('2018-05-03'), 0)
        self.assertEqual(get_days('2018-03-01') - get_days('2018-02-28'), 1)
        self.assertEqual(get_days('2016-03-01') - get_days('2016-02-28'), 2)
        with self.assertRaises(ValueError
                               ):
            get_days('2018/12/03') - get_days('2018-12-03')

    def test_days_second(self):
        with self.assertRaises(AttributeError):
            get_days(2018) - get_days(2019)


if __name__ == '__main__':
    unittest.main()