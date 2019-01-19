import imageio
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import seaborn as sns
sns.set()
import numpy as np
from tqdm import trange
import os

class algopy:

    def __init__(self):
        self._ims = []
        self.fps = 10
        self.input_shape = (0,0)
        self.title = ""
        self.comparisons = 0
        self.track_operations = True

        self.show_title = True
        self.title_fontsize = 15

        self.show_xlable = True
        self.xlable_fontsize = 15

        self.rectangle_color_1 = 'black'
        self.rectangle_color_2 = 'gold'
        self.rectangle_linewidth = 5

        self.colormap = 'cool'
        self.numbers_color = "dynamic"
        self.numbers_fontsize = 15
        self.dpi = 100

        self.save_dir = 'gifs/'


    def visulize_algorithm(self,array,i_1,i_2,i_3,ec1,ec2,ec3):

        # reahsape array into its original shape
        array = np.array(array).reshape(self.input_shape[0], self.input_shape[1])

        # find coordinates for the rectangles
        dx = 0.05
        dy = dx
        index=[(i_1%self.input_shape[1]+dx,i_1//self.input_shape[1]+dy),
               (i_2%self.input_shape[1]+dx,i_2//self.input_shape[1]+dy),
               (i_3%self.input_shape[1]+dx,i_3//self.input_shape[1]+dy)]

        if self.numbers_color == 'dynamic':
            annot_kws = { 'fontsize' : self.numbers_fontsize  }
        else:
            annot_kws = { 'fontsize' : self.numbers_fontsize , 'color' : self.numbers_color }

        # set plot figsize
        scale = 0.8
        figsize = (self.input_shape[1]*scale, self.input_shape[0]*scale)
        fig, ax = plt.subplots(figsize=figsize)

        # create heatmap
        ax = sns.heatmap(array,
                         annot=True,
                         annot_kws = annot_kws,
                         fmt="d",
                         linewidths=2,
                         cbar=False,
                         cmap=self.colormap,
                         yticklabels=False,
                         xticklabels=False,
                         square=True)

        # plot title
        if self.show_title:
            ax.set_title(self.title, fontsize=self.title_fontsize )

        # plot number of comparisons
        if self.show_xlable:
            plt.xlabel(f'Comparisons:\n{self.comparisons}',fontsize=self.xlable_fontsize)

        if self.track_operations:
            # draw rectangle around tracked cells
            if i_1 != -1:
                ax.add_patch(Rectangle(index[0], 0.9, 0.9, fill=False, edgecolor=ec1, lw=self.rectangle_linewidth))
            if i_2 != -1:
                ax.add_patch(Rectangle(index[1], 0.9, 0.9, fill=False, edgecolor=ec2, lw=self.rectangle_linewidth))
            if i_3 != -1:
                ax.add_patch(Rectangle(index[2], 0.9, 0.9, fill=False, edgecolor=ec3, lw=self.rectangle_linewidth))

        # create and save gif

        if not os.path.exists('temp/'):
                os.mkdir('temp/')

        img_loc = 'temp/' + 'temp_image_{:d}'.format(self.comparisons+1) + '.png'

        plt.savefig(img_loc, bbox_inches='tight', dpi=self.dpi)
        self._ims.append(imageio.imread(img_loc))
        os.remove(img_loc)

        plt.close()

    def bubbleSort(self, array, title="Bubble Sort"):

        self.title = title
        array = self._array_transform(array)

        self.comparisons = 0

        for passnum in trange(len(array)-1,0,-1):
            for i in range(passnum):
                self.comparisons += 1
                if array[i]>array[i+1]:
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp

                    self.visulize_algorithm(array,i,i+1,-1,ec1=self.rectangle_color_2,ec2=self.rectangle_color_2,ec3=self.rectangle_color_2)
                else:
                    self.visulize_algorithm(array,i,i+1,-1,ec1=self.rectangle_color_1,ec2=self.rectangle_color_1,ec3=self.rectangle_color_1)

        imageio.mimsave(f'{self.save_dir}/bubble_sort_comparisons_{self.comparisons}.gif', self._ims, fps=self.fps)
        self._ims = []

    def insertionSort(self, array, title="Insertion Sort"):

        self.title = title
        array = self._array_transform(array)

        self.comparisons = 0

        for index in trange(1,len(array)):

            currentvalue = array[index]
            position = index

            while position>0 and array[position-1]>currentvalue:

                self.comparisons += 1

                array[position]=array[position-1]
                position = position-1
                array[position]=currentvalue

                self.visulize_algorithm(array,index,position,-1,ec1=self.rectangle_color_1,ec2=self.rectangle_color_1,ec3=self.rectangle_color_1)

        imageio.mimsave(f'{self.save_dir}insertion_sort_comparisons_{self.comparisons}.gif', self._ims, fps=self.fps)
        self._ims = []

    def selectionSort(self, array, title="Selection Sort"):

        self.title = title
        array = self._array_transform(array)

        self.comparisons = 0

        for fillslot in trange(len(array)-1,0,-1):
            positionOfMax=0
            for location in range(1,fillslot+1):
                self.comparisons += 1

                self.visulize_algorithm(array,fillslot,positionOfMax,location,ec1=self.rectangle_color_2,ec2=self.rectangle_color_2,ec3=self.rectangle_color_1)

                if array[location]>array[positionOfMax]:
                    positionOfMax = location

            temp = array[fillslot]
            array[fillslot] = array[positionOfMax]
            array[positionOfMax] = temp

        imageio.mimsave(f'{self.save_dir}selection_sort_comparisons_{self.comparisons}.gif', self._ims, fps=self.fps)
        self._ims = []

    def _array_transform(self, array):

        if type(array) == list:
            array = np.array(array)
        if array.ndim == 1:
            array = np.array([array])

        self.input_shape = array.shape

        # flatten the array so it can be used by the algorithm
        array = array.flatten()

        return array
