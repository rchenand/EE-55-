# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:34:18 2020

@author: rchen
"""

'''import numpy as np
import wave 
obj = wave.open("sample.wav", 'rb')
data = obj.readframes(-1)
data = np.frombuffer(data, dtype='int16')'''


#rate, aud_data = scipy.io.wavfile.read(simplewave.wav)
#rate, aud_data = 44000, np.random.random((9218368,))

import numpy as np
import matplotlib.pyplot as plt
import wave
obj = wave.open("hw3sound.wav", 'rb')
data = obj.readframes(-1)
data = np.frombuffer(data, dtype = 'int16')
ft = np.fft.fft(data, norm = 'ortho')
plt.plot(ft)
plt.show()
