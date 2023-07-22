import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# get the start time
st = time.time()

for  i in range (10000000):
    # if (i%2548==0 and i%2546==0 and i> 97000000):
    if (i>100000000 and i<100000002 ):
        print (" i = " ,i)

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')