from typing import Sequence

from application.models.tcid50.dillution import Dillution

class TCID50InputDataSet:
    dillutions = []

    def __init__(self, dillutions: Sequence[Dillution]):
        self.dillutions = dillutions
