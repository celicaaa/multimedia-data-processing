import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
df=pd.read_csv('data1.csv',sep=';', decimal=',',index_col=0)
df.head()
print(df)
# pd.plotting.scatter_matrix(df,color='red')
fig=px.scatter_matrix(df)
fig.write_html("scatter_matrix.html")
fig = px.scatter_3d(df, x='oil', y='gas', z='coal', color='country')
fig.write_html("3d_plot1.html")
fig = px.scatter_3d(df, x='nuclear', y='hydroelectricity', z='renewables', color='country')
fig.write_html("3d_plot2.html")
fig = px.parallel_coordinates(df,color='oil',dimensions=['oil', 'gas', 'coal', 'nuclear', 'hydroelectricity', 'renewables'])
fig.write_html("parallel.html")
