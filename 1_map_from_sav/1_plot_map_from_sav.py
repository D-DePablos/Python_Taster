#-----------------------------------------------------------------------------#
#--------------------- How to Plot an IDL Map in Python ----------------------#
#------------------------------ Alexander James ------------------------------#
#-----------------------------------------------------------------------------#

#---- Imports ----------------------------------------------------------------#

import os                               #For getting working directory
from scipy.io.idl import readsav        #For reading IDL data
import sunpy.cm                         #For solar colourmaps
import matplotlib.pyplot as plt         #For plotting

#---- Inputs -----------------------------------------------------------------#

cwd = os.getcwd() + '/'                 #Get current working directory

sav_file = 'aia_193_maps.sav'           #Name of input '.sav' file

#---- Read Data --------------------------------------------------------------#

idl_data = readsav(cwd+sav_file)  #Read the sav file

print(idl_data)                         #See what is in this sav file

maps = idl_data.maps                    #Take the maps from the sav file
#Note: this will depend on what you decide to call your variable in IDL.
#e.g.:
#   IDL > save, filename='aia_193_maps.sav', maps, /compress

print(len(maps))                        #This sav file contains 2 maps

data = maps[0]['data']                  #Take data of the 1st (0th) map

#---- Plotting ---------------------------------------------------------------#

cmap = plt.get_cmap('sdoaia193')        #Choose AIA 193 colormap

fig = plt.figure()                      #Set up a blank Figure
ax = fig.add_subplot(111)               #Set up a blank axis in the Figure
ax.imshow(data, origin='lower',         #Plot data with origin in lower left...
          cmap=cmap, vmin=0, vmax=3000) #...with our chosen colormap
plt.savefig(cwd+'map_from_sav.png', dpi=200) #Save the Figure
plt.show()                              #Show the Figure

#---- Advanced: Labelling the Axes -------------------------------------------#

mymap = maps[0]                         #Take first (0th) map
data = mymap['data']                    #Take data from map

xc = mymap['xc']                        #Centre X-coordinate of map
yc = mymap['yc']                        #Centre Y-coordinate of map
dx = mymap['dx']                        #Width of pixels
dy = mymap['dy']                        #Height of pixels
xpix = len(data[0])                     #Number of pixels in X-direction
ypix = len(data)                        #Number of pixels in Y-direction

left = xc - ((xpix*0.5)*dx)             #X-coordinate of left edge in arcsec
right = xc + ((xpix*0.5)*dx)            #X-coordinate of right edge in arcsec
bottom = yc - ((ypix*0.5)*dy)           #Y-coordinate of bottom edge in arcsec
top = yc + ((ypix*0.5)*dy)              #Y-coordinate of top edge in arcsec

plt.imshow(data, origin='lower', cmap=cmap,     #Plot image...
           vmin=0, vmax=3000,                   #...with saturation limits...
           extent=[left,right,bottom,top])      #...with specified coordinates
plt.savefig(cwd+'map_from_sav2.png', dpi=200)   #Save the Figure
plt.show()                              #Show the Figure
