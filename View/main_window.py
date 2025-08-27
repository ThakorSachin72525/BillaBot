from PySide6.QtWidgets import QMainWindow
from View.ui.main_window_ui import Ui_MainWindow  
from Controller.tool_controller import clear_table, get_ids_count

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_clearbtn.clicked.connect(self.on_clear_clicked)

        self.id_count()

    def id_count(self):
        
        count = get_ids_count()
        print(count)
        self.textEdit.append(f"Initial ID count: {count}")
        
    def on_clear_clicked(self):
        clear_table()
        print("Clear button clicked.")
