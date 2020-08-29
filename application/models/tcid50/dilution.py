class Dilution:
    dilution_amount = 0.0
    infected_total = 0
    uninfected_total = 0

    def __init__(self, dilution_amount, infected_total, uninfected_total):
        self.dilution_amount = dilution_amount
        self.infected_total = infected_total
        self.uninfected_total = uninfected_total