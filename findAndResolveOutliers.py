import seaborn as sb 
import pandas as pd

df = pd.read_csv("./pokemon_data.csv")
sb.boxplot(y="HP", data = df)