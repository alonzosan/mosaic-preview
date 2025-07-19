
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog, QFileDialog
from .processor import process_footprint, process_geoimage, process_mosaic

FORM_CLASS, _ = uic.loadUiType(__file__.replace(".py", ".ui"))

class MosaicPreviewDialog(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.selectFolderButton.clicked.connect(self.select_folder)
        self.runButton.clicked.connect(self.run_process)
        self.clearButton.clicked.connect(self.outputTextEdit.clear)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select folder", "")
        if folder:
            self.folderLineEdit.setText(folder)
            self.folderStatusLabel.setText(folder)

    def run_process(self):
        folder = self.folderLineEdit.text()
        self.outputTextEdit.append("Running...")
        if self.footprintCheckbox.isChecked():
            process_footprint(folder, self.outputTextEdit)
        if self.geoimageCheckbox.isChecked():
            process_geoimage(folder, self.outputTextEdit)
        if self.mosaicCheckbox.isChecked():
            process_mosaic(folder, self.outputTextEdit)
