
from .mosaic_preview_dialog import MosaicPreviewDialog
import os

class MosaicPreview:
    def __init__(self, iface):
        self.iface = iface
        self.dlg = None

    def initGui(self):
        from qgis.PyQt.QtWidgets import QAction, QIcon
        self.action = QAction(QIcon(":/plugins/mosaic_preview/icon.png"), "Mosaic Preview", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("&Mosaic Preview", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removePluginMenu("&Mosaic Preview", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        if not self.dlg:
            self.dlg = MosaicPreviewDialog()
        self.dlg.show()
        self.dlg.raise_()
        self.dlg.activateWindow()
