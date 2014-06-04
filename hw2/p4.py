# Tom Hogans, HW2 Problem 4

import os
import itertools

import random
import numpy as np
import pandas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


data_dir = "./med_doc_set"
files = ['%s/%s' % (data_dir, f) for f in os.listdir(data_dir) if f.endswith('.txt')]
files = files

# Options tried:
# With no stop words defined, there were 85303 trigrams.
# This custom list of common words returns 61251 trigrams.
stop_words = [
    'a', 'an', 'the', 'and', 'or', 'it', 'of', 'in', 'as', 'to',
    'for', 'that', 'he', 'she', 'on', 'is', 'at', 'by', 'can', 'did', 'be', 'was',
    'br']
# By using the default 'english' stopwords list, it was reduced to 43887.
# By setting min_df=2, we ignore terms that only occur once, reducing the
# terms count to 505.  By setting min_df=3, we reduce the count to 9.  For
# the following code, we're only using only the regular 'english' stopword
# list and setting min_df=2 in order to have a reasonable amount of terms.
vectorizer = CountVectorizer(input='filename', ngram_range=(3, 3),
                             encoding='latin-1', stop_words='english',
                             max_features=None, binary=True, min_df=2)
raw_count_matrix = vectorizer.fit_transform(files)
print("Found %d trigrams in %d files" % (raw_count_matrix.shape[1], raw_count_matrix.shape[0]))

count_matrix = pandas.DataFrame(raw_count_matrix.toarray())
count_matrix = count_matrix.transpose()

transformer = TfidfTransformer()
transformer_matrix = transformer.fit_transform(raw_count_matrix)
tfidf_matrix = pandas.DataFrame(transformer_matrix.toarray())
tfidf_matrix.transpose()


# Define parameters: number of bands, rows, hash functions, and threshold
r = 6  # rows
b = 4  # bands
t = (1.0 / b) ** (1.0 / r)  # threshold
n = b * r  # number of hash functions


def minhash_signature(count_matrix, hash_count, p=32452867):
    """ Takes a count matrix and returns a minhash signature matrix

    Generates hash_count hash functions from the (ax + b) % p % n family of
    hash functions.
    """
    # Generate hash functions with random values for 1 <= a <= p and 0 <= b <= p
    hash_functions = [
        lambda x: ((random.randint(1, p) * x + random.randint(0, p)) % p) % hash_count
        for _ in range(hash_count)]

    # Set up minhash signature matrix with all values defaulting to infinity
    sig_rows = len(hash_functions)
    sig_cols = len(count_matrix.columns)
    sig_matrix = pandas.DataFrame(index=range(sig_rows), columns=range(sig_cols))
    sig_matrix = sig_matrix.fillna(value=float('inf'))

    # Calculate and fill values for signature matrix
    for row in range(len(count_matrix)):
        # Calculate hash results for this row number
        hash_results = [h(row) for h in hash_functions]
        # Find Sets with non-zero values
        for col in count_matrix.columns:
            if count_matrix[col][row] > 0:
                for i in range(len(hash_results)):
                    # Only set SIG(i, c) if hash_results[i] < SIG(i, c)
                    sig_matrix[col][i] = min(sig_matrix[col][i], hash_results[i])
    return sig_matrix


def cosine_signature(matrix, hash_count):
    """ Accepts a TF.IDF matrix and returns a cosine distance signature matrix

    """
    def random_unit_vector(d):
        """ Generates vector of dimension d with random components within the
        interval [-1, 1] and returns the normalized (unit) vector. """
        v = [random.random() * 2 - 1 for _ in range(d)]
        return v / np.linalg.norm(v)

    random_unit_vectors = [random_unit_vector(len(matrix))
                           for _ in range(hash_count)]

    # Set up minhash signature matrix with all values defaulting to infinity
    sig_rows = len(random_unit_vectors)
    sig_cols = len(matrix.columns)
    sig_matrix = pandas.DataFrame(index=range(sig_rows), columns=range(sig_cols))
    sig_matrix = sig_matrix.fillna(value=float('inf'))

    for row, unit_vector in enumerate(random_unit_vectors):
        for col in matrix.columns:
            feature_vector = matrix[col]
            result = feature_vector.dot(unit_vector)
            # Set signature matrix values to 1 or -1 depending on result sign
            sig_matrix[col][row] = 1 if result >= 0 else 0

    return sig_matrix


def candidate_pairs(sig_matrix, band_size):
    """ Finds set pairs whose signature (row) values match exactly within one
    or more bands """
    candidates = set()
    for i in range(0, n, b):
        band = sig_matrix[i:i + band_size]
        # Check each pair for matching row values
        for x, y in itertools.combinations(band.columns, 2):
            if sum(band[x] == band[y]) == len(band[x]):
                candidates.add((x, y))
    return candidates


def compare_candidate_signatures(candidates, sig_matrix, threshold):
    """ Examine each pair of candidates and determine whether the fraction of
    their components in which they agree in the signature matrix is at least
    equal to threshold.  Returns the pairs where similarty >= threshold. """
    pairs = set()
    for x, y in candidates:
        matches = sum(sig_matrix[x] == sig_matrix[y])
        total = len(sig_matrix[x])
        similarity = float(matches) / float(total)
        if similarity >= threshold:
            pairs.add((x, y))
    return pairs


print("Calculating signature tables for minhash and cosine distance")
# Construct signature tables for each technique
minhash_sig_matrix = minhash_signature(count_matrix, n)
cosine_sig_matrix = cosine_signature(tfidf_matrix, n)

# Use LSH technique to construct candidate pairs
print("Finding candidate pairs for minhash signatures")
minhash_candidates = candidate_pairs(minhash_sig_matrix, b)
print("Finding candidate pairs for cosine distance signatures")
cosine_candidates = candidate_pairs(cosine_sig_matrix, b)

minhash_pairs = compare_candidate_signatures(cosine_candidates, cosine_sig_matrix, t)
cosine_pairs = compare_candidate_signatures(cosine_candidates, cosine_sig_matrix, t)
for x, y in cosine_pairs.union(minhash_pairs):
    print("%s similar to %s" % (files[x], files[y]))
