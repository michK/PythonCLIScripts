import click
import json
import csv


@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def convert(input, output):
    """
        Convert Fitbit json file to csv, where INPUT is the fitbit
        json file and OUTPUT is the converted csv file.
        Packages used: click, json, csv
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
