from typing import Sequence, Dict

from application.models.tcid50.dilution import Dilution

class TCID50CalculatedDataSet:
    dilutions = []
    dilution_to_cumulative_infected = {}
    dilution_to_cumulative_uninfected = {}
    dilution_to_percent_infected = {}
    pd = 0.0
    tcid50 = 0.0
    tcid50_per_milliliter = 0.0
    pfu_per_milliliter = 0.0

    def __init__(self,
                 dilutions: Sequence[Dilution],
                 dilution_to_cumulative_infected: Dict[Dilution, float],
                 dilution_to_cumulative_uninfected: Dict[Dilution, float],
                 dilution_to_percent_infected: Dict[Dilution, float],
                 pd: float,
                 tcid50: float,
                 tcid50_per_milliliter: float,
                 pfu_per_milliliter: float):
        self.dilutions = dilutions
        self.dilution_to_cumulative_infected = dilution_to_cumulative_infected
        self.dilution_to_cumulative_uninfected = dilution_to_cumulative_uninfected
        self.dilution_to_percent_infected = dilution_to_percent_infected
        self.pd = pd
        self.tcid50 = tcid50
        self.tcid50_per_milliliter = tcid50_per_milliliter
        self.pfu_per_milliliter = pfu_per_milliliter