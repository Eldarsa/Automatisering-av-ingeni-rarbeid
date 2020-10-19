import math
import random

def calculate_joints(number_of_legs):
    return number_of_legs+1

def randomize_from_reference(reference, span):
    random.seed()
    return random.randint(int(reference/span), int(reference*span))

def generate_legs(number_of_legs, leg_diameter, leg_height, 
base_vector, base_leg_vector, base_leg_origin, leg_angle):

    legs = dict() #Create a dictionary
    legs["leg0"] = {
        "diameter": leg_diameter,
        "height": leg_height,
        "origin": base_leg_origin,
        "vector": base_leg_vector
    }

    vectorList = [base_leg_vector]
    for i in range(1,number_of_legs):
        vectorList.append(calculate_leg_vector(base_vector, vectorList[i-1], leg_angle))

    originList = [base_leg_origin]
    for i in range(1,number_of_legs):
        originList.append()

    for i in range(1, number_of_legs):
        legs["leg"+i] = dict(diameter=leg_diameter, 
                            height=leg_height, 
                            origin=originList[i], 
                            vector=vectorList[i])

def calculate_head_origin(leg_params):
    head_origin = 0
    return head_origin

def calculate_leg_vector(frame_reference_vector, previous_leg_vector, vertical_angle):

    flipped_previous_leg_vector = (-previous_leg_vector) * (-frame_reference_vector) 
    #This is really a pretty cheap solution


    return flipped_previous_leg_vector 

def calculate_vector_using_angles(vertical_angle, horisontal_angle):

    #You can try to just flip these using a [-1,-1,1] vector!
    vector = [
        math.cos(math.radians(horisontal_angle)),
        math.sin(math.radians(horisontal_angle)),
        math.sin(math.radians(vertical_angle))
    ]
    return vector


#Support functions to calculate vector directions
def dot_product(x, y):
    return sum([x[i] * y[i] for i in range(len(x))])

def norm(x):
    return sqrt(dot_product(x, x))

def normalize(x):
    return [x[i] / norm(x) for i in range(len(x))]

def project_onto_plane(x, n):
    d = dot_product(x, n) / norm(n)
    p = [d * normalize(n)[i] for i in range(len(n))]
    return [x[i] - p[i] for i in range(len(x))]

