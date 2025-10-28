from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage, QPainter
from PySide6.QtCore import Qt, QSize
import numpy as np


class RGBImageWidget(QWidget):
    """
    A QWidget that displays raw RGB image data (uint8, shape=(h, w, 3)).
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._qimage = None

    def setImage(self, rgb_array: np.ndarray):
        """
        Set the image to display.
        :param rgb_array: A numpy array of shape (height, width, 3), dtype=np.uint8
        """
        if rgb_array is None:
            self._qimage = None
            self.update()
            return

        if rgb_array.ndim != 3 or rgb_array.shape[2] != 3:
            raise ValueError("Input must have shape (height, width, 3)")

        height, width, _ = rgb_array.shape
        bytes_per_line = 3 * width
        self._qimage = QImage(
            rgb_array.data, width, height, bytes_per_line, QImage.Format_RGB888
        ).copy()  # copy() ensures the data is safely owned

        self.update()  # trigger repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        if self._qimage:
            # scale the image to fit the widget
            target_rect = self.rect()
            painter.drawImage(target_rect, self._qimage)
        else:
            painter.fillRect(self.rect(), Qt.black)

    def sizeHint(self) -> QSize:
        """Default widget size hint."""
        if self._qimage:
            return QSize(self._qimage.width(), self._qimage.height())
        return QSize(640, 480)
