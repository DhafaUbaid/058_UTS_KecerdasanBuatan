# -*- coding: utf-8 -*-
"""UTS_NO_1C

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A4kxjjQKUqv5DKftqsCTnetEcqZNKT79
"""

import numpy as np

inputs = [
    [21.0, 11.5, 32.0, 32.5, 33.0, 53.5, 14.9, 24.5, 5.0, 5.5],
    [41.5, 11.4, 12.2, 12.4, 3.2, 35.4, 14.2, 42.4, 51.2, 5.4],
    [3.5, 8.5, 18.0, 20.5, 30.0, 30.5, 40.0, 40.5, 50.0, 50.5],
    [2.7, 21.8, 25.6, 62.8, 43.6, 23.8, 54.6, 4.8, 52.6, 15.8],
    [2.5, 1.4, 57.2, 47.4, 18.2, 82.4, 49.2, 92.4, 10.2, 10.4],
    [1.5, 6.4, 17.2, 17.4, 18.2, 18.4, 19.2, 19.4, 10.2, 10.4],
]

weights = [
    [1.0, 12.5, 4.0, 22.5, 53.7, 33.5, 6.7, 2.5, 2.0, 5.5],
    [1.2, 21.4, 27.2, 23.4, 55.2, 3.4, 3.2, 4.4, 3.2, 5.4],
    [2.7, 13.8, 2.6, 2.8, 55.6, 52.8, 4.6, 24.8, 6.6, 5.8],
    [2.2, 6.3, 32.2, 7.4, 8.2, 28.4, 9.2, 29.4, 10.2, 10.4],
    [3.5, 18.5, 18.0, 20.5, 30.6, 0.5, 4.0, 4.5, 5.0, 50.5]
]

biases = [1.9, 2.0, 3.5, 3.2, 3.8]

outputs = np.dot(inputs, np.array(weights) . T) + biases
print(outputs)