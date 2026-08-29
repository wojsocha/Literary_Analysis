from collections import Counter
import numpy as np
import literary_analysis.stats as stats

def distribution(counter, n):
    all = sum(counter.values())
    first_n = stats.top_n_sorter(counter, n)
    counter_normalized = Counter({word: count/all for word, count in first_n})
    return counter_normalized

# def entropy(counter, n):
#     _, values = distribution(counter, n)
#     p = np.array(values)
#     entropy = -np.sum(p*np.log(p))
#     return entropy
