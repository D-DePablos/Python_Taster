#-----------------------------------------------------------------------------#
#------------------- How to Plot an Image from a FITS File -------------------#
#------------------------------ Alexander James ------------------------------#
#-----------------------------------------------------------------------------#

#---- Imports ----------------------------------------------------------------#

import os                               #For getting working directory
from os import listdir                  #For finding FITS files
from os.path import isfile, join        #For finding FITS files
import sunpy.map                        #For making maps
import matplotlib.pyplot as plt         #For plotting
import sunpy.cm                         #For solar colourmaps

#---- Inputs -----------------------------------------------------------------#

cwd = os.getcwd()                       #Get current working directory
cwd = cwd + '/2_map_from_fits/'         #Specify current working directory

#---- Read Data --------------------------------------------------------------#

#Find all FITS files in the current working directory
files = [cwd+f for f in listdir(cwd) if isfile(join(cwd, f)) and '.fits' in f]

print(files)                            #See a list of the files it found

smap = sunpy.map.Map(files[0])          #Make a map from the file

data = smap.data                        #Get data from map

#---- Plotting ---------------------------------------------------------------#

fig = plt.figure()                      #Set up a blank Figure
ax = fig.add_subplot(111)               #Set up a blank axis in the Figure
smap.plot()                             #Plot the Map
plt.savefig(cwd+'map_from_fits.png')    #Save the Figure
plt.show()                              #Show the Figure
