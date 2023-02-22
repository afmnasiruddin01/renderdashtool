
import plotly.express as px
import dash
from dash import Dash, html, dcc
import numpy as np
import pandas as pd
np.random.seed(10)

app = dash.Dash(__name__)
server = app.server

fig = px.scatter(x=[12, 15, 16, 50, 30], y=[1, 5, 6, 10, 8],
                 title="A plotly express figure")

# print(df.loc[:, 2013])
app.layout = html.Div([
              dcc.Graph(figure=fig)
])



if __name__ == "__main__":
    app.run_server(debug=True)
