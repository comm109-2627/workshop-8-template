from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt


def path_to_png(
    pathlist,
    filename="plot.png",
    grid_step=20,
    stroke="#2563eb",
    stroke_width=2,
    dpi=200,
):
    """
    Renders a list of two-point coordinates [((x1, y1), (x2, y2)), ...]
    onto a Cartesian (+) grid and saves directly to a PNG file.
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    # 1. Plot all line segments at once
    if pathlist:
        lc = LineCollection(
            pathlist, colors=stroke, linewidths=stroke_width, capstyle="round"
        )
        ax.add_collection(lc)

    # 2. Centre the X and Y spines at (0, 0) to form a '+' coordinate system
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # Style the axis lines
    ax.spines["left"].set_color("#475569")
    ax.spines["bottom"].set_color("#475569")
    ax.spines["left"].set_linewidth(1.2)
    ax.spines["bottom"].set_linewidth(1.2)

    # 3. Configure equal aspect ratio, grid intervals, and auto-scaling
    ax.set_aspect("equal", adjustable="datalim")
    ax.xaxis.set_major_locator(plt.MultipleLocator(grid_step))
    ax.yaxis.set_major_locator(plt.MultipleLocator(grid_step))
    ax.grid(True, which="both", color="#e2e8f0", linestyle="-", linewidth=0.8)
    ax.set_axisbelow(True)  # Keep grid lines behind your path segments
    ax.autoscale_view()

    # 4. Save directly to PNG
    plt.savefig(filename, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)  # Free memory after saving
