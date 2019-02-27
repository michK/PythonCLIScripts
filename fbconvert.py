import click
import json
import csv
from pprint import pprint


@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def convert(input, output):
    """
        Convert fitbit json file to csv, where INPUT is the fitbit
        json file and OUTPUT is the converted csv file.
    """

    with input as f:
        data_in = json.load(f)

    for line in data_in:
        # print(line)
        output.write(line['dateTime'])
        output.write(', ')
        output.write(line['value'])
        output.write('\n')

if __name__ == '__main__':
    convert()