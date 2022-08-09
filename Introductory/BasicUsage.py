#%% Librerias
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#%% A simple example
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.
#%% Parts of a Figure

"""
FIGURE
The easiest way to create a new Figure is with pyplot:"""
fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

"""
AXES
An Axes is an Artist attached to a Figure that contains a region for plotting data, 
and usually includes two (or three in the case of 3D) Axis objects (be aware of the
difference between Axes and Axis) that provide ticks and tick labels to provide scales 
for the data in the Axes. Each Axes also has a title (set via set_title()), an x-label 
(set via set_xlabel()), and a y-label set via set_ylabel()).

The Axes class and its member functions are the primary entry point to working with 
the OOP interface, and have most of the plotting methods defined on them 
(e.g. ax.plot(), shown above, uses the plot method)"""

"""
AXIS
These objects set the scale and limits and generate ticks (the marks on the Axis) 
and ticklabels (strings labeling the ticks). The location of the ticks is determined 
by a Locator object and the ticklabel strings are formatted by a Formatter. 
The combination of the correct Locator and Formatter gives very fine control over 
the tick locations and labels.
"""

"""
ARTIST
Basically, everything visible on the Figure is an Artist (even Figure, Axes, 
and Axis objects). This includes Text objects, Line2D objects, collections 
objects, Patch objects, etc. When the Figure is rendered, all of the Artists 
are drawn to the canvas. Most Artists are tied to an Axes; such an Artist 
cannot be shared by multiple Axes, or moved from one to another.
"""

#%% Types of inputs to plotting  functions
"""Plotting functions expect numpy.array or numpy.ma.masked_array as input, 
or objects that can be passed to numpy.asarray. Classes that are similar 
to arrays ('array-like') such as pandas data objects and numpy.matrix may 
not work as intended. Common convention is to convert these to numpy.array 
objects prior to plotting. For example, to convert a numpy.matrix: """
b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)
"""
Most methods will also parse an addressable object like a dict, 
a numpy.recarray, or a pandas.DataFrame. Matplotlib allows you provide 
the data keyword argument and generate plots passing the strings 
corresponding to the x and y variables."""
np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
# Descomentar para mostrar las gráficas en la salida del cmd o powershell
#plt.show();
# %%
