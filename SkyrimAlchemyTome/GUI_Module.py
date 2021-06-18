import sys, sqlite3
import GUI
from PyQt5.QtWidgets import QApplication,QMainWindow, QTableWidgetItem

class GUIClass(QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("alchemy.sqlite")
        self.loadTables()


        self.Functions()

    def Functions(self):
        self.mainTabWidget.currentChanged.connect(self.MainLableTextChange)

    def MainLableTextChange(self, tabIndex):
        if tabIndex == 0:
            self.currentSpaceLabel.setText("Ingredients and Effects")
        elif tabIndex == 1:
            self.currentSpaceLabel.setText("Alchemy Lab")

    def loadTables(self):
        # Effects
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM Effects").fetchall()
        self.tableWidget_effects.setRowCount(len(result))
        self.tableWidget_effects.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget_effects.setItem(i, j, QTableWidgetItem(str(val)))

        # Ingredients
        stringa = ""
        ings = cur.execute("SELECT Name FROM Ingredients").fetchall()
        for i in ings:
            ingrName = i[0]
            stringa += ingrName + ": "
            for eff in cur.execute(f'SELECT Effect FROM HasEffect WHERE Ingredient=="{ingrName}"'):
                stringa += eff[0] + ", "
            print(stringa)
            stringa = ""