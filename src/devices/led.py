# src/devices/led.py
import nidaqmx

class LED:
    """
    Simple LED controller using an analog output channel.
    """

    def __init__(self, channel="Dev1/ao2", max_voltage=10.0):
        self.channel = channel
        self.max_voltage = max_voltage

    def set_voltage(self, voltage):
        """
        Set LED voltage.

        Args:
            voltage (float): 0 to max_voltage
        """
        if not (0.0 <= voltage <= self.max_voltage):
            raise ValueError(f"Voltage must be between 0 and {self.max_voltage} V.")
        
        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(self.channel)
            task.write(voltage, auto_start=True)
            print(f"Analog output on {self.channel} set to {voltage:.2f} V")
