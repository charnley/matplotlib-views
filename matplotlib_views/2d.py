

def show_2d(matrix, xaxis, yaxis):


    mappable = ax.imshow(timings, cmap="PuRd")
    # fig.colorbar(mappable)

    ax.set_xticks(list(range(len(xaxis))))
    ax.set_xticklabels(xaxis)

    ax.set_yticks(list(range(len(yaxis))))
    ax.set_yticklabels(yaxis)

    # ax.set_xlabel("len(compounds)")
    # ax.set_ylabel("len(assays)")

    # Start lowest in bottom
    ax.invert_yaxis()

    return mappable



