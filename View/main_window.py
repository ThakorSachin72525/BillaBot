from PySide6.QtWidgets import QMainWindow
from View.ui.main_window_ui import Ui_MainWindow  # import the generated UI class

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 