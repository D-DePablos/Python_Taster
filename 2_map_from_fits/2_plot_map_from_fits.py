

#---- Imports ----------------------------------------------------------#

from os import listdir                  #For finding FITS files
from os.path import isfile, join        #For finding FITS files
import sunpy.map                        #For making maps
import matplotlib.pyplot as plt         #For plotting
import sunpy.cm                         #For solar colourmaps

#---- Inputs -----------------------------------------------------------#

data_path = ('/Users/alexanderjames/Documents/PhD/Python_Code'
             '/Python_Taster/2_map_from_fits/')

#---- Read Data --------------------------------------------------------#

#Find all FITS files in the data_path
files = [data_path+f for f in listdir(data_path) if isfile(join(data_path, f))
         and '.fits' in f]

print(files)                            #See a list of the files it found

smap = sunpy.map.Map(files[0])          #Make a map from the file

data = smap.data                        #Get data from map

#---- Plotting ---------------------------------------------------------#

fig = plt.figure()                      #Set up a blank Figure
ax = fig.add_subplot(111)               #Set up a blank axis in the Figure
smap.plot()                             #Plot the Map
plt.savefig('map_from_fits.png')       #Save the Figure
plt.show()                              #Show the Figure
