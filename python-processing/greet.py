import numpy as np
import pandas as pd

def greet():
    # return pandas and numpy versions
    return 'Pandas version: ' + pd.__version__ + ' Numpy version: ' + np.__version__