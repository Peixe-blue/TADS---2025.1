"""
from functions.white_noise import white_noise
import plotly.express as px

time, values = white_noise(seed = 100)

px.line(
    x = time,
    y = values
 )
"""

import pandas as pd
import plotly.express as px

# read the data
df = pd.read_csv('data/coffee_sales.csv')
df.head(10)

# convert data column to datetime
df['data'] = pd.to_datetime(df['data'])
df.head()

# ensuring that date is in order
df = df.sort_values('data')
df.head()

# counting na's
df.isna().sum()

# plot time serie
fig = px.line(df,
    x='data',
    y='vendas',
    title='vendas diárias da cafeteria'
)

fig.update_layout(
    xaxis_title='Data',
    yaxis_title='Unidades vendidas'
)
fig.show()

# moving average
df['media_7_dias'] = df ['vendas'].rolling(7).mean()
df.head()

fig = px.line(df,
    x='data',
    y=['vendas', 'media_7_dias'],
    title='vendas diárias da cafeteria'
)

fig.update_layout(
    xaxis_title='Data',
    yaxis_title='Unidades vendidas'
)
fig.show()