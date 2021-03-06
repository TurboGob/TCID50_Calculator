import argparse
import csv
from pathlib import Path

from application.calculators.tcid50.tcid50_calculator import TCID50Calculator
from application.models.tcid50.dilution import Dilution
from application.models.tcid50.tcid50_input_data_set import TCID50InputDataSet


def process_tcid50(args):
    if args.input_csv_file is None:
        raise RuntimeError("Parameter input_csv_file must be defined.")

    # These should be moved to better OOP classes
    row_content_between_calculations = []
    non_calculation_row_content = []
    individual_calculations = []
    current_dilutions = None

    with open(args.input_csv_file, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        dilution_amount_index = None
        infected_index = None
        uninfected_index = None
        for row in csvReader:
            if len(row) == 0:
                non_calculation_row_content.append(row)
                continue

            if row[0].lower() == "start" or row[0].lower() == "end":
                if current_dilutions is not None and len(current_dilutions) > 0:
                    individual_calculations.insert(len(individual_calculations), current_dilutions)
                if non_calculation_row_content is not None and len(non_calculation_row_content) > 0:
                    row_content_between_calculations.insert(len(row_content_between_calculations), non_calculation_row_content)
                current_dilutions = []
                non_calculation_row_content = []
                dilution_amount_index = None
                infected_index = None
                uninfected_index = None
            elif dilution_amount_index is None or infected_index is None or uninfected_index is None:
                for cell in row:
                    if cell.lower() == "dilution":
                        dilution_amount_index = row.index(cell)
                    elif cell.lower() == "infected":
                        infected_index = row.index(cell)
                    elif cell.lower() == "uninfected":
                        uninfected_index = row.index(cell)
                if dilution_amount_index is None or infected_index is None or uninfected_index is None:
                    non_calculation_row_content.append(row)
            elif dilution_amount_index is not None and infected_index is not None and uninfected_index is not None and len(row) == 3:
                dilution_amount = None
                if '^' in row[dilution_amount_index]:
                    split = row[dilution_amount_index].split('^')
                    val = float(split[0].replace('^', ''))
                    exponent = float(split[1].replace('^', ''))
                    dilution_amount = val ** exponent
                elif 'e' in row[dilution_amount_index]:
                    split = row[dilution_amount_index].split('e')
                    val = float(split[0].replace('e', ''))
                    exponent = float(split[1].replace('e', ''))
                    dilution_amount = val * (10 ** exponent)
                else:
                    dilution_amount = float(row[dilution_amount_index])
                current_dilutions.append(Dilution(dilution_amount, int(row[infected_index]), int(row[uninfected_index])))
            else:
                non_calculation_row_content.append(row)

    if current_dilutions is not None and len(current_dilutions) > 0:
        individual_calculations.insert(len(individual_calculations), current_dilutions)
    if non_calculation_row_content is not None and len(non_calculation_row_content) > 0:
        row_content_between_calculations.insert(len(row_content_between_calculations), non_calculation_row_content)

    results = []
    calculator = TCID50Calculator()
    for requested_calculation in individual_calculations:
        results.append(calculator.calculate(TCID50InputDataSet(requested_calculation)))

    with open(args.input_csv_file.replace('.csv', '_results.csv'), 'w', newline='') as csvfile:
        result_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        index = 0
        for result in results:
            for row in row_content_between_calculations[index]:
                result_writer.writerow(row)

            result_writer.writerow(['start'])
            result_writer.writerow(['Dilution', 'Infected', 'Uninfected', 'Cumulative_Infected', 'Cumulative_Uninfected', 'Percent_infected', '', 'PD', 'TCID50', 'TCID50_per_mL', 'pfu_per_mL'])
            for dilution in result.dilutions:
                result_writer.writerow([
                    dilution.dilution_amount,
                    dilution.infected_total,
                    dilution.uninfected_total,
                    result.dilution_to_cumulative_infected[dilution],
                    result.dilution_to_cumulative_uninfected[dilution],
                    result.dilution_to_percent_infected[dilution],
                    '',
                    result.pd,
                    result.tcid50,
                    result.tcid50_per_milliliter,
                    result.pfu_per_milliliter
                ])
            result_writer.writerow(['end'])
            index += 1

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

tcid50_command_parser = subparsers.add_parser('calculate_tcid50')
tcid50_command_parser.add_argument('input_csv_file')
tcid50_command_parser.set_defaults(func=process_tcid50)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)

