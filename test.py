import unittest

from main import *
from ddt import ddt, data, file_data, idata, unpack

@ddt
class TestMainFunctions(unittest.TestCase):

    def test_calc_heartbeat_tanaka_success(self):
        hrtbt = calc_heartbeat_tanaka(36)
        self.assertEqual(hrtbt, 183)

    @file_data('test_data_calc_bmr.json')
    def test_calc_bmr_success(self, value):
        bmr = calc_bmr(value[0],value[1],value[2])
        self.assertEqual(bmr, value[3])

if __name__ == '__main__':
    unittest.main()