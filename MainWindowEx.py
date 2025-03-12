from PyQt6.QtWidgets import QInputDialog, QTableWidgetItem, QHeaderView
from MainWindow import Ui_MainWindow
import pandas as pd

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.data = pd.read_csv("SampleData2.csv")

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.refresh_data()
        self.pushButton.clicked.connect(self.refresh_data)
        self.pushButton_2.clicked.connect(self.sort_by_price)
        self.pushButton_3.clicked.connect(self.search_symbol_and_reduce)
        self.pushButton_4.clicked.connect(self.add_usd_column)
        self.pushButton_5.clicked.connect(self.add_new_row)
        self.pushButton_6.clicked.connect(self.group_and_statistics)
        self.pushButton_7.clicked.connect(self.delete_by_symbol)

    def refresh_data(self):
        self.tableWidget.setRowCount(self.data.shape[0])
        self.tableWidget.setColumnCount(self.data.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(self.data.columns)
        for row in range(self.data.shape[0]):
            for col in range(self.data.shape[1]):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(self.data.iloc[row, col])))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def sort_by_price(self):
        self.data = self.data.sort_values(by='Price', ascending=True)
        self.refresh_data()

    def search_symbol_and_reduce(self):
        symbol, ok = QInputDialog.getText(self.MainWindow, "Input Symbol", "Enter Symbol to reduce price:")
        if ok and symbol:
            self.data.loc[self.data['Symbol'] == symbol, 'Price'] /= 2
            self.refresh_data()

    def add_usd_column(self):
        self.data['USD'] = self.data['Price'] / 23
        self.refresh_data()

    def add_new_row(self):
        symbol, ok1 = QInputDialog.getText(self.MainWindow, "Input Symbol", "Enter Symbol:")
        price, ok2 = QInputDialog.getDouble(self.MainWindow, "Input Price", "Enter Price:")
        pe, ok3 = QInputDialog.getDouble(self.MainWindow, "Input PE", "Enter PE:")
        if ok1 and ok2 and ok3:
            self.data.loc[len(self.data)] = [symbol, price, pe, price / 23]
            self.refresh_data()

    def group_and_statistics(self):
        grouped = self.data.groupby('Group').agg({'Price': ['mean', 'sum', 'count']})
        grouped.columns = ['_'.join(col) for col in grouped.columns]
        self.data = grouped.reset_index()
        self.refresh_data()

    def delete_by_symbol(self):
        symbol, ok = QInputDialog.getText(self.MainWindow, "Input Symbol", "Enter Symbol to delete:")
        if ok and symbol:
            self.data = self.data[self.data['Symbol'] != symbol]
            self.refresh_data()

    def show(self):
        self.MainWindow.show()