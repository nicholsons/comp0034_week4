# Import the required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import os

# Import the data set
DATA_DIR = 'data'
purchase_data = os.path.join(DATA_DIR, 'purchase_data.csv')
df = pd.read_csv(purchase_data)
df['spend'] = df['price'] * df['quantitiy']
df = df[['date', 'place', 'spend']]
df = df.groupby(['date', 'place']).sum().reset_index()

# Create the Plotly figure (bar chart from the previous activity)
fig = px.bar(df, x="spend", y="date", color="place", title="Purchases by place")

# Create a Dash app (if you use a stylesheet in the assets folder you will need to use __name__ in the constructor).
app = dash.Dash(__name__)

# Create the app layout and add the bar chart to it
app.layout = html.Div(children=[

    html.H1('Lollapalooza experience'),
    html.H2('How did I spend my money?'),
    dcc.Graph(figure=fig),

])

# Run the web app server
if __name__ == '__main__':
    app.run_server(debug=False, port=8050)
