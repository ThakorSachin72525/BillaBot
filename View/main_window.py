from PySide6.QtWidgets import QMainWindow
from View.ui.main_window_ui import Ui_MainWindow  # import the generated UI class
from Controller.tool_controller import clear_table

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_clearbtn.clicked.connect(self.on_clear_clicked)

    def on_clear_clicked(self):
        clear_table()
        print("Clear button clicked.")

        