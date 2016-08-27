"""
A personal finance parser for my 
exported transaction files, which 
are in CSV format.
"""

import csv
import sys
import tkinter as tk

def process_csv():
    filepath = fileInput.get()
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
        'Checksum': row[0],
        'Debit/Credit': row[3],
        'Value': row[4],
        'Date': row[6],
        'Vendor': row[7],
        'Description': row[8],
        'Account': row[12],
        'Category': row[13]
        }
    return data


root = tk.Tk()
root.title('FBT Transaction Records')
fileInput = tk.Entry(root, width=60)
processButton = tk.Button(root, text='Process Record')
recordList = tk.Text(root)

# Geometry Manager
tk.Label(root, text='CSV Filepath: ').grid(row=0, column=0, sticky=tk.NSEW)
fileInput.grid(row=0, column=1, sticky=tk.NSEW)
processButton.grid(row=0, column=2, sticky=tk.NSEW)
recordList.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)

processButton.config(command=process_csv)

root.mainloop()

