#-----------------------------------------------------------------------------#
#------------ Tweaking Image Parameters in Matplotlib ------------------------#
#--------------------- Diego de Pablos ---------------------------------------#
#-----------------------------------------------------------------------------#

#---- Imports ----------------------------------------------------------------#

import matplotlib.pyplot as plt
import numpy as np

#------------------------Inputs ----------------------------------------------#

# We first create a pair of values to plot:
# - Linear space of 2Pi Radians, taking 200 steps
x = np.linspace(0,2*np.pi,200)
y = np.sin(x)
z = np.cosh(x)

#---------------------First Example Plot -------------------------------------#

plt.plot(x,y)   # No given parameters, defaults to...
plt.show()      # Coloured lines!

# ----------------------Plot Parameters --------------------------------------#
# Using plt.style, we can give the plots a general theme:

# For example, we may use any of the default styles
print(plt.style.available)

plt.style.use('seaborn-paper')  # seaborn is a package available in anaconda!
plt.plot(x,y)   # Which improves resulting graph already
plt.show()

#-----------------------Full Custom ------------------------------------------#
# Things we may want to change in our plots:
# - Figure Size
# - Axis Ticks
# - Font parameters
# - Text: Titles, legends, Annotations, ...
# - Line shapes, transparency, points


# First create a figure with the required size and dpi -------------------------
fig = plt.figure(figsize =(10,4),
                 dpi = 150)       # Create a figure with a given size, dpi
ax = plt.gca()


# We may now set the axis ticks to an empty array ------------------------------
ax.get_xaxis().set_ticks([])      # We can set the ticks to an empty array
ax.get_yaxis().set_ticks([])      # So they are not shown


# We can give our figure an overall title and styling --------------------------
plt.suptitle('Results from a Great Mathematical Investigation')
plt.rc('font', family='serif')    # Set parameters prior to creating plots
plt.rc('xtick', labelsize='small')#
plt.rc('ytick', labelsize='small')

# Now create each of the subfigures using the global plot configuration --------
# Subplot 1
ax1 = fig.add_subplot(2,1,1) # Grid of 2*1 columns * rows, figure number 1
plt.title('Sine function')
ax1.plot(x, y, color='k', ls='solid')   # k stands for black, ls is linestyle
ax1.plot(x, -y, color='0.7', ls='dashed') # Can set color as inverse percentage

ax1.get_xaxis().set_ticks([])            # Again, set axis ticks to empty
ax1.set_ylabel('Y 1')                    # And label the y axis



# Subplot 2
ax2 = fig.add_subplot(2,1,2) # Grid of 2*1 columns * rows, figure number 2
plt.title('Hyperbolic Cosine function')
ax2.plot(x, z, '--k', linewidth=1)        # Another way to style each plot

ax2.legend(['The legend'])                  # We may also set a legend
ax2.text(1,200, '"Truly fascinating"')                # And some Text


ax2.set_xlabel('X Value')
ax2.set_ylabel('Y 2')

plt.show()

###############################################################################
# Getting help:

# Even though Python's docs are not as great as the interactive docs inside IDL,
# popular functions have very well explained help sections:

help(plt)
help(ax)
help(fig)

# Documentation: https://matplotlib.org/tutorials/introductory/pyplot.html
