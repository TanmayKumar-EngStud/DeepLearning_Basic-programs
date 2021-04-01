import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("pokemon.csv")
df = df.drop(["#","Type 1","Name","Type 2"], axis = 1)

df.to_csv("new.csv", sep= ",")

n=df.to_numpy()

x = n[0:,1]
y = n[0:,2]
plt.plot(x,y, "r. ", label = 'line')
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.show()
plt.savefig("status.jpg",dpi=300)