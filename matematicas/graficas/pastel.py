import matplotlib.pyplot as plt
import numpy as np

def pastel(figura, xs, ys):
    figura.pie(ys, labels=xs, autopct="%1.1f%%")