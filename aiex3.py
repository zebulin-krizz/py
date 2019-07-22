import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = 'c:\\Python\\data\\ex2data1.txt'
data = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
print(data.head())