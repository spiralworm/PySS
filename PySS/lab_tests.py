# -*- coding: utf-8 -*-

"""
Module with functions related to laboratory work and data acquired with CATMAN.

"""

import numpy as np
import csv
import codecs
from os.path import basename, splitext
from matplotlib import pyplot as plt


class Experiment:
    """
    Laboratory test data.

    Class laboratory experiment containing methods for loading and manipulating data recorded with CATMAN software. The
    class is designed to be used with the `from_...` alternative constructors and not by giving the data directly for
    the object to be constructed.

    """
    def __init__(self, name=None, data=None):
        self.data = data
        self.name = name

    def plot2d(self, x_data, y_data, ax=None):
        """
        Plot two recorded channels against each other.

        Parameters
        ----------
        x_data : str
            Key from self.data dictionary for the x-axis.
        y_data : str
            Key from self.data dictionary for the y-axis.
        ax : axis object, optional
            The axis to be used for plotting. By default, new figure and axis are created.

        """

        if ax is None:
            fig = plt.figure()
            plt.plot()
            ax = fig.axes[0]
        elif not isinstance(ax, type(plt.axes())):
            print('Unexpected input type. Input argument `ax` must be of type `matplotlib.pyplot.axes()`')
            return NotImplemented

        ax.plot(self.data[x_data], self.data[y_data], label=self.name)

        return ax

    def add_new_channel_zeros(self, name):
        """"Initialise a new channel entry in the dictionary with zeros."""
        self.data[name] = np.zeros([len(self.data[next(iter(self.data))]), 1])

    @classmethod
    def from_file(cls, fh):
        """
        Alternative constructor.

        Used to make a coupon object and load the data at once.

        Parameters
        ----------
        fh : str
            Path of ascii data file.

        """

        # Name from filename.
        filename = splitext(basename(fh))[0]

        # Open the requested file.
        f = codecs.open(fh, 'r', 'ISO-8859-1')

        # Read the header
        header = list(csv.reader([next(f) for x in range(7)], delimiter='\t'))

        # Read the column headers.
        next(f)
        column_head = list(csv.reader([next(f) for x in range(29)], delimiter='\t'))

        # Read the tab separated values.
        next(f)
        values = list(csv.reader(f, delimiter='\t'))

        # Get the number of channels
        n_chan = len(values[0])

        # Create a dictionary.
        data = {}

        # Build a dictionary with the data using the column header to fetch the dict keys.
        for i in range(n_chan):
            channel = np.zeros((len(values), 1))
            name = column_head[0][i].partition(' ')[0]
            for j, row in enumerate(values):
                channel[j] = (float(row[i].replace(',', '.')))
            data[name] = channel

        return cls(name=filename, data=data)


class CouponTest(Experiment):
    """
    Class for coupon tests.

    Inherits the basic properties of a generic experiment class and offers standard calculations for rectangular
    cross-section tensile coupon tests.

    """

    def __init__(self, name=None, data=None, thickness=None, width=None, l_0=None):
        super().__init__(name=name, data=data)
        self.thickness = thickness
        self.width = width
        self.l_0 = l_0
        # If geometric data existe, calculate the initial area.
        if (
            isinstance(thickness, float) or isinstance(thickness, int)
        ) and (
            isinstance(width, float) or isinstance(width, int)
        ):
            self.A_0 = thickness * width
        else:
            self.A_0 = None

    def add_initial_data(self, thickness, width, l_0):
        """
        Add initial geometrical data of the coupon specimen.

        Assuming that the imported test data provide stroke-load readings from testing, the geometric data of the coupon
        (thickness, width, initial gauge length) are needed to calculate the stress-strain curves. The method will
        overwrite pre existing.

        Parameters
        ----------
        thickness : float
            Coupon's measured thickness.
        width : float
            Coupon's measured width.
        l_0 : float
            Initial gauge length, %l_{0}%

        """
        self.thickness = thickness
        self.width = width
        self.l_0 = l_0
        self.A_0 = thickness * width

    def calc_stress_strain(self):
        """
        Calculate stress-strain curve.

        Calculate the engineering ant the true stress-strain curves for the coupon test. Initial geometric data as well
        as test data (stroke, load) must be assigned to the object for the method to run. The method assumes that
        entries with keys 'Stroke' and 'Load' exit in the data dictionary.

        """

        self.data['StressEng'] = 1000 * self.data['Load'] / self.A_0
        self.data['StrainEng'] = self.data['Epsilon'] / self.l_0

    def plot_stressstrain_eng(self, ax=None):
        ax = self.plot2d('StrainEng', 'StressEng', ax=ax)
        plt.xlabel('Strain, $\epsilon_{eng}$ [%]')
        plt.ylabel('Stress, $\sigma_{eng}$ [MPa]')
        plt.title(self.name)
        return ax


def main():
    cp = []
    for i in range(1, 7):
        cp.append(CouponTest.from_file('./data/coupons/cp{}.asc'.format(i)))

    widths = [20.408, 20.386, 20.397, 20.366, 20.35, 20.39]
    thicknesses = [1.884, 1.891, 1.9, 1.88, 1.882, 1.878]
    l_0s = [80., 80., 80., 80., 80., 80.]

    for i , x in enumerate(cp):
        x.add_initial_data(thicknesses[i], widths[i], l_0s[i])
        x.calc_stress_strain()
        x.plot_stressstrain_eng()

    return cp

