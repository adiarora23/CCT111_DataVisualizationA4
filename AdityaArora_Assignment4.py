"""
Author: Aditya Arora
Class: CCT111H5, Summer 2020
Programming Assignment #4
8/22/2020

Description:
"""

import pandas as pd
import matplotlib.pyplot as plt

measles_reader = pd.read_csv('measles.csv')
print(measles_reader.head())

g = measles_reader.groupby('World_Bank_Income_Level')

# max percentage vaccine graph
g.max().plot(kind='line', figsize=(12, 9))
plt.title('Max percentage for each of the income levels')
plt.xlabel('Income levels')
plt.ylabel('Average percentage')


plt.legend(g.max(), loc='lower right', prop={'size': 9})
plt.show()

# average percentage vaccine graph
plt.figure(figsize=(12, 9))
plt.title('Average percentage for each of the income levels')
plt.xlabel('Income levels')
plt.ylabel('Average percentage')

plt.plot(g.mean())
plt.legend(g.mean(), loc='lower right', prop={'size': 9})
plt.show()
