import matplotlib.pyplot as plt

def plot_similarities(similarity_matrix, work_names, work_index):
    names = [str(name) for name in work_names[:work_index] + work_names[work_index+1:]]
    scores = list(similarity_matrix[work_index])
    scores = scores[:work_index] + scores[work_index + 1:]

    fig, ax = plt.subplots() #This is only for testing purposes
    ax.bar(names, scores)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Compared works")
    ax.xaxis.set_label_coords(-0.1, -0.05)
    ax.tick_params(axis="x", labelrotation=90)
    ax.set_ylabel("Level of similarity")
    ax.set_title(f"How similar is {work_names[work_index]} to other works")
    plt.show()
    return ax #This is only for testing purposes

def plot_matrix(similarity_matrix, all_names, how):
    fig, ax = plt.subplots()
    ax.imshow(similarity_matrix, cmap=how)
    ax.set_xticks(range(len(all_names)), all_names, rotation=90)
    ax.set_yticks(range(len(all_names)), all_names)
    ax.set_title(f"Heatmap of how similar are Master's works to each other")
    plt.show()
    return ax
