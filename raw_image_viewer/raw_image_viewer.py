import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import numpy as np
from raw_image_viewer import RGBImageWidget
from raw_image_viewer import SerialImageLoader
from raw_image_viewer import ui_frontend
from raw_image_viewer import image_processing
from raw_image_viewer import version

class main_window(QMainWindow, ui_frontend.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load the designed UI
        self.rgbImageWidget = RGBImageWidget.RGBImageWidget()
        layout = self.ImageWidget.parentWidget().layout()
        layout.replaceWidget(self.ImageWidget, self.rgbImageWidget)

        self.setWindowTitle("Raw Image Viewer V%s"%version.VERSION)

        self.serial = SerialImageLoader.SerialManager()
        self.comboComport.addItems(self.serial.list_ports())

        self.buttonConnect.pressed.connect(self.onConnect)
        self.buttonRefresh.pressed.connect(self.onRefresh)
        self.buttonDisconnect.pressed.connect(self.onDisconnect)

        self.serial.message_received.connect(self.onNewImage)
        self.serial.error.connect(self.onSerialError)
        self.serial.connected.connect(self.onSerialConnect)
        self.serial.disconnected.connect(self.onSerialDisconnect)

    def onNewImage(self, data):
        pixformat = self.comboPixFormat.currentText()
        framesize_text = self.comboFramesize.currentText()
        framesize = framesize_text.split()[0] if framesize_text else ""
        frame_dimensions = {
            "FRAMESIZE_UXGA": (1600, 1200),
            "FRAMESIZE_SXGA": (1280, 1024),
            "FRAMESIZE_XGA": (1024, 768),
            "FRAMESIZE_SVGA": (800, 600),
            "FRAMESIZE_VGA": (640, 480),
            "FRAMESIZE_CIF": (352, 288),
            "FRAMESIZE_QVGA": (320, 240),
            "FRAMESIZE_96X96": (96, 96),
        }
        
        if pixformat == "PIXFORMAT_RGB565":
            converter_func = image_processing.convert_image_rgb565_to_rgb
        elif pixformat == "PIXFORMAT_GRAYSCALE":
            converter_func = image_processing.convert_image_grayscale_to_rgb
        elif pixformat == "PIXFORMAT_YUV422":
            converter_func = image_processing.convert_image_YUV422_to_rgb
        else:
            return
        if framesize not in frame_dimensions:
            return
        width, height = frame_dimensions[framesize]
        try:
            image = converter_func(data, height, width)
        except Exception as e:
            print("Error ", e)
            self.statusbar.showMessage("Frame Issue: %s"%str(e))
            return
        self.rgbImageWidget.setImage(image)

    def onSerialError(self, text):
        self.statusbar.showMessage("Serial Error: "+text)

    def onSerialConnect(self, text):
        self.statusbar.showMessage("Serial Connect: "+text)

    def onSerialDisconnect(self, text):
        self.statusbar.showMessage("Serial Disconnect: "+text)

    def onConnect(self):
        port = self.comboComport.currentText()
        self.serial.connect(port)

    def onRefresh(self):
        self.comboComport.clear()
        self.comboComport.addItems(self.serial.list_ports())

    def onDisconnect(self):
        self.serial.disconnect()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec())
