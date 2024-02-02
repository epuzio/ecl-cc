"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "jennihutson"

import rhinoscriptsyntax as rs
import Rhino.Geometry
import math
import scriptcontext

np = scriptcontext.sticky['numpy']
sp = scriptcontext.sticky['scipy']
spwavfile = scriptcontext.sticky['scipy.io.wavfile']
signal = scriptcontext.sticky['scipy.signal']

wavfilename = wavfilepath

samplerate, data = spwavfile.read(wavfilename)
data1 = signal.resample(data, nbPoints)
if data1.ndim > 1:
 data1 = data1[:, 0]

sampleNumber = len(data1)

myfft = np.fft.fft(data1)
freq = np.fft.fftfreq(sampleNumber)
if len(values0) == 0:
    prevValues = np.zeros(nbPoints)
else:
    prevValues = values0
    
npvalues = np.zeros_like(prevValues)


mags = abs(myfft)/(sampleNumber/2)
freqsMult = freq * 2* math.pi

dy = sampleNumber/nbPoints

for j in range(nbPoints):
    freqsByJ = freqsMult[:int(sampleNumber/2)] * j * dy #must scale j total length of wave
    sinArr = amplitude*((mags[:int(sampleNumber/2)]*np.sin(freqsByJ)))
    if mode == "additive" or mode == "":
        npvalues[j] = np.sum(sinArr) + prevValues[j]
    elif mode == "multiplicative":
        npvalues[j] = np.sum(sinArr) * prevValues[j]

values = []
for i in range(nbPoints):
    values.append(float(npvalues[i]))