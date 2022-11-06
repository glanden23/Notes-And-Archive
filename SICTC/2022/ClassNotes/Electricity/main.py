import pandas as pd
import matplotlib.pyplot as plt
from random import randint
data = pd.read_csv("elec_access_data.csv")

validCountries = ["Greece", "Hungary", "Sweden", "Denmark", "Norway"]

for i in validCountries:
    years = data[data["Entity"]==i]['Year']
    access = data[data["Entity"]==i]["Access"]
    plt.plot(years,access,label=i)
plt.ylabel("% of Country Population")
plt.xlabel("Year")
plt.legend()
plt.title("% of Population with electricity")
plt.show()