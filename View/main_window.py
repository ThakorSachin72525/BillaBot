from PySide6.QtCore import QThread, QObject, Signal, Slot
from PySide6.QtWidgets import QMainWindow, QFileDialog
from View.ui.main_window_ui import Ui_MainWindow
from Controller.tool_controller import clear_table, get_ids_count, handle_upload_ids


# This new class will perform the long-running task in a separate thread.
class Worker(QObject):
    # These signals will be used to communicate back to the main window.
    finished = Signal(int, int) # (uploaded_count, total_count)
    error = Signal(str) # (error_message)
    
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    @Slot()
    def run(self):
        """
        This method will be executed in the new thread.
        It encapsulates the long-running database operations.
        """
        try:
            uploaded_count, total_count = handle_upload_ids(self.file_path)
            # Emit the finished signal with the results.
            self.finished.emit(uploaded_count, total_count)
        except Exception as e:
            # If an error occurs, emit the error signal.
            self.error.emit(str(e))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_clearbtn.clicked.connect(self.on_clear_clicked)
        self.pushButton_uploadbtn.clicked.connect(self.on_upload_clicked)

        self.id_count()

    def id_count(self):
        
        count = get_ids_count()
        self.textEdit.append(f"Initial ID count: {count}")
        
    def on_clear_clicked(self):
        new_count = clear_table()
        self.textEdit.append("Table cleared.")
        self.textEdit.append(f"New ID count: {new_count}")

    def on_upload_clicked(self):
        """
        Initiates the file upload process on a separate thread.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Excel File",
            "",
            "Excel Files (*.xlsx *.xls)"
        )
        
        if file_path:
            self.textEdit.append("\nAction: 'Upload ID' button clicked.")
            self.textEdit.append(f"Selected file: {file_path}")
            self.textEdit.append("Uploading... this may take a moment.")
            
            # Disable buttons to prevent user from clicking them again.
            self.pushButton_uploadbtn.setEnabled(False)
            self.pushButton_clearbtn.setEnabled(False)

            # 1. Create a QThread object
            self.thread = QThread()
            # 2. Create a worker object
            self.worker = Worker(file_path)
            # 3. Move the worker object to the thread
            self.worker.moveToThread(self.thread)
            
            # 4. Connect signals and slots
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.on_upload_finished)
            self.worker.error.connect(self.on_upload_error)
            
            # 5. Start the thread
            self.thread.start()
        else:
            self.textEdit.append("File selection cancelled.")

    @Slot(int, int)
    def on_upload_finished(self, uploaded_count, total_count):
        """
        This slot is called when the worker thread successfully finishes.
        """
        self.textEdit.append(f"Successfully uploaded {uploaded_count} IDs.")
        self.textEdit.append(f"Total IDs in table: {total_count}")
        # Re-enable the buttons after the task is complete.
        self.pushButton_uploadbtn.setEnabled(True)
        self.pushButton_clearbtn.setEnabled(True)
        # Clean up the thread
        self.thread.quit()
        self.thread.wait()
        
    @Slot(str)
    def on_upload_error(self, error_message):
        """
        This slot is called when an error occurs in the worker thread.
        """
        self.textEdit.append(f"Error during file upload: {error_message}")
        # Re-enable the buttons after the task fails.
        self.pushButton_uploadbtn.setEnabled(True)
        self.pushButton_clearbtn.setEnabled(True)
        # Clean up the thread
        self.thread.quit()
        self.thread.wait()

