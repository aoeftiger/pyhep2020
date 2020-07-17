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

# plotting intra-bunch motion for PyHEADTAIL
def plot_intrabunch(pyht_ring_elements, pyht_beam, slicer, slices0=None):
    slices = pyht_beam.get_slices(slicer, statistics=['mean_y'])

    if slices0:
        l1, = plt.plot(slices0.z_centers, slices0.mean_y * slices0.n_macroparticles_per_slice, zorder=3)
    l2, = plt.plot(slices.z_centers, slices.mean_y * slices.n_macroparticles_per_slice, zorder=4, ls='--')

    for i in range(10):
        for element in pyht_ring_elements:
            element.track(pyht_beam)
        slices = pyht_beam.get_slices(slicer, statistics=['mean_y'])
        l3, = plt.plot(slices.z_centers, slices.mean_y * slices.n_macroparticles_per_slice, color='C7')

    if slices0:
        handles = [l1, l2, l3]
        lables = ['initial', 'final', 'final + :10']
    else:
        handles = [l2, l3]
        lables = ['final', 'final + :10']

    plt.legend(handles, lables,
               loc=2, bbox_to_anchor=(1.05, 1))
    plt.xlabel('$z$ [m]')
    plt.ylabel('BPM signal')
    plt.title('Vertical intra-bunch motion');
