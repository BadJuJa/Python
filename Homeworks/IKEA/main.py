import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import csv
import design


class Extended(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable('IKEA.csv')

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Extended()
    ex.show()
    sys.exit(app.exec_())
