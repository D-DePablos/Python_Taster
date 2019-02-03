#-----------------------------------------------------------------------------#
#------------------- How to Plot an Image from a FITS File -------------------#
#------------------------------ Alexander James ------------------------------#
#-----------------------------------------------------------------------------#

#---- Imports ----------------------------------------------------------------#
from pathlib import Path                # Path Operations
import sunpy.map                        # Mapping
import matplotlib.pyplot as plt         # Plotting

#---- Inputs -----------------------------------------------------------------#
work_dir = Path.cwd() /'2_map_from_fits'     # Formatting Paths is easy
#---- Read Data --------------------------------------------------------------#

filelist = sorted(work_dir.glob('*.fits')) # Selects all files with fits suffix

# Each file has a corresponding index, sort normally, look for .fits extensions
for index, file in enumerate(filelist):

    smap = sunpy.map.Map(str(file))          #Make a map from the file
    #---- Plotting ---------------------------------------------------------------#

    fig = plt.figure()                      #Set up a blank Figure
    ax = fig.add_subplot(1,1,1)             #Set up a blank axis in the Figure
    smap.plot()                             #Plot the Map

    # Now, we may save the particular figure by formatting it per current index:
    plt.savefig(f'{work_dir}/map_from_fits_{index:03d}.png') # 03d -> 00{index}
    plt.show()
