# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:31:53 2020

@author: rchen
"""

import matplotlib.pyplot as plt
import numpy as np
import wave
from numpy import linalg as LA


def save_data_to_wav(filename, wav, data):
    # round the data to int16 format for writing to .wav file
    data   = data.astype(np.int16)
    outwav = wave.open(filename, 'w')
    outwav.setparams(wav.getparams())
    outwav.setparams(wav.getparams())
    outwav.setnchannels(1)
    # convert data to bytes for storage
    outwav.writeframes(data.tobytes())
    
def read_from_wav(filename):    
    # the output: int16 numpy array
    obj  = wave.open(filename, 'rb')
    data = obj.readframes(-1)
    data = np.frombuffer(data, dtype='int16')
    obj.close()
    return data

fn = "hw3sound.wav" # change to the correct location 
data = read_from_wav(fn)

b = 10000
d= 480000
MSE = 0
## Your work here
ft = np.fft.fft(data) # this give us y
for x in range(0,len(ft)):
    if x > b and x < (d-b):
        ft[x] = 0
print(data-np.fft.ifft(ft))
MSE = (1/d)*LA.norm((data-np.fft.ifft(ft)))**2
    
plt.plot(np.fft.ifft(ft))
plt.show()
print(MSE)


#  Processing of data
#data_processed = np.fft.fft(data) # this give us y 
# now to zero out values
data_processed = np.fft.ifft(ft)


#data_processed = np.zeros(10) # replace this line by your processing steps...##



# store data_processed into .wav file with parameters the same as "sample.wav"
wav = wave.open("hw3sound.wav", 'rb')
save_data_to_wav("output5.wav", wav, data_processed)
wav.close()
