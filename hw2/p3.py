# Tom Hogans, Big Data CS491
# Problem Set #2, Question 3

import itertools
import numpy as np

# MMDS 9.2.1

vectors = {
    'A': np.array([3.06, 500, 6]),
    'B': np.array([2.68, 320, 4]),
    'C': np.array([2.92, 640, 6])}


def scale_vector(vector, alpha, beta):
    """ Scales a vector with 3 components.
    The 2nd component is scaled by alpha.
    The 3rd component is scaled by beta. """
    vector[1] = vector[1] * alpha
    vector[2] = vector[2] * beta
    return vector

def cosine_distance(x, y):
    """ Returns the cosine distance of vectors x and y """
    dot_product = x.dot(y)
    l2_norms = np.linalg.norm(x) * np.linalg.norm(y)
    return float(dot_product) / float(l2_norms)


# Scale with alpha=1, beta=1
print("Scaling vectors with alpha=1, beta=1")
vectors = {k: scale_vector(v, 1, 1) for k, v in vectors.items()}
print(vectors)
for x, y in itertools.combinations(vectors, 2):
    print("Pair %s, %s cosine distance is %s" %
         (x, y, cosine_distance(vectors[x], vectors[y])))

print("\n\n")

# Scale with alpha=.01, beta=.5
print("Scaling vectors with alpha=.01, beta=.5")
vectors = {k: scale_vector(v, .01, .5) for k, v in vectors.items()}
print(vectors)
for x, y in itertools.combinations(vectors, 2):
    print("Pair %s, %s cosine distance is %s" %
         (x, y, cosine_distance(vectors[x], vectors[y])))
