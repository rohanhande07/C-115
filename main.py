import pandas as pd
import plotly.express as px

df = pd.read_csv("class1.csv")

score_list = df["Score"].tolist()
accepted_list = df["Accepted"].tolist()

fig = px.scatter(x=score_list, y=accepted_list)
fig.show()