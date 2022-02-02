import sys
from pathlib import Path
import logging
import os

from file_converter_worker import FileConverterWorker

from PyQt6.QtCore import Qt, QThread
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from ui.MainWindow import Ui_MainWindow

logging.basicConfig(level=logging.DEBUG)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.converted_path = 'converted_pdfs'
        self.dir_files = []
        self.files_to_convert = []
        self.converted_files = []
        self.selected_dir = None
        self.setupUi(self)
        self.show()
        self.dirSelectButton.clicked.connect(self.select_folder)
        self.selectAllCheckbox.stateChanged.connect(
            self.select_all_state_change)
        self.dirList.itemSelectionChanged.connect(
            self.update_selected_items_label)
        self.convertButton.clicked.connect(self.click_convert_button)
        self.convertedList.itemDoubleClicked.connect(self.open_file)

    def open_file(self, item):
        for path in self.converted_files:
            if item.text() == path.name:
                logging.debug(f"File Path to Open: {Path(path)}")
                os.system(f"open '{Path(path)}'")

    def select_folder(self):
        if self.dirEdit.text().strip() == "":
            self.selected_dir = QFileDialog.getExistingDirectory(
                self, "Select Folder", str(Path.home()))
        else:
            self.selected_dir = str(Path(self.dirEdit.text()))
        logging.debug(f"Selected Folder: {self.selected_dir}")
        self.dirEdit.setText(self.selected_dir)
        self.selectedDirLabel.setText(
            f"Files in: /{Path(self.selected_dir).stem}")
        self.update_files_list(self.selected_dir)

    def update_files_list(self, path_str):
        dir_content_generator = Path(path_str).iterdir()
        self.dir_files = [x for x in dir_content_generator if x.is_file() and x.suffix.lower() in [
            '.tif', '.tiff']]
        logging.debug(f"Selected Folder Files: {self.dir_files}")
        self.update_selected_dir_file_list()

    def update_selected_dir_file_list(self):
        self.dirList.clear()
        self.dirList.addItems([x.name for x in self.dir_files])

    def select_all_state_change(self):
        state = self.selectAllCheckbox.checkState()
        logging.debug(f"Checkbox State: {state}")
        if state == Qt.CheckState.Checked:
            self.dirList.selectAll()
        elif state == Qt.CheckState.Unchecked:
            self.dirList.clearSelection()

    def update_selected_items_label(self):
        num_selected = len(self.dirList.selectedItems())
        self.numSelectedLabel.setText(f"{num_selected} files selected")

    def click_convert_button(self):
        self.progressBar.setValue(0)
        self.progressLabel.setText("0%")
        self.numConvertedLabel.setText("0 files converted")
        self.convertedList.clear()
        selected = [item.text() for item in self.dirList.selectedItems()]
        self.files_to_convert = [
            file for file in self.dir_files if file.name in selected]
        logging.debug(f"Selected Items: text={self.files_to_convert}")
        if not (self.files_to_convert[0].parent / self.converted_path).is_dir():
            Path.mkdir(self.files_to_convert[0].parent / self.converted_path)
        self._convert_files_thread()

    def _convert_files_thread(self):
        logging.debug("Entered convert_files_thread...")
        self._thread = QThread()
        self._file_converter_worker = FileConverterWorker(
            self.files_to_convert, self.converted_path)
        self._file_converter_worker.moveToThread(self._thread)
        self._thread.started.connect(self._file_converter_worker.convert_files)
        logging.debug("running convert_files worker...")
        self._file_converter_worker.converted_file.connect(
            self._update_state_when_file_converted)
        self._file_converter_worker.progress.connect(
            self._update_state_progress)
        self._file_converter_worker.finished.connect(
            self._update_state_finish_converting)
        self._thread.finished.connect(self._thread.deleteLater)
        self._thread.start()

    def _update_state_when_file_converted(self, new_file_path: str):
        self.statusbar.showMessage(f"converted {new_file_path.name}")
        self.convertedList.addItem(new_file_path.name)
        self.converted_files.append(new_file_path)

    def _update_state_progress(self, index: int):
        percent = int(index / len(self.files_to_convert) * 100)
        self.progressBar.setValue(percent)
        self.progressLabel.setText(f"{percent}%")
        self.numConvertedLabel.setText(f"{index} files converted")

    def _update_state_finish_converting(self):
        self.statusbar.showMessage("conversion complete...")
        self._thread.quit()
        self._thread.wait()
        msg = QMessageBox.information(
            self, "Info", "File conversion is complete.")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
