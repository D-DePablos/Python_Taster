

#---- Imports ----------------------------------------------------------#

from scipy.io.idl import readsav                    # For reading IDL data
import matplotlib.pyplot as plt                     # For plotting

##import matplotlib.pyplot as plt
##import sunpy.cm
##cmap = plt.get_cmap('sdoaia171')

#---- Inputs -----------------------------------------------------------#

data_path = ('/Users/alexanderjames/Documents/PhD/Python_Code'
             '/Python_Taster/1_map_from_sav/')
sav_file = '20120614_1030_1316_smaparr_0hmi.sav'

#---- Read Data --------------------------------------------------------#

idl_data = readsav(data_path+sav_file)  #Read the sav file

print(idl_data)                         #See what is in this sav file

maps = idl_data.smaparr                 #Take the maps from the sav file
#Note, 'smaparr' is just the name of the IDL variable I saved in my sav
#file. It's an array of submaps! But this will be whatever you decide
#to call your variable in IDL.
#e.g.:
#   IDL > save, smaparr, '20120614_1030_1316_smaparr_0hmi.sav'

print(len(maps))                        #This sav file contains 2 maps

data = maps[0]['data']                  #Take data of the 1st (0th) map

#---- Plotting ---------------------------------------------------------#

fig = plt.figure()                      #Set up a blank Figure
ax = fig.add_subplot(111)               #Set up a blank axis in the Figure
ax.imshow(data, origin='lower',         #Plot data with origin in lower left...
          cmap='Greys_r')               #...and black-grey-white colourmap
plt.savefig('map_from_sav.png')         #Save the Figure
plt.show()                              #Show the Figure

#---- Advanced: Labelling the Axes -------------------------------------#

mymap = maps[0]                         #Take first (0th) map
data = mymap['data']                    #Take data from map

xc = mymap['xc']                        #Centre X-coordinate of map
yc = mymap['yc']                        #Centre Y-coordinate of map
dx = mymap['dx']                        #Width of pixels
dy = mymap['dy']                        #Height of pixels
xpix = len(data[0])                     #Number of pixels in X-direction
ypix = len(data)                        #Number of pixels in Y-direction
xunits = mymap['xunits']                #Unit of coordinates (arcsecs)
yunits = mymap['yunits']                #Unit of coordinates (arcsecs)

left = xc - ((xpix*0.5)*dx)             #X-coordinate of left edge in arcsec
right = xc + ((xpix*0.5)*dx)            #X-coordinate of right edge in arcsec
bottom = yc - ((ypix*0.5)*dy)           #Y-coordinate of bottom edge in arcsec
top = yc + ((ypix*0.5)*dy)              #Y-coordinate of top edge in arcsec

plt.imshow(data, origin='lower', cmap='Greys_r',    #Plot image...
           extent=[left,right,bottom,top])          #...with given coordinates
plt.xlabel(xunits)                      #Label X-axis with units
plt.ylabel(yunits)                      #Label Y-axis with units
plt.savefig('map_from_sav_arcsec.png')  #Save the Figure
plt.show()                              #Show the Figure
