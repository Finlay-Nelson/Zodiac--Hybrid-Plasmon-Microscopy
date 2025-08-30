# src/gui/led_control_gui.py
import sys
import os

from devices.led import LED

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PySide6.QtCore import Qt

class LEDControlGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LED Voltage Control")
        self.led = LED(max_voltage=5.0)  # limit for user

        self.layout = QVBoxLayout()
        self.label = QLabel("Voltage: 0.00 V")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(500)  # scale slider to 0-5 V in 0.01 V steps
        self.slider.valueChanged.connect(self.update_voltage)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)
        self.setLayout(self.layout)

    def update_voltage(self, value):
        voltage = value / 100  # convert slider integer to float voltage
        self.label.setText(f"Voltage: {voltage:.2f} V")
        try:
            self.led.set_voltage(voltage)
        except Exception as e:
            print(f"Error setting voltage: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = LEDControlGUI()
    gui.show()
    sys.exit(app.exec())

