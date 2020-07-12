import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerBase

def pl(title, x, y1):
    fig, axL = plt.subplots(figsize=(4,3))
    axL.plot(x, y1, color='limegreen', marker=".", markersize=10)
    #plt.ylim(min(y1),max(y1))
    plt.title(title, color='k')
    plt.legend( ['corrected'])
    fig = plt.gcf()
    fig.set_size_inches((8, 5), forward=False)
    fig.savefig(title+".PNG", dpi=500)


x_list = []
df = pd.read_excel("results and charts.xlsx")
x = df.iloc[17:26,0]
y1 = df.iloc[17:26,19]
y2 = df.iloc[17:26,20]
y3 = df.iloc[17:26,21]

x = x.tolist()
y1 = y1.tolist()
y2 = y2.tolist()


pl("Noise = 0.3 - LR single", x, y2)
pl("Noise = 0.3 - mLTS single", x, y3)
