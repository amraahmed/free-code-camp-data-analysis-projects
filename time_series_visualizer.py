import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to "date".)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=["date"],index_col="date")

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025))&
    (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(figsize=(10,5))
    ax.plot(df.index,df["value"],"r",linewidth=1)
    ax.set_title("Fourm Views")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")





    # Save image and return fig (don"t change this part)
    fig.savefig("line_plot1.png")
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(["year","month"])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot.bar(legend=True,figsize=(13,6),ylabel="Average Page Views",xlabel="Years").figure
    plt.legend(['jan','Feb','Mar','Apr','May','Jun','jul','Aug','Sep','Oct','Nov','Dec'])
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)

    # Save image and return fig (don"t change this part)
    fig.savefig("bar_plot12.png")
    return fig