# plotting
import numpy as np
from matplotlib import pyplot as plt

import seaborn as sns
sns.set_context('talk', font_scale=1.2, rc={'lines.linewidth': 3})
sns.set_style(
    'whitegrid',
    {'grid.linestyle': ':',
     'grid.color': 'red',
     'axes.edgecolor': '0.5',
     'axes.linewidth': 1.2,
     'legend.frameon': True
    }
)

# PyHEADTAIL path (need github version because of GPU module)
import sys
sys.path = ['/home/oeftiger/gsi/git/PyHEADTAIL/'] + sys.path

# semantic sugar: avoid cuBLAS warning in scikit-cuda
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import skcuda.cublas
