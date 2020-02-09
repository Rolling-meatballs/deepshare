import numpy as np

def tr_complate():
    a = np.arange(12).reshape(3, 4)
    b = np.empty((4, 3), dtype=int)

    result_1 = np.dot(a, b)
    result_2 = np.dot(b, a)


    a_tr = a.transpose()
