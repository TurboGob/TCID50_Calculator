from application.models.tcid50.tcid50_input_data_set import TCID50InputDataSet
from application.models.tcid50.tcid50_calculated_data_set import TCID50CalculatedDataSet

class TCID50Calculator:
    def calculate(self, input):
        if type(input) != TCID50InputDataSet:
            raise RuntimeError("Input to the TCID50Calculator must be a TCID50InputDataSet.")

        ordered_dilutions = sorted(input.dilutions, key=lambda x: x.dilution_amount, reverse=True)
        dilution_to_cumulative_infected = {}
        dilution_to_cumulative_uninfected = {}
        dilution_to_percent_infected = {}

        cumulative_infected = 0
        cumulative_uninfected = 0
        for dilution in ordered_dilutions:
            cumulative_uninfected += dilution.uninfected_total
            dilution_to_cumulative_uninfected[dilution] = cumulative_uninfected

        for dilution in sorted(input.dilutions, key=lambda x: x.dilution_amount, reverse=False):
            cumulative_infected += dilution.infected_total
            dilution_to_cumulative_infected[dilution] = cumulative_infected

        dilution_above_closest_to_fifty_percent = None
        pd_above_closest_to_fifty_percent = 100
        pd_below_closest_to_fifty_percent = 0
        for dilution in ordered_dilutions:
            percent_infected = (dilution_to_cumulative_infected[dilution] / float(dilution_to_cumulative_infected[dilution] + dilution_to_cumulative_uninfected[dilution])) * 100
            dilution_to_percent_infected[dilution] = percent_infected
            if percent_infected >= 50 and percent_infected <= pd_above_closest_to_fifty_percent:
                pd_above_closest_to_fifty_percent = percent_infected
                dilution_above_closest_to_fifty_percent = dilution
            elif percent_infected < 50 and percent_infected > pd_below_closest_to_fifty_percent:
                pd_below_closest_to_fifty_percent = percent_infected

        pd = (pd_above_closest_to_fifty_percent - 50) / (pd_above_closest_to_fifty_percent - pd_below_closest_to_fifty_percent)
        tcid50 = 0.0
        tcid50_per_milliliter = 0.0
        pfu_per_milliliter = 0.0
        if dilution_above_closest_to_fifty_percent is not None:
            exponent = int("{:e}".format(dilution_above_closest_to_fifty_percent.dilution_amount).split("e")[1])
            log_of_tcid50 = exponent - pd
            tcid50 = 10 ** log_of_tcid50
            tcid50_per_milliliter = (1 / tcid50) * 100
            pfu_per_milliliter = tcid50_per_milliliter * 0.69

        return TCID50CalculatedDataSet(
            ordered_dilutions,
            dilution_to_cumulative_infected,
            dilution_to_cumulative_uninfected,
            dilution_to_percent_infected,
            pd,
            tcid50,
            tcid50_per_milliliter,
            pfu_per_milliliter
        )