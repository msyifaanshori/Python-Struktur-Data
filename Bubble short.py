import random
import time
import copy
import sys
import matplotlib.pyplot as plt

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        # Optimasi: Cek jika ada pertukaran dalam satu pass
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        # Jika tidak ada pertukaran, array sudah terurut
        if not swapped:
            break
    return data