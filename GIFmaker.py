import matplotlib.pyplot as plt
from Point import Point
import imageio

def saveAsGIF(tabu, points, path="img\\"):
    
    
    size_min = -5
    size_max = 80
    filenames = []

    for i in range(len(tabu.permutationHistoryGlobal)):
        perm_g = tabu.permutationHistoryGlobal[i]
        perm_l = tabu.permutationHistoryLocal[i]
        x_g = []
        y_g = []
        x_l = []
        y_l = []
        
        for j in range(len(perm_g)):
            x_g.append(points[perm_g[j]].x)
            y_g.append(points[perm_g[j]].y)
            x_l.append(points[perm_l[j]].x)
            y_l.append(points[perm_l[j]].y)

        fig, ax = plt.subplots(1, 2, figsize=(20,10))
        ax[0].plot(x_g, y_g, zorder=1, linewidth=5)
        ax[0].scatter(x_g, y_g, color='orange', zorder=2, s=120)
        ax[0].set_xlabel("X")
        ax[0].set_ylabel("Y")
        ax[0].set_title("Global best permutation")
        # ax[0].set_xlim([size_min, size_max])
        # ax[0].set_ylim([size_min, size_max])
        ax[1].plot(x_l, y_l, zorder=1, linewidth=5)
        ax[1].scatter(x_g, y_g, color='orange', zorder=2, s=120)
        ax[1].set_xlabel("X")
        ax[1].set_ylabel("Y")
        ax[1].set_title("Local best permutation")
        # ax[1].set_xlim([size_min, size_max])
        # ax[1].set_ylim([size_min, size_max])
        fig.savefig(path + str(i) + ".png")
        filenames.append(path + str(i) + ".png")
        plt.close()
    
    with imageio.get_writer(path + 'mygif.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)