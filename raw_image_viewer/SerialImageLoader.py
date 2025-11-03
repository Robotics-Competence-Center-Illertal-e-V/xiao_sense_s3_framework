import serial
import serial.tools.list_ports
from PySide6.QtCore import QObject, QThread, Signal


class SerialReaderWorker(QObject):
    """
    Worker class that runs in a separate thread to read binary data
    from the serial port and emit complete messages split by a delimiter.
    """
    message_received = Signal(bytes)
    error = Signal(str)
    finished = Signal()

    def __init__(self, port_name: str, baudrate: int = 115200, delimiter: bytes = b'\xDE\xAD\xBE\xAF'):
        super().__init__()
        self.port_name = port_name
        self.baudrate = baudrate
        self.delimiter = delimiter
        self._running = False
        self._buffer = bytearray()
        self.ser = None

    def start(self):
        """Start reading serial data."""
        print(f"connecting to {self.port_name}, baud {self.baudrate}")
        try:
            self.ser = serial.Serial(self.port_name, self.baudrate, timeout=0.1)
            self._running = True
        except serial.SerialException as e:
            self.error.emit(f"Failed to open port {self.port_name}: {e}")
            self.finished.emit()
            print("failed")
            return
        print("connected")
        while self._running:
            try:
                data = self.ser.read(1024)
                if data:
                    self._buffer.extend(data)
                    while self.delimiter in self._buffer:
                        parts = self._buffer.split(self.delimiter)
                        for msg in parts[:-1]:
                            if msg:
                                self.message_received.emit(bytes(msg))
                        self._buffer = bytearray(parts[-1])
            except serial.SerialException as e:
                self.error.emit(f"Serial error: {e}")
                break

        if self.ser and self.ser.is_open:
            self.ser.close()
        self.finished.emit()

    def stop(self):
        """Stop reading and close the serial port."""
        self._running = False


class SerialManager(QObject):
    """
    High-level class to manage serial connections and integrate with PySide6.
    """
    message_received = Signal(bytes)
    error = Signal(str)
    connected = Signal(str)
    disconnected = Signal(str)

    def __init__(self):
        super().__init__()
        self.thread = None
        self.worker = None

    @staticmethod
    def list_ports() -> list:
        """Return a list of available serial ports."""
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def connect(self, port_name: str, baudrate: int = 115200):
        """Connect to the selected serial port and start reading data."""
        try:
            if self.thread or self.thread.isRunning():
                if self.worker._running:
                    self.error.emit("Already connected to a serial port.")
                    return
                else:
                    print("worker not running")
        except:
            pass

        self.thread = QThread()
        self.worker = SerialReaderWorker(port_name, baudrate)
        self.worker.moveToThread(self.thread)

        # Wire up signals
        self.thread.started.connect(self.worker.start)
        self.worker.message_received.connect(self.message_received)
        self.worker.error.connect(self.error)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.connected.emit(port_name)

    def disconnect(self):
        """Stop reading and disconnect from the serial port."""
        if self.worker:
            self.worker.stop()
            self.disconnected.emit(self.worker.port_name)
            self.worker = None
        if self.thread:
            self.thread.quit()
            self.thread.wait()
            self.thread = None
