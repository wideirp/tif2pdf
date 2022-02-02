from pathlib import Path
import logging

import img2pdf
from PyQt6.QtCore import QObject, pyqtSignal

logging.basicConfig(level=logging.DEBUG)


class FileConverterWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    converted_file = pyqtSignal(Path)

    def __init__(self, files: list, converted_path: str):
        super().__init__()
        self.files = files
        self.converted_path = converted_path
        self.num_files = len(self.files)
        logging.debug("Inside converter worker")

    def convert_files(self):
        for index, file in enumerate(self.files, 1):
            new_file_path = (file.parent / self.converted_path /
                             file.stem).with_suffix('.pdf')
            with open(new_file_path, 'wb') as f:
                f.write(img2pdf.convert(str(file)))
                self.converted_file.emit(new_file_path)
            self.progress.emit(index)
        self.finished.emit()
