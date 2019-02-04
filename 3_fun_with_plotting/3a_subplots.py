#-----------------------------------------------------------------------------#
#------------------------ How to Plot Multiple Images ------------------------#
#------------------------------ Alexander James ------------------------------#
#-----------------------------------------------------------------------------#

#---- Imports ----------------------------------------------------------------#

import os                                   #For getting working directory
from os import listdir                      #For finding FITS files
from os.path import isfile, join            #For finding FITS files
import sunpy.map                            #For making maps
import matplotlib.pyplot as plt             #For plotting

#---- Inputs -----------------------------------------------------------------#

cwd = os.getcwd() +'/'                      #Get current working directory

#---- Read Data --------------------------------------------------------------#

#Find all FITS files in the data_path
files = [cwd+f for f in listdir(cwd) if isfile(join(cwd, f)) and '.fits' in f]
files = sorted(files)                       #Sort to get them in date-order

smap1 = sunpy.map.Map(files[0])             #Make first map

smap2 = sunpy.map.Map(files[1])             #Make second map

#---- Plotting ---------------------------------------------------------------#

fig = plt.figure(figsize=(10,4))         #Set up a blank Figure. Size in inches

ax1 = fig.add_subplot(1,2,1, projection=smap1)  #1 row, 2 columns, 1st axis
smap1.plot()                                    #Plot the first Map on axis 1
ax1.grid(False)                                 #Turn off coordinate grid

ax2 = fig.add_subplot(1,2,2, projection=smap2)  #1 row, 2 columns, 2nd axis
smap2.plot()                                    #Plot the second Map on axis 2
ax2.grid(False)                                 #Turn off coordinate grid

plt.savefig(cwd+'subplots.png')                 #Save the Figure
plt.show()                                      #Show the Figure
