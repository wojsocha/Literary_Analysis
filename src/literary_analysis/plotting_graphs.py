import matplotlib.pyplot as plt

def plot_similarities(similarity_matrix, work_names, work_index):
    names = work_names[:work_index] + work_names[work_index+1:]
    scores = similarity_matrix[work_index]
    scores = scores[:work_index] + scores[work_index + 1:]

    fig, ax = plt.subplots() #This is only for testing purposes
    ax.bar(names, scores)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Compared works")
    ax.set_ylabel("Level of similarity")
    ax.set_title(f"How similar is {work_names[work_index]} to the other works")
    plt.show()
    return ax #This is only for testing purposes
