import matplotlib.pylab as plt
import matplotlib.dates as mdates


def plotDataFrame(df):
    my_fmt = mdates.DateFormatter('%d-%m-%y')

    fig = plt.figure(figsize=(16, 8))
    ax = plt.axes()

    ax.set_xlabel('Time')
    ax.set_ylabel('Popularity')
    ax.xaxis.set_major_formatter(my_fmt)

    # Aesthetics
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for column in df.columns[1:]:
        plt.plot(df[column][-52:])

    ax.legend(list(df.columns[1:]))

    for tick in ax.get_xticklabels():
        tick.set_rotation(45)

    plt.show()