import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import numpy as np
from raw_image_viewer import RGBImageWidget
from raw_image_viewer import SerialImageLoader

from raw_image_viewer import ui_frontend

from raw_image_viewer import image_processing

class main_window(QMainWindow, ui_frontend.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load the designed UI
        self.rgbImageWidget = RGBImageWidget.RGBImageWidget()
        layout = self.ImageWidget.parentWidget().layout()
        layout.replaceWidget(self.ImageWidget, self.rgbImageWidget)

        self.serial = SerialImageLoader.SerialManager()
        self.comboComport.addItems(self.serial.list_ports())

        self.buttonConnect.pressed.connect(self.onConnect)

        self.serial.message_received.connect(self.onNewImage)

    def onNewImage(self, data):
        pixformat = self.comboPixFormat.currentText()
        framesize = self.comboFramesize.currentText()
        
        if pixformat == "PIXFORMAT_RGB565":
            converter_func = image_processing.convert_image_rgb565_to_rgb
        elif pixformat == "PIXFORMAT_GRAYSCALE":
            converter_func = image_processing.convert_image_grayscale_to_rgb
        else:
            return
        if framesize == "FRAMESIZE_96X96":
            width = 96
            heigth = 96
        else:
            return
        try:
            image = converter_func(data, heigth, width)
        except Exception as e:
            print("Error ", e)
            return
        self.rgbImageWidget.setImage(image)

    def onConnect(self):
        port = self.comboComport.currentText()
        self.serial.connect(port)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec())
