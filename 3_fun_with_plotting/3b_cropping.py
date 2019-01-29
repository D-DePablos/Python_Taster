

#---- Imports ----------------------------------------------------------#

from os import listdir                      #for finding FITS files
from os.path import isfile, join            #for finding FITS files
import sunpy.map                            #for making maps
import matplotlib.pyplot as plt             #for plotting

import astropy.units as u                   #for giving arcseconds
from astropy.coordinates import SkyCoord    #for coordinates
from matplotlib import patches              #for drawing boxes

#---- Inputs -----------------------------------------------------------#

data_path = ('/Users/alexanderjames/Documents/PhD/Python_Code'
             '/Python_Taster/3_fun_with_plotting/')

# Define a region of interest
x0 = -300 * u.arcsec                    #centre x-coordinate
y0 = -300 * u.arcsec                    #centre y-coordinate
length = 250 * u.arcsec                 #length of box
height = 250 * u.arcsec                 #height of box

#---- Read Data --------------------------------------------------------#

#Find all FITS files in the data_path
files = [data_path+f for f in listdir(data_path) if isfile(join(data_path, f))
         and '.fits' in f]
files = sorted(files) #sort alphabetically to get them in date-order

smap1 = sunpy.map.Map(files[0]) #Make first map

#---- Cropping ---------------------------------------------------------#

#Create coordinates of submap corners
bottom_left = SkyCoord(x0 - length, y0 - length, frame=smap1.coordinate_frame)
top_right = SkyCoord(x0 + length, y0 + length, frame=smap1.coordinate_frame)

#Create submap
smap2 = smap1.submap(bottom_left, top_right)

#---- Plotting ---------------------------------------------------------#

fig = plt.figure(figsize=(10,4))                #Set up a blank Figure

ax1 = fig.add_subplot(1,2,1, projection=smap1)  #1 row, 2 columns, 1st axis
smap1.plot()                                    #Plot the first Map on axis 1
ax1.grid(False)                                 #Turn off coordinate grid
#Draw a box of the submap area on the full image
smap1.draw_rectangle(bottom_left, length*2, height*2) 

ax2 = fig.add_subplot(1,2,2, projection=smap2)  #1 row, 2 columns, 2nd axis
smap2.plot()                                    #Plot the second Map on axis 2
ax2.grid(False)                                 #Turn off coordinate grid

plt.savefig('cropping.png')                     #Save the Figure
plt.show()                                      #Show the Figure
