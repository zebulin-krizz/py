import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = 'c:\\Python\\data\\ex1data2.txt'
data2 = pd.read_csv(path, header=None, names=['Size','Bedrooms','Price'])
print(data2.head())
