
from PyQt5.QtWidgets import QAction
from .mosaic_preview_dialog import MosaicPreviewDialog

class MosaicPreview:
    def __init__(self, iface):
        self.iface = iface
        self.dialog = None

    def initGui(self):
        self.action = QAction("Mosaic Preview", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("Mosaic Preview", self.action)

    def unload(self):
        self.iface.removePluginMenu("Mosaic Preview", self.action)

    def run(self):
        if not self.dialog:
            self.dialog = MosaicPreviewDialog()
        self.dialog.show()
