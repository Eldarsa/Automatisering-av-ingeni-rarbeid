import math
import random
import numpy as np
from sympy import Line3D, Point3D, Plane


import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

def randomize_int_from_reference(reference, span):
    random.seed()
    if reference == 0:
        return random.randint(-int(span), int(span))
    else:
        return random.randint(int(reference - span*abs(reference)), int(reference + span*reference))


def randomize_float_from_reference(reference, span):
    random.seed()
    if reference == 0.:
        return random.uniform(-span, span)
    else:
        return random.uniform(float(reference-span*abs(reference)), float(reference+span*reference))

################# VECTOR SUPPORT FUNCTIONS ######################

def get_random_vector():
    return np.array([random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)])

def convert_to_unit(vector):
    v = np.array(vector)
    return v / np.linalg.norm(v)

def project_onto_plane(vector, normal):
    d = (vector * normal) / np.linalg.norm(normal) #All in numpy array
    p = [d * convert_to_unit(normal)[i] for i in range(len(vector))]
    projMatrix = np.array([vector[i] - p[i] for i in range(len(vector))])
    return np.array([projMatrix[0][0], projMatrix[1][1], 0])

def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

def calculate_accuracy(hood_origin, hood_direction, target):

    target_vector = np.array(hood_origin - target)

    if np.dot(hood_direction, target_vector) <= 0:

        pt1 = Point3D(hood_origin) #Where the lamp hood connects to the leg
        pt2 = Point3D(hood_origin + hood_direction) #A point slightly of the leg in the right direction
        target = Point3D(target)

        line = Line3D(pt1, pt2) #Create a line that at some point crosses the plane
        plane = Plane(Point3D(target), normal_vector=target_vector) #Creates the plane perpendicular on the vector between the target and lamp head
        intersection = plane.intersection(line) #Where the plane intersects the line  
        result = intersection[0].distance(target) #Finds the distance we need

        return float(result)

    else:
        return float('inf') #To check if we never intersect the plane


# def dot_product(x, y):
#     return sum([x[i] * y[i] for i in range(len(x))])

# def norm(x):
#     return math.sqrt(dot_product(x, x))

# def normalize(x):
#     return [x[i] / norm(x) for i in range(len(x))]

# def project_onto_plane(x, n):
#     d = dot_product(x, n) / norm(n)
#     p = [d * normalize(n)[i] for i in range(len(n))]
#     return [x[i] - p[i] for i in range(len(x))]

