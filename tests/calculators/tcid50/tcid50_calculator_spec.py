import unittest

from application.calculators.tcid50.tcid50_calculator import TCID50Calculator
from application.models.tcid50.dillution import Dillution
from application.models.tcid50.tcid50_input_data_set import TCID50InputDataSet


class Given_A_TCID50Calculator_And_A_TCID50InputDataset_It_Should_Calculate_A_TCID50CalculatedDataSet(unittest.TestCase):
    def test(self):
        input_dillusions = [Dillution(0.00000001, 0, 8), Dillution(0.000001, 5, 3), Dillution(0.00001, 8, 0), Dillution(0.0000001, 1, 7)]

        output = TCID50Calculator().execute(TCID50InputDataSet(input_dillusions))

        self.assertEqual(output, 5)