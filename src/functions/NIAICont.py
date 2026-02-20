
import numpy as np
import matplotlib.pyplot as plt
import datetime
import nidaqmx
import nidaqmx.stream_readers

from nidaqmx.constants import TerminalConfiguration, VoltageUnits, AcquisitionType 
from scipy.fft import rfft, rfftfreq

# USER VARIABLES
channelNo = 2
FS = 10000
TS = 1
WW = 1
Vmax = 2
Vmin = -Vmax

window = int(FS * WW)
SPC = int(TS * FS)

buffer = np.zeros(SPC)
ds = np.zeros(FS * 10)

time_vector = np.arange(len(ds)) / FS

plt.ion()
fig, (ax1, ax2, ax3) = plt.subplots(3,1)
fig.suptitle('Continuous AI Acquisition')

ax1.set_ylabel('Voltage [V]')
ax2.set_ylabel('Voltage [V]')
ax3.set_xlabel('Frequency [Hz]')
ax3.set_ylabel('PSD [V/√Hz]')

with nidaqmx.Task() as AI:

    AI.ai_channels.add_ai_voltage_chan(
        f'Dev1/ai{channelNo}',
        terminal_config=TerminalConfiguration.RSE,
        min_val=Vmin,
        max_val=Vmax,
        units=VoltageUnits.VOLTS
    )

    AI.timing.cfg_samp_clk_timing(
        rate=FS,
        sample_mode=AcquisitionType.CONTINUOUS,
        samps_per_chan=SPC
    )

    reader = nidaqmx.stream_readers.AnalogSingleChannelReader(AI.in_stream)

    while True:

        reader.read_many_sample(buffer, number_of_samples_per_channel=SPC)

        ds = np.roll(ds, -SPC)
        ds[-SPC:] = buffer

        xf = rfftfreq(SPC, 1/FS)
        yf = rfft(buffer)

        ax1.clear()
        ax2.clear()
        ax3.clear()

        ax1.plot(time_vector[-window:], ds[-window:])
        ax2.plot(time_vector, ds)
        ax3.loglog(xf, np.abs(yf))

        plt.pause(0.001)
        

        
    
                                    
    
