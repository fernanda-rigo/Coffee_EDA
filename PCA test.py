import plotly.express as px
from sklearn.decomposition import PCA
import pandas as pd

ci = pd.read_csv('countries_of_interest.csv')
print(ci.columns)
x = ci[['population','coffee_production_tonnes','Year','rural_pop_percent']]
pca = PCA(n_components=3)
components = pca.fit_transform(x)
fig = px.scatter(components,x=1,y=0,color=ci['country'])
fig.show()



