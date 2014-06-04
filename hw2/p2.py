# Tom Hogans, Big Data CS491
# Problem Set #2, Question 2

import itertools
import numpy as np

# MMDS 3.7.1
# For each of the pairs of these vectors, which f_i functions
# makes the pair a candidate?
# Answer: we iterate through each pair and find the index of the
# matching bits and return those for each pair.

vectors = ['000000', '110011', '010101', '011100']
# For each pair of vectors x, y from above
for x, y in itertools.combinations(vectors, 2):
    assert len(x) == len(y)
    d = len(x)
    candidates = [i + 1 for i in range(d) if x[i] == y[i]]
    candidates = map(str, candidates)
    print("3.7.1: For pair (%s, %s): %s" % (x, y, ", ".join(candidates)))
print("\n")


# MMDS 3.7.2
vectors = [
    np.array([1, 1, 1, -1]),
    np.array([1, 1, -1, 1]),
    np.array([1, -1, 1, 1]),
    np.array([-1, 1, 1, 1]), ]

def get_sketch(input_array, vectors):
    results = []
    for v in vectors:
        v_result = v.dot(input_array)
        if v_result >= 0:
            results.append(1)
        else:
            results.append(-1)
    return results

# Compute the sketches of the following vectors.
print("3.7.2 (a): %s" % get_sketch(np.array([2, 3, 4, 5]), vectors))
print("3.7.2 (b): %s" % get_sketch(np.array([-2, 3, -4, 5]), vectors))
print("3.7.2 (c): %s" % get_sketch(np.array([2, -3, 4, -5]), vectors))
