from collections import Counter
import numpy as np
import literary_analysis.stats as stats

def distribution(counter, n, with_ties=False):  #If we want to compare 2 distributions, they need to have the same amount of weights to reasonably compare them
    all = sum(counter.values())                 #This is not an actual prob. distribution, but rather distribution without its tail
    first_n = stats.top_n_sorter(counter, n, with_ties)
    counter_normalized = Counter({word: count/all for word, count in first_n})
    return counter_normalized

def L1_distance(distr1, distr2):
    words = set(distr1) | set(distr2)
    p = np.array([distr1[word] for word in words])
    q = np.array([distr2[word] for word in words])
    return np.linalg.norm(p - q, ord=1)

def weighted_Jaccard(distr1, distr2):
    words = set(distr1) | set(distr2)
    p = np.array([distr1[word] for word in words])
    q = np.array([distr2[word] for word in words])
    numerator = np.minimum(p, q).sum()
    denominator = np.maximum(p, q).sum()
    if denominator == 0:    #Both p and q are arrays of zeros, that shouldn't happen
        raise ValueError("Both distributions are empty")
    return numerator / denominator

def similarity(distr1, distr2, alpha):
    if not 0 <= alpha <= 1:
        raise ValueError("alpha must be a number between 0 and 1")
    return 100 * (alpha * weighted_Jaccard(distr1, distr2) + (1 - alpha) * (1 - 0.5 * L1_distance(distr1, distr2)))
