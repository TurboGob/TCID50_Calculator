from typing import Sequence, Dict

from application.models.tcid50.dillution import Dillution

class TCID50CalculatedDataSet:
    dillutions = []
    dillution_to_cumulative_infected = {}
    dillution_to_cumulative_uninfected = {}
    dillution_to_percent_infected = {}
    pd = 0.0
    tcid50 = 0.0
    tcid50_per_milliliter = 0.0
    pfu_per_milliliter = 0.0

    def __init__(self,
                 dillutions: Sequence[Dillution],
                 dillution_to_cumulative_infected: Dict[Dillution, float],
                 dillution_to_cumulative_uninfected: Dict[Dillution, float],
                 dillution_to_percent_infected: Dict[Dillution, float],
                 pd: float,
                 tcid50: float,
                 tcid50_per_milliliter: float,
                 pfu_per_milliliter: float):
        self.dillutions = dillutions
        self.dillution_to_cumulative_infected = dillution_to_cumulative_infected
        self.dillution_to_cumulative_uninfected = dillution_to_cumulative_uninfected
        self.dillution_to_percent_infected = dillution_to_percent_infected
        self.pd = pd
        self.tcid50 = tcid50
        self.tcid50_per_milliliter = tcid50_per_milliliter
        self.pfu_per_milliliter = pfu_per_milliliter