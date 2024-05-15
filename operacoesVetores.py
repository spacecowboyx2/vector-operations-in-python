from math import acos, pi
#adding vectors

def add_vectors(vector1, vector2):
    new_vector = []
    if len(vector1) == len(vector2):
        for c in range(len(vector1)):
            new_vector.append(vector1[c] + vector2[c])
        return new_vector
    else:
        print("the number of vectors components is not equal")
    return []

print(add_vectors([1,2,4],[3,2,5])) #output: [4,4,9]

#subtracting vectors

def sub_vectors(vector1, vector2):
    new_vector = []
    if len(vector1) == len(vector2):
        for c in range(len(vector1)):
            new_vector.append(vector1[c] - vector2[c])
        return new_vector
    else:
        print("the number of vectors components is not equal")
    return []

print(sub_vectors([1,2,4],[3,2,5])) #output: [-2,0,-1]

#calculate scalar multiplication
def scalar_multiplication(e, vector):
    new_vector = []
    for c in range(len(vector)):
        new_vector.append(vector[c]*e)

    return new_vector

print(scalar_multiplication(2,[1,3,2])) #output: [2,6,4]

#dot_product
def dot_product(vector1, vector2):
    soma = 0
    if len(vector1) == len(vector2):
        for c in range(len(vector1)):
            soma += vector1[c] * vector2[c]
        return soma
    else:
        print("the number of vectors components is not equal")
    return []

print(dot_product([-2,4,1], [6,0,-1])) #output: -13

#modulus or magnitude

def modulus_vector(vector):
    soma = 0
    for c in range(len(vector)):
        vector[c] = vector[c]**2
        soma += vector[c]
    modulus = soma**(1/2)

    return modulus

print(modulus_vector([3,4])) #output: 5.0
print(modulus_vector([2,4,5]))#output: 6.70820393... -> sqrt(45)

#distance between vectors

def distance_vectors(vector1, vector2):
    return modulus_vector(sub_vectors(vector1, vector2))
    

print(distance_vectors([1,-2,3], [2,4,5])) #output: 6.40312423... -> sqrt(41)

#angle between two vectors

def radians_to_degress(radian): # radian to degress
    return radian * 180/pi


print(dot_product([1,0],[0,3]))
def angle_between(vector1, vector2): 
    cos = dot_product(vector1, vector2) / (modulus_vector(vector1) * modulus_vector(vector2))
    angle = acos(cos) #radians
    angle = radians_to_degress(angle) #degress
    return angle

print(angle_between([1,0],[0,3])) #output: 90.0



