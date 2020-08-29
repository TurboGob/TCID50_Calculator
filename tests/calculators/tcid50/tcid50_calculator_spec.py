import unittest

from application.calculators.tcid50.tcid50_calculator import TCID50Calculator
from application.models.tcid50.dilution import Dilution
from application.models.tcid50.tcid50_input_data_set import TCID50InputDataSet
from application.models.tcid50.tcid50_calculated_data_set import TCID50CalculatedDataSet
from typing import Sequence

class Given_A_TCID50Calculator_And_A_TCID50InputDataset_It_Should_Calculate_A_TCID50CalculatedDataSet(unittest.TestCase):
    def test(self):
        input_dilutions = [
            Dilution(0.00000001, 0, 8),
            Dilution(0.000001, 5, 3),
            Dilution(0.00001, 8, 0),
            Dilution(0.0000001, 1, 7)
        ]

        output = TCID50Calculator().calculate(TCID50InputDataSet(input_dilutions))

        self.assertEqual(output.dilutions[0].dilution_amount, 0.00001)
        self.assertEqual(output.dilutions[0].infected_total, 8)
        self.assertEqual(output.dilutions[0].uninfected_total, 0)
        self.assertEqual(output.dilutions[1].dilution_amount, 0.000001)
        self.assertEqual(output.dilutions[1].infected_total, 5)
        self.assertEqual(output.dilutions[1].uninfected_total, 3)
        self.assertEqual(output.dilutions[2].dilution_amount, 0.0000001)
        self.assertEqual(output.dilutions[2].infected_total, 1)
        self.assertEqual(output.dilutions[2].uninfected_total, 7)
        self.assertEqual(output.dilutions[3].dilution_amount, 0.00000001)
        self.assertEqual(output.dilutions[3].infected_total, 0)
        self.assertEqual(output.dilutions[3].uninfected_total, 8)

        self.assertEqual(output.dilution_to_cumulative_infected[output.dilutions[0]], 14)
        self.assertEqual(output.dilution_to_cumulative_infected[output.dilutions[1]], 6)
        self.assertEqual(output.dilution_to_cumulative_infected[output.dilutions[2]], 1)
        self.assertEqual(output.dilution_to_cumulative_infected[output.dilutions[3]], 0)

        self.assertEqual(output.dilution_to_cumulative_uninfected[output.dilutions[0]], 0)
        self.assertEqual(output.dilution_to_cumulative_uninfected[output.dilutions[1]], 3)
        self.assertEqual(output.dilution_to_cumulative_uninfected[output.dilutions[2]], 10)
        self.assertEqual(output.dilution_to_cumulative_uninfected[output.dilutions[3]], 18)

        self.assertEqual(output.dilution_to_percent_infected[output.dilutions[0]], 100)
        self.assertEqual(round(output.dilution_to_percent_infected[output.dilutions[1]], 1), 66.7)
        self.assertEqual(round(output.dilution_to_percent_infected[output.dilutions[2]], 1), 9.1)
        self.assertEqual(output.dilution_to_percent_infected[output.dilutions[3]], 0)

        self.assertEqual(round(output.pd, 2), 0.29)
        self.assertEqual(round(output.tcid50, 9), 0.000000513)
        self.assertEqual(round(output.tcid50_per_milliliter, 0), 194748304.0)
        self.assertEqual(round(output.pfu_per_milliliter, 0), 134376330.0)