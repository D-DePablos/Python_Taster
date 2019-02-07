#-----------------------------------------------------------------------------#
#------------------- How to Plot an Image from a FITS File -------------------#
#------------------------------ Alexander James ------------------------------#
#-----------------------------------------------------------------------------#

#---- Imports ----------------------------------------------------------------#

import matplotlib.pyplot as plt         #For plotting
from os import listdir, getcwd          #For finding FITS files
from os.path import isfile, join        #For finding FITS files
import sunpy.map                        #For making maps

#---- Inputs -----------------------------------------------------------------#

cwd = getcwd() + '/'                    #Get current working directory

levels = [3000]                         #Intensity levels to draw contours at
colors = ['blue']                       #Colours for each contour level

#---- Read Data --------------------------------------------------------------#

#Find all FITS files in the current working directory
files = [cwd+f for f in listdir(cwd) if isfile(join(cwd, f)) and '.fits' in f]

print(files)                            #See a list of the files it found

smap = sunpy.map.Map(files[1])          #Make a map from the file

#---- Plotting ---------------------------------------------------------------#

x0 = smap.bottom_left_coord.Tx.value    #Left x-coordinate
x1 = smap.top_right_coord.Tx.value      #Right x-coordinate
y0 = smap.bottom_left_coord.Ty.value    #Bottom y-coordinate
y1 = smap.top_right_coord.Ty.value      #Top y-coordinate

fig = plt.figure()                      #Set up a blank Figure
ax = fig.add_subplot(111)               #Set up a blank axis in the Figure
smap.plot()                             #Plot the Map
ax.contour(smap.data, levels=levels,             #Draw contours at levels...
           extent=[x0,x1, y0,y1], colors=colors) #...using the map coordinates
plt.savefig(cwd+'contour.png')          #Save the Figure
plt.show()                              #Show the Figure
