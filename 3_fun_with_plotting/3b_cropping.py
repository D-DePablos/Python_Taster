#-----------------------------------------------------------------------------#
#-------------------- How to Crop a Submap from an Image ---------------------#
#------------------------------ Alexander James ------------------------------#
#-----------------------------------------------------------------------------#

#---- Imports ----------------------------------------------------------------#

import os                                   #for getting working directory
from os import listdir                      #for finding FITS files
from os.path import isfile, join            #for finding FITS files
import sunpy.map                            #for making maps
import matplotlib.pyplot as plt             #for plotting

import astropy.units as u                   #for giving arcseconds
from astropy.coordinates import SkyCoord    #for coordinates
from matplotlib import patches              #for drawing boxes

#---- Inputs -----------------------------------------------------------------#

cwd = os.getcwd()                           #Get current working directory
cwd = cwd + '/3_fun_with_plotting/'         #Specify current working directory

# Define a region of interest
x0 = -300 * u.arcsec                        #Centre x-coordinate
y0 = -300 * u.arcsec                        #Centre y-coordinate
length = 250 * u.arcsec                     #Length of box
height = 250 * u.arcsec                     #Height of box

#---- Read Data --------------------------------------------------------------#

#Find all FITS files in the data_path
files = [cwd+f for f in listdir(cwd) if isfile(join(cwd, f)) and '.fits' in f]
files = sorted(files) #sort alphabetically to get them in date-order

smap1 = sunpy.map.Map(files[0]) #Make first map

#---- Cropping ---------------------------------------------------------------#

#Create coordinates of submap corners
bottom_left = SkyCoord(x0 - length, y0 - length, frame=smap1.coordinate_frame)
top_right = SkyCoord(x0 + length, y0 + length, frame=smap1.coordinate_frame)

#Create submap
smap2 = smap1.submap(bottom_left, top_right)

#---- Plotting ---------------------------------------------------------------#

fig = plt.figure(figsize=(10,4))                #Set up a blank Figure

ax1 = fig.add_subplot(1,2,1, projection=smap1)  #1 row, 2 columns, 1st axis
smap1.plot()                                    #Plot the first Map on axis 1
ax1.grid(False)                                 #Turn off coordinate grid
#Draw a box of the submap area on the full image
smap1.draw_rectangle(bottom_left, length*2, height*2)

ax2 = fig.add_subplot(1,2,2, projection=smap2)  #1 row, 2 columns, 2nd axis
smap2.plot()                                    #Plot the second Map on axis 2
ax2.grid(False)                                 #Turn off coordinate grid

plt.savefig(cwd+'cropping.png')                     #Save the Figure
plt.show()                                      #Show the Figure
