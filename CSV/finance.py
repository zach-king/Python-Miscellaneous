"""
A personal finance parser for my 
exported transaction files, which 
are in CSV format.
"""

import csv
import sys

def main(filepath):
    with open(filepath, newline='') as csvfile:
        data = []
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            for i, item in enumerate(row):
                print('\t' + str(i) + ': ' + str(item))
            data.append(parse_row(row))
            print('------------------------------')

def parse_row(row):
    data = {
        'Checksum': data[0],
        'Debit/Credit': data[3],
        'Value': data[4],
        'Date': data[6],
        'Vendor': data[7],
        'Description': data[8],
        'Account': data[12],
        'Category': data[13]
        }
    return data
    


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        filepath = input('CSV Filepath: ')
        main(filepath)