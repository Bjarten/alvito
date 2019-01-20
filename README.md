# Alvito - An Algorithm Visualization Tool for Python

Alvito is a tool for creating sorting and search algorithm visualizations and saving them as GIFs. You can find the ```algopy``` class in the ```algorithm_visualizer.py```.

## Usage

You can run this project and create your own GIFs directly in the browser by clicking this button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Bjarten/algorithm-visualizer-python/master)
, or you can clone the project to your computer and install the required pip packages specified in the requirements text file.

```
pip install -r requirements.txt
```

## Code Example

```
from algorithm_visualizer import algopy

ap = algopy()
ap.fps = 1
ap.xlable_fontsize = 12
ap.title_fontsize = 12

array = [1,18,16,2,9,6,12,4,19,17,14,3,10,20,5,13,8,11,15,7]

ap.bubbleSort(array)
```
The code above will generate the following GIF
![](gifs/bubble_sort_list.gif)

## Notebooks
Here are links to view the notebooks on [nbviewer](https://nbviewer.jupyter.org/) if GitHub should struggle with them.

[Examples.ipynb](https://nbviewer.jupyter.org/github/Bjarten/algorithm-visualizer-python/blob/master/Examples.ipynb)<br>
[Algorithms.ipynb](https://nbviewer.jupyter.org/github/Bjarten/algorithm-visualizer-python/blob/master/Algorithms.ipynb)<br>
[Colors_and_Colormaps.ipynb](https://nbviewer.jupyter.org/github/Bjarten/algorithm-visualizer-python/blob/master/Colors_and_Colormaps.ipynb)

## Algorithms

Algorithm support so far (more coming soon!):

* Bubble Sort
* Selection Sort
* Insertion Sort

The code for the algorithms used in the tool comes from [Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/runestone/static/pythonds/index.html). This is a great source to learn about algorithms and data structures, check it out!

## Example GIFs

![](gifs/bubble_sort_6_6.gif)
![](gifs/insertion_sort_6_6.gif)<br>
![](gifs/bubble_sort_YlGn.gif)
![](gifs/insertion_sort_wistia.gif)<br>
![](gifs/insertion_sort_grey.gif)
![](gifs/insertion_sort_reds.gif)<br>
![](gifs/insertion_sort_blues.gif)
![](gifs/bubble_sort_cool.gif)<br>

![](gifs/insertion_sort_20_1.gif)
