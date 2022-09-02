# Dependencies
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from math import sqrt
# Our integral approximation function
def integral_approximation(f, a, b):
    return (b-a)*np.mean(f)

def square(list):
    return [i ** 2 for i in list]
f = open(r"test_noise1.raw", "r")  #"test_noise1_slew.raw" for other circuit
i = 0
freqArr = [];
noiseArr = [];
for x in f:
  if i>839:
        break
  if i%4==0:
      freqArr.append(float((x.strip()).split("\t")[1]))
  elif i%4==1:
      noiseArr.append(float(x.strip(" ")))
  i=i+1

freqArr = np.array(freqArr)
noiseArr = np.array(square(noiseArr))
# Bounds of integral
a = min(freqArr)
b = max(freqArr)
# Approximate integral
approx = integral_approximation(noiseArr,a,b)

print(sqrt(approx))
