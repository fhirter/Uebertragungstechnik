import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

sampling_frequency = 1000
filter_frequency = 10
period = 5
signal_frequency = 1/period

duty_cycle = 0.1

# Data for plotting
t = np.linspace(0.0, period, sampling_frequency)

sine = np.sin(2 * np.pi * signal_frequency * t)*325
sawtooth = signal.sawtooth(2 * np.pi * signal_frequency * t*2)*0.5+0.5

pwm = sawtooth > duty_cycle

pwm_inverted = np.array(pwm)

#change signal here
input_signal = pwm*sine

# filter signal
b, a = signal.iirfilter(2, filter_frequency/sampling_frequency, btype='lowpass')
filtered_square = signal.lfilter(b, a, input_signal)

## fourier transform
f_orig = np.fft.fft(input_signal)
f_filtered = np.fft.fft(filtered_square)

## sample frequencies
freq = np.fft.fftfreq(len(filtered_square), d=t[1]-t[0])

figure1, (ax1, ax3) = plt.subplots(2, 1)

ax1.plot(t, input_signal)
ax1.set(xlabel='time (s)', title='Square signal')
ax1.grid()

ax3.bar(freq, abs(f_orig)**2, 0.3)
ax3.set(xlabel='frequency (Hz)', title='Filtered square Signal')
ax3.set_xlim(0, signal_frequency*10)
ax3.grid()
ax3.set_xticks(np.arange(signal_frequency, signal_frequency*10, step=signal_frequency))


# figure2, (ax2, ax4) = plt.subplots(2, 1)
# ax2.plot(t, filtered_square)
# ax2.set(xlabel='time (s)', title='Lowpass filtered square signal')
# ax2.grid()
#
# ax4.bar(freq, abs(f_filtered)**2, 0.1)
# ax4.set(xlabel='frequency (Hz)', title='Lowpass Square signal')
# ax4.set_xlim(0, signal_frequency*10)

plt.show()
