"""
A personal finance parser for my 
exported transaction files, which 
are in CSV format.
"""

import csv
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *



class FinanceApp(QDialog):
    def __init__(self, parent=None):
        super(FinanceApp, self).__init__(parent)

        self.record = None
        self.createWidgets()
        self.setWindowTitle('FBT Transaction Record Viewer')
        self.resize(1900, 1000)
        self.setWindowState(Qt.WindowMaximized)

    def createWidgets(self):
        layout = QVBoxLayout()
        self.recordTable = QTableWidget(0, 8, self)
        self.recordTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.openButton = QPushButton('Open Record', self)
        layout.addWidget(self.recordTable)
        layout.addWidget(self.openButton)
        self.setLayout(layout)
        self.openButton.clicked.connect(self.process_csv)

    def process_csv(self):
        fname = QFileDialog.getOpenFileName()
        with open(fname) as csvfile:
            data = []
            reader = csv.reader(csvfile, delimiter=',')
            for row_num, row in enumerate(reader):
                self.recordTable.insertRow(row_num)
                parsed_data = self.parse_row(row)
                data.append(parsed_data)
                for i, pair in enumerate(list(parsed_data.items())):
                    key = pair[0]
                    value = pair[1]
                    if parsed_data['Debit/Credit'] == 'Debit':
                        prefix = '- $'
                    elif parsed_data['Debit/Credit'] == 'Credit':
                        prefix = '+ $'
                    else:
                        prefix = ''
                    self.recordTable.setItem(row_num, 0, QTableWidgetItem(parsed_data['Date']))
                    self.recordTable.setItem(row_num, 1, QTableWidgetItem(parsed_data['Account']))
                    self.recordTable.setItem(row_num, 2, QTableWidgetItem(parsed_data['Vendor']))
                    self.recordTable.setItem(row_num, 3, QTableWidgetItem(parsed_data['Description']))
                    self.recordTable.setItem(row_num, 4, QTableWidgetItem(parsed_data['Category']))
                    self.recordTable.setItem(row_num, 5, QTableWidgetItem(prefix + str(parsed_data['Value'])))
                    self.recordTable.setItem(row_num, 6, QTableWidgetItem(parsed_data['Debit/Credit']))
        self.recordTable.resizeColumnsToContents()

    def parse_row(self, row):
        data = {
            'ID': row[0],
            'Debit/Credit': row[3],
            'Value': row[4],
            'Date': row[6],
            'Vendor': row[7],
            'Description': row[8],
            'Account': row[12],
            'Category': row[13]
            }
        return data
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FinanceApp()
    window.show()
    sys.exit(app.exec_())

    
