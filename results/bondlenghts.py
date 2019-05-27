import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = pd.read_csv("bondlengths.txt")
print(df.head())
print(df.info())


plt.plot(df["Molecules"], df["MC"])
plt.show()
