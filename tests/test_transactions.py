import unittest
from subrent.transactions import *
from subrent import MONTHLY_PLAN


class MyTestCase(unittest.TestCase):
    def test_get_daily_incomes(self):
        daily_incomes = get_daily_incomes('2022-12-01')
        self.assertIsNotNone(daily_incomes)
        self.assertEqual(len(daily_incomes), 1)
        self.assertEqual(daily_incomes[0][1], 7500.)

    def test_get_daily_total_income(self):
        self.assertEqual(get_daily_total_income('2022-12-01'), 7500.)
        self.assertEqual(get_daily_total_income('2022-12-10'), 9500.)

    def test_get_monthly_total_income(self):
        self.assertEqual(get_monthly_total_income('2022-12-01'), 7500.)
        self.assertEqual(get_monthly_total_income('2022-12-05'), 55700.)
        self.assertEqual(get_monthly_total_income('2022-12-20'), 126878.81)

    def test_get_monthly_total_deposit(self):
        self.assertEqual(get_monthly_total_deposit('2022-12-01'), 0.)
        self.assertEqual(get_monthly_total_deposit('2022-12-05'), 3000.)
        self.assertEqual(get_monthly_total_deposit('2022-12-20'), -9400.)


if __name__ == '__main__':
    unittest.main()
