# Integrating GPU libraries for fun and profit

## ...on extending and interfacing HPC simulation tools

**Authors: Adrian Oeftiger and Martin Schwinzerl**

A talk on the PyHEP'20, recorded and [published on Youtube](https://www.youtube.com/watch?v=QjEEO40rCm8&t=01m18s). 
Find the [indico time table here](https://indico.cern.ch/event/882824/timetable/#52-integrating-gpu-libraries-f).
See also the [rendered talk slides on github](https://aoeftiger.github.io/pyhep2020/).

## How To Use

To run the notebook talk.ipynb, you will need the following packages
* numpy
* scipy
* matplotlib (& seaborn)
* pycuda
* scikit-cuda (skcuda)
* [sixtracklib](https://github.com/sixtrack/sixtracklib/)
* [PyHEADTAIL](https://github.com/PyCOMPLETE/PyHEADTAIL) (on develop branch as of 17.07.2020)

... and preferably have an NVIDIA GPU available and CUDA installed ;-)

(For the openCL demo of SixTrackLib you will need to compile it with openCL support (and correspondingly have an openCL platform installed on your environment). It is not a crucial part of the talk though, but do make sure you compile with CUDA support in SixTrackLib's Settings.cmake file.)
