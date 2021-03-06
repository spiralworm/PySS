# -*- coding: utf-8 -*-

"""
Module containing methods related to 3D scanning.

"""
import numpy as np
from PySS import analytic_geometry as ag
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# TODO: Useless class, either delete OR transfer relative functionality from ag.Points3D (possibly remove stl from ag)
class Scan3D(ag.Points3D):
    """
    3D model data.

    Class of 3D objects. Can be imported from an .stl file of a .txt file of list of node coordinates.

    """

    def __init__(self, swarm=None):
        super().__init__(swarm=swarm)
    #
    #     self.grouped_data = None
    #     self.centre = None
    #     self.size = None
    #
    # @classmethod
    # def from_stl_file(cls, fh, del_original=None):
    #     """
    #     Import stl file.
    #
    #     Alternative constructor, creates a Scan3D object by reading data from an .stl file. In case the file is created
    #     by Creaform's software (it is detected using name of the solid object as described in it's frist line), it is
    #     corrected accordingly before importing. The original file is renamed by adding '_old' before the extension or
    #     they can be deleted automatically if specified so.
    #
    #     Parameters
    #     ----------
    #     fh : str
    #         File path.
    #     del_original : bool, optional
    #         Keep or delete the original file. Default is keep.
    #     """
    #     with open(fh, 'r') as f:
    #         fl = f.readlines(1)[0]
    #         identifier = fl.split(None, 1)[1]
    #
    #     if identifier == 'ASCII STL file generated with VxScan by Creaform.\n':
    #         # Repair the file format
    #         Scan3D.repair_stl_file_structure(fh, del_original=del_original)
    #
    #     return cls(swarm=Scan3D.array2points(mesh.Mesh.from_file(fh)))
    #
    # @classmethod
    # def from_pickle(cls, fh):
    #     """
    #     Method for importing a pickle file containing x, y, z, coordinates.
    #
    #     Used to import data exported from blender. The pickle file is should contain a list of lists.
    #
    #     """
    #     with open(fh, 'rb') as fh:
    #         return cls(swarm=Scan3D.array2points(np.array(pickle.load(fh))))
    #
    # @classmethod
    # def from_coordinates_file(cls, fh):
    #     """
    #     Method reading text files containing x, y, z coordinates.
    #
    #     Used to import data from 3D scanning files.
    #     """
    #
    #     # Open the requested file.
    #     with open(fh, 'r') as f:
    #         # Number of points.
    #         n_of_points = len(f.readlines())
    #
    #         # Initialise a numpy array for the values.
    #         swarm = np.empty([n_of_points, 3])
    #
    #         # Reset the file read cursor and loop over the lines of the file populating the numpy array.
    #         f.seek(0)
    #         for i, l in enumerate(f):
    #             swarm[i] = l.split()
    #
    #     return cls(swarm=Scan3D.array2points(swarm))
    #
    # @staticmethod
    # def repair_stl_file_structure(fh, del_original=None):
    #     """
    #     Repair header-footer of files created by Creaform's package.
    #
    #     The .stl files created by Creaform's software are missing standard .stl header and footer. This method will
    #     create a copy of the requested file with proper header-footer using the filename (without the extension) as a
    #     name of the solid.
    #
    #     Parameters
    #     ----------
    #     fh : str
    #         File path.
    #     del_original : bool, optional
    #         Keep or delete the original file. Default is keep.
    #     """
    #     if del_original is None:
    #         del_original = False
    #     solid_name = os.path.splitext(os.path.basename(fh))[0]
    #
    #     start_line = "solid " + solid_name + "\n"
    #     end_line = "endsolid " + solid_name
    #     old_file = os.path.splitext(fh)[0] + 'old.stl'
    #
    #     os.rename(fh, old_file)
    #     with open(old_file) as fin:
    #         lines = fin.readlines()
    #     lines[0] = start_line
    #     lines.append(end_line)
    #
    #     with open(fh, 'w') as fout:
    #         for line in lines:
    #             fout.write(line)
    #
    #     if del_original:
    #         os.remove(old_file)
    #
    # @staticmethod
    # def array2points(array):
    #     """
    #     Convert an array of coordinates to a list of Point3D objects.
    #
    #     Parameters
    #     ----------
    #     array : {n*3} np.ndarray
    #
    #     Returns
    #     -------
    #     list of Point3D.
    #
    #     """
    #     if isinstance(array, np.ndarray):
    #         if np.shape(array)[1] == 3:
    #             point_list = []
    #             for i in array:
    #                 point_list.append(ag.Point3D.from_coordinates(i[0], i[1], i[2]))
    #             return point_list
    #         else:
    #             print('Wrong array dimensions. The array must have 3 columns.')
    #             return NotImplemented
    #     else:
    #         print('Wrong input. Input must be np.ndarray')
    #         return NotImplemented
    #
    # def sort_on_axis(self, axis=None):
    #     """
    #     Sort scanned data.
    #
    #     The scanned points are sorted for a given axis.
    #
    #     Parameters
    #     ----------
    #     axis : {0, 1, 2}, optional
    #         Axis for which the points are sorted. 0 for `x`, 1 for `y` and 2 for `z`.
    #         Default is 0
    #
    #     """
    #     if axis is None:
    #         axis = 0
    #
    #     self.swarm.sort(key=lambda x: x.coords[axis])
    #
    # def quantize(self, axis=None, tolerance=None):
    #     """
    #     Group the scanned data.
    #
    #     The points with difference on a given axis smaller than the tolerance are grouped together and stored in a list
    #     in the attribute `grouped_data`.
    #
    #     Parameters
    #     ----------
    #     axis : {0, 1, 2}, optional
    #         Axis for which the points are grouped. 0 for `x`, 1 for `y` and 2 for `z`.
    #         Default is 0.
    #     tolerance : float
    #         Distance tolerance for grouping the points.
    #
    #     """
    #     if axis is None:
    #         axis = 0
    #
    #     if tolerance is None:
    #         tolerance = 1e-4
    #
    #     self.sort_on_axis(axis=axis)
    #     self.grouped_data = [[self.swarm[0]]]
    #     for point in self.swarm:
    #         if abs(point.coords[axis] - self.grouped_data[-1][0].coords[axis]) < tolerance:
    #             self.grouped_data[-1].append(point)
    #         else:
    #             self.grouped_data.append([point])
    #
    # def centre_size(self):
    #     """
    #     Get the centre and the range of the data points.
    #
    #     Used in combination with the plotting methods to define the bounding box.
    #     """
    #     # Bounding box of the points.
    #     x_min = min([i.coords[0] for i in self.swarm])
    #     x_max = max([i.coords[0] for i in self.swarm])
    #     y_min = min([i.coords[1] for i in self.swarm])
    #     y_max = max([i.coords[1] for i in self.swarm])
    #     z_min = min([i.coords[2] for i in self.swarm])
    #     z_max = max([i.coords[2] for i in self.swarm])
    #     x_range = abs(x_max - x_min)
    #     y_range = abs(y_max - y_min)
    #     z_range = abs(z_max - z_min)
    #     x_mid = (x_max + x_min) / 2
    #     y_mid = (y_max + y_min) / 2
    #     z_mid = (z_min + z_max) / 2
    #
    #     self.centre = np.r_[x_mid, y_mid, z_mid]
    #     self.size = np.r_[x_range, y_range, z_range]
    #
    # def plot_points(self, fig=None, reduced=None):
    #     """
    #     Method plotting the model as a 3D surface.
    #
    #     Parameters
    #     ----------
    #     fig : Object of class matplotlib.figure.Figure, optional
    #         The figure window to be used for plotting. By default, a new window is created.
    #     reduced: float, optional
    #         A reduced randomly selected subset of points is plotted (in case the data is too dense for plotting). The
    #         reduced size is given as a ratio of the total number of points, e.g `reduced=0.5` plots half the points. By
    #         default, all points are plotted.
    #
    #     """
    #     # Get a figure to plot on
    #     if fig is None:
    #         fig = plt.figure()
    #         ax = Axes3D(fig)
    #     else:
    #         ax = fig.get_axes()[0]
    #
    #     # Make a randomly selected subset of points acc. to the input arg 'reduced=x'.
    #     if isinstance(reduced, float) and (0 < reduced < 1):
    #         n = list(np.random.choice(
    #             len(self.swarm),
    #             size=round(len(self.swarm) * reduced),
    #             replace=False
    #         ))
    #     else:
    #         n = range(0, len(self.swarm))
    #
    #     # Create the x, y, z lists
    #     x, y, z = [], [], []
    #     for i in n:
    #         x.append(self.swarm[i].coords[0])
    #         y.append(self.swarm[i].coords[1])
    #         z.append(self.swarm[i].coords[2])
    #
    #     # Plot the data
    #     ax.scatter(x, y, z, c='r', s=1)


class FlatFace(Scan3D):
    """
    Subclass of the Scan3D class, specifically for flat faces.

    Used for the individual faces of the polygonal specimens.

    """

    def __init__(self, swarm=None):
        self.face2ref_dist = None
        self.ref_plane = None
        self.local_csys = None

        super().__init__(swarm)

    def fit_plane(self):
        """
        Fit a plane on the scanned data.

        The Plane3D object is assigned in the `self.ref_plane`. The fitted plane is returned using the
        analytic_geometry.lstsq_planar_fit with the optional argument lay_on_xy=True. See
        analytic_geometry.lstsq_planar_fit documentation.
        """
        self.ref_plane = ag.Plane3D.from_fitting(self, lay_on_xy=True)

    def offset_face(self, offset, offset_points=False):
        """
        Offset the plane and (optionally) the scanned data points.

        Useful for translating translating the scanned surface to the mid line.

        :param offset:
        :param offset_points:
        :return:
        """
        self.ref_plane.offset_plane(offset)

        if offset_points:
            offsetted_points = self.translate_swarm(ag.Point3D(self.ref_plane.plane_coeff[:3] * offset))
            self.swarm = offsetted_points.swarm

    def calc_face2ref_dist(self):
        """Calculates distances from facet points to the reference plane."""
        if self.ref_plane:
            self.face2ref_dist = []
            for x in self.swarm:
                self.face2ref_dist.append(x.distance_to_plane(self.ref_plane))

    def calc_local_csys(self):
        """
        Calculate point grid on the local coordinate system of the reference plane.

        The scanned points are projected on the reference plane and the projections are rotated to lie on xy-plane.

        Returns
        -------
        x, y : lst of float
            Coordinate lists of the local grid.

        """
        # # Check if face2ref exists (The check is performed with an if in the beginning of the method to avoid unnecessary
        # #  calculations)
        # if self.face2ref_dist is None:
        #     print('There is no face2ref. Try `calc_face2ref_dist`.')
        #     return
        #
        # # Find scanned points projections on the ref plane.
        # proj_swarm = self.project_swarm(self.ref_plane)

        # Z-axis unit vector.
        v1 = np.r_[0, 0, 1]

        # The normalised norm vector of the plane (which will be aligned to z axis)
        v2 = ag.unit_vector(self.ref_plane.plane_coeff[0:3])

        # Find the angle between the zz axis and the plane's normal vector, v2
        rot_ang = ag.angle_between(v1, v2)

        # Find the rotation axis.
        rot_ax = ag.unit_vector(np.r_[-v2[1], v2[0], 0])

        # Lay the projections on xy
        # xy_swarm  = proj_swarm.rotate_swarm(rot_ang, rot_ax)
        transformed = self.rotate_swarm(rot_ang, rot_ax)
        transformed = transformed.translate_swarm(ag.Point3D.from_coordinates(0, 0, self.ref_plane.plane_coeff[3]))

        # Fit a line on the transformed data to get the direction of the laid down facet.
        # The direction vector is multiplied by the sign of the y-coordinate so that it is always on quadrants 1 and 2.
        dir_line = ag.Line3D.from_fitting(transformed.swarm)
        direction = np.sign(dir_line.parallel[1])*(dir_line.parallel[:2])

        # Calculate the angle of the laid down facet to the x axis.
        rot_ang2 = ag.angle_between(direction, [1, 0])

        # Rotate the swarm again, this time around the z axis, so that it is aligned with the x axis
        transformed = transformed.rotate_swarm(rot_ang2, [0, 0, 1])

        # Check the orientation of the transformed swarm: the base of the specimen is always at the origin. Where is the
        # head of the specimen? (is it around 700 or -700). If it faces negative, rotate by another 180 deg.
        transformed.centre_size()
        if transformed.centre[0] < 0:
            transformed = transformed.rotate_swarm(np.pi, [0, 0, 1])

        # Translate the swarm so that the centre is on the origin. Then, the base of the specimen should be on the
        # negative and the head on the positive
        transformed.centre_size()
        translate_vect = ag.Point3D.from_coordinates(-transformed.centre[0], -transformed.centre[1], 0)
        transformed = transformed.translate_swarm(translate_vect)

        return transformed

        # # Extract x amd y lists
        # x, y = [], []
        # for point in xy_swarm:
        #     x.append(point.coords[0])
        #     y.append(point.coords[1])
        #
        # return [x, y, z]

    def plot_on_lcsys(self):
        """
        Initial imperfection contour field.

        Plot a contour field of the initial imperfections on the local coordinate system of the flat face. For the
        initial imperfections see :obj:`calc_face2ref_dist`. The contour of the initial imperfections (distance of the
        face points to the reference plane) is plotted on the local coordinate system of the face, on which the
        reference plane of the face is the xy plane and the initial distances are the z-values.

        """
        lcsys_dist = self.calc_local_csys()
        x, y, z = [], [], []
        for i in lcsys_dist.swarm:
            x.append(i.coords[0])
            y.append(i.coords[1])
            z.append(i.coords[2])

        plt.tripcolor(x, y, z)
        plt.colorbar()

    def plot_face(self, fig=None, reduced=None):
        """
        Surface plotter.

        Plot the 3d points and the fitted plane.

        Parameters
        ----------
        fig : Object of class matplotlib.figure.Figure, optional
            The figure window to be used for plotting. By default, a new window is created.

        """

        # Average and range of the points.
        self.centre_size()
        plot_dim = max(self.size[0], self.size[1], self.size[2])

        # Get a figure to plot on
        if fig is None:
            fig = plt.figure()
            ax = Axes3D(fig)
        else:
            ax = fig.get_axes()[0]

        # Plot scanned points
        if self.swarm:
            print('Plotting scanned points')
            self.plot_swarm(fig=fig, reduced=reduced)
        else:
            print('No scanned points to plot.')

        # Check if the the object contains a plane and plot it.
        if self.ref_plane:
            print('Plotting plane.')
            # Create a grid for for xy
            # get height and width (z and x axes) limits from points
            x_lims = [self.centre[0] - self.size[0] / 2., self.centre[0] + self.size[0] / 2.]
            y_lims = [self.centre[1] - self.size[1] / 2., self.centre[1] + self.size[1] / 2.]
            z_lims = [self.centre[2] - self.size[2] / 2., self.centre[2] + self.size[2] / 2.]

            ll1 = self.ref_plane.xy_return(z_lims[0])
            ll2 = self.ref_plane.xy_return(z_lims[1])

            if self.size[0]>self.size[1]:
                y1 = ll1.y_for_x(x_lims[0])
                y2 = ll1.y_for_x(x_lims[1])
                y3 = ll2.y_for_x(x_lims[0])
                y4 = ll2.y_for_x(x_lims[1])

                x = np.array([x_lims, x_lims])
                y = np.array([[y1, y2], [y3, y4]])
            else:
                x1 = ll1.x_for_y(y_lims[0])
                x2 = ll1.x_for_y(y_lims[1])
                x3 = ll2.x_for_y(y_lims[0])
                x4 = ll2.x_for_y(y_lims[1])

                x = np.array([[x1, x2], [x3, x4]])
                y = np.array([y_lims, y_lims])

            # x, y = np.meshgrid(x_lims, y_lims)
            # print(x, type(x))
            # print(y, type(y))
            # evaluate the plane function on the grid.
            z = self.ref_plane.z_return(x, y)
            # or expressed using matrix/vector product
            # z = np.dot(np.c_[xx, yy, np.ones(xx.shape)], self.plane_coeff).reshape(x.shape)

            # Plot the plane
            ax.plot_surface(x, y, z, rstride=1, cstride=1, alpha=0.2)

        else:
            print('No reference plane to plot. Use `fit_plane` to create one.')

        # Regulate figure.
        plt.xlabel('x')
        plt.ylabel('y')
        ax.set_zlabel('z')
        ax.set_xlim3d(self.centre[0] - plot_dim / 2, self.centre[0] + plot_dim / 2)
        ax.set_ylim3d(self.centre[1] - plot_dim / 2, self.centre[1] + plot_dim / 2)
        ax.set_zlim3d(self.centre[2] - plot_dim / 2, self.centre[2] + plot_dim / 2)
        plt.show()

        # Return the figure handle.
        return fig


class RoundedEdge(Scan3D):
    """
    A scanned rounded edge.

    """

    def __init__(self, swarm=None):
        self.theoretical_edge = None
        self.edge_points = None
        self.circles = None
        self.edge2ref_dist = None
        self.ref_line = None

        super().__init__(swarm)

    def add_theoretical_edge(self, line):
        """
        Add a reference line for the edge.

        Useful when the rounded edge lies between flat faces and the theoretical edge is at their intersection.

        Parameters
        ----------
        line : Line3D
            Theoretical edge line to be added. This line should be calculated as the intersection of the facets sharing
            this edge.
        """
        if isinstance(line, ag.Line3D):
            self.theoretical_edge = line
        else:
            print("ref_line must be Line3D")
            return NotImplemented

    def fit_circles(self, axis=None, offset=None):
        """
        Fit a series of circles along the length of the rounded edge.

        The scanned data are first grouped together based on their z-coordinate and then a horizontal circle is fitted
        for each group of points.

        Note
        ----
        The resulted circle from fitting at each height, z, are checked so that the centres are closer to the origin
        than the points that generated it, essentially checking if the curvature of the points is concave towards the
        origin. If not, the circle is ignored and a `None` placeholder is appended to the list of circles.

        """
        if axis is None:
            axis = 0

        if offset is None:
            offset = 0

        self.quantize(axis=axis)
        self.circles = []
        for group in self.grouped_data:
            circle = ag.Circle2D.from_fitting(group)
            if all([np.linalg.norm(i.coords[:2]) > np.linalg.norm(circle.centre) for i in group]):
                self.circles.append(circle)
                self.circles[-1].radius = self.circles[-1].radius + offset
            else:
                print('Suspicious circle from fitting ignored at height:    {}'.format(group[0].coords[2]))

    def calc_edge_points(self, other):
        """
        Intersect scanned points with a surface between the theoretical edge line and a given line.

        This function is used to find points on the scanned rounded corner. Circles are fitted on the
        scanned points on different positions. Then the circles are intersected with the theoretical edge and another
        line specified by the user (e.g. the centre of the column). A list of points is generated which represent the
        real edge of rounded corner.

        Parameters
        ----------
        other: Line3D object
            Secondary 3D line used together with the theoretical edge 3D line. The edge circles are intersected with
            line segments defined by points of those two 3D lines.

        """
        if isinstance(other, ag.Line3D):
            self.edge_points = []
            # Loop through the circles that represent the edge roundness at different heights.
            for circle in self.circles:
                # Get the z-coordinate (height) of the current point
                z_current = circle.points[0].coords[2]
                #print('Finding edge point at height {}'.format(z_current))

                # Get the x-y coordinates of the edge reference line and the mid-line for the given height, z.
                theoretical_line_point = self.theoretical_edge.xy_for_z(z_current)[:2]
                other_line_point = other.xy_for_z(z_current)

                # Create a temporary line object from the two points.
                intersection_line = ag.Line2D.from_2_points(theoretical_line_point, other_line_point[:2])

                # Intersect this temporary line with the current circle.
                line_circle_intersection = circle.intersect_with_line(intersection_line)

                # If the line does not intersect with the current circle, print on screen and continue.
                if line_circle_intersection is None:
                    print("Line and circle at height {} do not intersect. Point ignored.".format(z_current))

                else:
                    # If the line intersects with the circle, select the intersection point which is closest to the
                    # theoretical line.
                    dist = [np.linalg.norm(theoretical_line_point - x) for x in line_circle_intersection]
                    ref_point = line_circle_intersection[dist.index(min(dist))]

                    # Append the point to the list of edge_points
                    self.edge_points.append(ag.Point3D(np.append(ref_point, z_current)))
        else:
            print('The input object is not of the class `Line3D`')
            return NotImplemented

    def calc_ref_line(self):
        """
        Calculate the reference line.

        The reference line for the edge is defined as the best fit straight line to the edge points. For more
        information on the edge points, see the `intersect_data` method.
        """
        self.ref_line = ag.Line3D.from_fitting(self.edge_points)

    def calc_edge2ref_dist(self):
        """Calculate distances of edge points to the reference line."""
        if self.ref_line and self.ref_line is not NotImplemented:

            # Get the relative position of the first point on the reference edge line. This will be used as origin for
            # for the projected edge points on the reference line.
            origin = np.dot(self.ref_line.parallel, self.edge_points[0].coords)

            position = []
            distance = []

            for x in self.edge_points:
                # Find the distances from the the real edge and the ref line points to the (0, 0). Based on which one is
                # further away from the origin, the sign of the distance is assigned
                edge = np.linalg.norm(np.r_[0, 0] - x.coords[:2])
                refp = np.linalg.norm(np.r_[0, 0] - self.ref_line.xy_for_z(x.coords[2])[:2])
                s = np.sign(edge - refp)

                # calculate the distance of the edge point to the ref line and give this distance the sign calculated.
                distance.append(s * x.distance_to_line(self.ref_line))

                # calculate the position of the projected real edge point on the reference line, using as origin the
                # projection of the first point (see above).
                position.append(abs(origin - np.dot(self.ref_line.parallel, x.coords)))

            # assign positions and distances on the parent object
            self.edge2ref_dist = [position, distance]


        else:
            print('No reference line. First, add a reference line to the object. Check if the fitting process on the '
                  'edge points converged. Edge ignored.')
            return NotImplemented

    def plot_imp(self):
        if self.edge2ref_dist:
            plt.plot(self.edge2ref_dist[0], self.edge2ref_dist[1])
        else:
            print('No information for distances between edge points and reference line. Try the calc_edge2ref_dist '
                  'method.')

def main():
    print('Module successfully loaded.')


if __name__ == "__main__":
    main()
