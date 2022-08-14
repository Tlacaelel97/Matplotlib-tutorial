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

# %% CODING STYLES
"""
Tenemos basicamente dos formas de usar MAtplotlib:
        Explicitly create Figures and Axes, and call methods on them (the "object-oriented (OO) style").

        Rely on pyplot to automatically create and manage the Figures and Axes, and use pyplot functions 
        for plotting.
"""
"""Mediante OO-style"""
x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend();  # Add a legend.

"""Mediante pyplot-style"""
x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend();

"""
OO style es muy util para funciones complicadas y scripts para
proyectos grandes, mienrtas que pyplot puede ser usada para 
graficaciones rápidas
"""

#%% MAKING HELPER FUNCTIONS

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

#usamos esta funcion para hacer las siguientes gráficas
data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'});

#%% Styling Artists
"""
Most plotting methods have styling options for the Artists, accessible either 
when a plotting method is called, or from a "setter" on the 
Artist. In the plot below we manually set the color, linewidth, and 
linestyle of the Artists created by plot, and we set the linestyle 
of the second line after the fact with set_linestyle.
"""
fig, ax = plt.subplots(figsize=(5, 2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':');

# COLOR
"""
Some Artists will take multiple colors. i.e. for a scatter plot, the 
edge of the markers can be different colors from the interior:
"""
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k');

# LINEWIDHTS, LINESTYLES AND MARKERSIZES
"""
Marker size depends on the method being used. plot specifies markersize 
in points, and is generally the "diameter" or width of the marker. 
scatter specifies markersize as approximately proportional to the 
visual area of the marker. There is an array of markerstyles available 
as string codes (see markers), or users can define their own MarkerStyle 
(see Marker reference):
"""
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(data1, 'o', label='data1')
ax.plot(data2, 'd', label='data2')
ax.plot(data3, 'v', label='data3')
ax.plot(data4, 's', label='data4')
ax.legend();

#%% LABELING PLOTS
# AXES LABELS AND TEXT
"""set_xlabel, set_ylabel, and set_title are used to add text in the 
indicated locations (see Text in Matplotlib Plots for more discussion). 
Text can also be directly added to plots using text:
"""
mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# the histogram of the data
n, bins, patches = ax.hist(x, 50, density=1, facecolor='C0', alpha=0.75)

ax.set_xlabel('Length [cm]')
ax.set_ylabel('Probability')
ax.set_title('Aardvark lengths\n (not really)')
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
ax.grid(True);

"""
All of the text functions return a matplotlib.text.Text instance. 
Just as with lines above, you can customize the properties by passing 
keyword arguments into the text functions:
"""
t = ax.set_xlabel('my data', fontsize=14, color='red')

# Using mathematical expressions in text

"""
Matplotlib accepts TeX equation expressions in any text expression
"""

ax.set_title(r'$\sigma_i=15$')

"""
where the r preceding the title string signifies that the string is a 
raw string and not to treat backslashes as python escapes. Matplotlib 
has a built-in TeX expression parser and layout engine, and ships its 
own math fonts. for details see Writing mathematical expressions. You 
can also use LaTeX directly to format your text and incorporate the output 
directly into your display figures or saved postscript. see Text rendering 
with LaTeX.
"""

# Annotations

"""
We can also annotate points on a plot, often by connecting an arrow pointing 
to xy, to a piece of text at xytext:
"""

fig, ax = plt.subplots(figsize=(5, 2.7))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.set_ylim(-2, 2);

"""
In this basic example, both xy and xytext are in data coordinates. There 
are a variety of other coordinate systems one can choose -- see Basic 
annotation and Advanced Annotations for details. More examples also 
can be found in Annotating Plots.
"""
# Legends
"""
Often we want to identify lines or markers with a Axes.legend:
"""
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(np.arange(len(data1)), data1, label='data1')
ax.plot(np.arange(len(data2)), data2, label='data2')
ax.plot(np.arange(len(data3)), data3, 'd', label='data3')
ax.legend();

#%% Axis scales and ticks


#%%
# Descomentar para mostrar las gráficas en la salida del cmd o powershell
#plt.show();

