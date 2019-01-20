import numpy as np
from random import shuffle

def random_array(shape):
    np.random.seed(42)
    array_1 = np.arange(1,shape[0]*shape[1]+1)
    np.random.shuffle(array_1)
    array = array_1.reshape((shape[0], shape[1]))
    return array