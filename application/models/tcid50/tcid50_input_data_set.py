from typing import List

from application.models.tcid50.dilution import Dilution

class TCID50InputDataSet:
    dilutions = []

    def __init__(self, dilutions: List[Dilution]):
        self.dilutions = dilutions
