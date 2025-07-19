from PyQt5.QtWidgets import QFileDialog, QMessageBox
from .mosaic_preview_dialog_base import Ui_MosaicPreviewDialogBase
from PyQt5.QtWidgets import QDialog
import os
from .scripts.processor import process_footprint, process_geoimage, process_mosaic

class MosaicPreviewDialog(QDialog, Ui_MosaicPreviewDialogBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.selectFolderButton.clicked.connect(self.select_folder)
        self.runButton.clicked.connect(self.run_selected)
        self.clearButton.clicked.connect(self.clear_output)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folderLineEdit.setText(folder)
            self.folderStatusLabel.setText(folder)
        else:
            self.folderStatusLabel.setText("No folder selected.")

    def run_selected(self):
        folder_path = self.folderLineEdit.text().strip()
        if not os.path.isdir(folder_path):
            QMessageBox.critical(self, "Error", "Please select a valid folder.")
            return

        self.outputTextEdit.clear()
        if self.footprintCheckbox.isChecked():
            self.outputTextEdit.append("Running Footprint...")
            process_footprint(folder_path, self.outputTextEdit)
        if self.geoimageCheckbox.isChecked():
            self.outputTextEdit.append("Running GeoImage...")
            process_geoimage(folder_path, self.outputTextEdit)
        if self.mosaicCheckbox.isChecked():
            self.outputTextEdit.append("Running Mosaic...")
            process_mosaic(folder_path, self.outputTextEdit)

    def clear_output(self):
        self.outputTextEdit.clear()
