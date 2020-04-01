import numpy as np
import pandas as pd
import ternary

# test
def main():
    # paths to equilibrium data
    path_meoh = r"data\MeOH_H2O_Limonene.csv"
    path_etoh = r"data\EtOH_H2O_Limonene.csv"
    # read equilibrium data from csv
    df_meoh = pd.read_csv(path_meoh)
    df_etoh = pd.read_csv(path_etoh)
    # plot 2 phase triangle diagram for methanol,water, limonene system
    scale = 1.0
    fontsize = 14
    # create empty ternary plot
    label1 = ["Methanol", "Water", "Limonene"]
    label2 = ["Ethanol", "Water", "Limonene"]
    ternary_plot_empty(
        df_meoh,
        r"figures\MeOH_ternary.png",
        label1,
        scale,
        fontsize,
        ["blue", "red"],
        ["Aqueous", "Organic"],
    )
    ternary_plot_empty(
        df_etoh,
        r"figures\EtOH_ternary.png",
        label2,
        scale,
        fontsize,
        ["red", "blue"],
        ["Organic", "Aqueous"],
    )


def ternary_plot_empty(df, opp, label, scale, fs, phasecolor, phase):
    ## Boundary and Gridlines
    figure, tax = ternary.figure(scale=scale)
    tax.boundary(linewidth=2.0)
    tax.gridlines(color="blue", multiple=0.1, linewidth=0.5)

    # set axis labels and title
    tax.get_axes().axis("off")
    tax.clear_matplotlib_ticks()
    side_offset = -0.03
    # Set Axis labels and Title
    tax.right_corner_label(label[2], fontsize=fs, offset=side_offset)
    tax.top_corner_label(label[1], fontsize=fs, offset=0.2)
    tax.left_corner_label(label[0], fontsize=fs, offset=side_offset)

    # Set ticks
    tax.ticks(axis="lbr", linewidth=1, multiple=0.1, tick_formats="%.1f", offset=0.02)

    # Remove default Matplotlib Axes
    tax.clear_matplotlib_ticks()
    """Create points for plot
       add data (Limonene, water, methanol)
    """

    curve_1 = [
        (i, j, k) for i, j, k in zip(df.iloc[:, 2], df.iloc[:, 0], df.iloc[:, 1])
    ]
    curve_2 = [
        (i, j, k) for i, j, k in zip(df.iloc[:, 5], df.iloc[:, 3], df.iloc[:, 4])
    ]
    for p1, p2 in zip(curve_1, curve_2):
        tax.line(p1, p2, linewidth=0.5, color="black")
    tax.scatter(curve_1, color=phasecolor[0], label=phase[0])
    tax.scatter(curve_2, color=phasecolor[1], label=phase[1])
    tax.legend()
    """This ensures that the labels are included in the saved graphs
    """
    tax._redraw_labels()
    ternary.plt.savefig(opp)


if __name__ == "__main__":
    main()
