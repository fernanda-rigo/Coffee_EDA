# preparing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.decomposition import PCA

# PREPARING
print('-------- PREPARING... -------')
coffe_production_v1 = pd.read_csv('coffee_production_countries.csv')
coffe_production = coffe_production_v1.drop ( columns=['Domain' , 'Element' , 'Item' , 'Unit'] )
coffe_production = coffe_production.rename ( columns={'Area' : 'country' , 'Value' : 'coffee_production_tonnes'} )
population_by_country_v1 = pd.read_csv ( 'population_bothsexes.csv' )
population_by_country = population_by_country_v1.drop ( columns=['Domain' , 'Element' , 'Item' , 'Unit'] )
population_by_country = population_by_country.rename ( columns={'Area' : 'country' , 'Value' : 'population(*1000)'} )
population_by_country['population'] = population_by_country['population(*1000)'] * 1000
population_by_country = population_by_country.drop ( columns=['population(*1000)'] )
rural_population_v1 = pd.read_csv ( 'rural_population_bothsexes.csv' )
rural_population = rural_population_v1.drop ( columns=['Domain' , 'Element' , 'Item' , 'Unit'] )
rural_population = rural_population.rename ( columns={'Area' : 'country' , 'Value' : 'rural_population(*1000)'} )
rural_population['rural_population'] = rural_population['rural_population(*1000)'] * 1000
rural_population = rural_population.drop ( columns=['rural_population(*1000)'] )
merged_pop = population_by_country.merge ( rural_population , how='inner') \
	.merge ( coffe_production , how='inner' )
merged_pop = merged_pop.dropna ()
merged_pop = merged_pop.replace({'Democratic Republic of the Congo':'Congo DR'})

# ANALYSE
print('-------- ANALYSE... -------')
print('-------- Part I -------')
# selecting rows for top20 largest producers, and organize
print('-------- KR1 - selecting the largest coffee producers ever -------')
largest_producers = merged_pop.groupby(by=["country"], dropna=True)['coffee_production_tonnes'].sum()
largest_producers = largest_producers.sort_values(ascending=False)
# print(largest_producers.head(20))
top20_largest_producers = largest_producers.iloc[0:20]
top20_largest_producers_list = top20_largest_producers.index.tolist()

top10_largest_producers = largest_producers.iloc[0:10]
top10_largest_producers_list = top10_largest_producers.index.tolist()
# print('TOP 20 and 10 largest coffee producers')
print(top20_largest_producers_list)
print(top10_largest_producers_list)
# print(largest_producers.head(20))

print('-------- KR2 - Who are the largest coffee producers during time?-------')
# print('TOP 20 largest coffee producers over years')
top20_yearly = merged_pop.loc[merged_pop['country'].isin(top20_largest_producers_list)]
top20_yearly = top20_yearly[['Year','country','coffee_production_tonnes']]
top20_yearly = top20_yearly.sort_values(['Year','coffee_production_tonnes'], ascending = [True, False])
# print(top20_yearly.tail(20))
#
fig1 = plt.figure(num = 1, figsize=(8, 6), constrained_layout = True)
ax = sns.lineplot(x="Year", y="coffee_production_tonnes",
             hue="country",
             data=top20_yearly)
sns.move_legend(ax, "upper left", bbox_to_anchor=(1,1),  frameon=True)
plt.title('TOP 20 largest coffee producers over 1961 - 2018')
plt.ylabel('Coffee production (tonnes)')
plt.xlabel('Year - 1961 to 2018')


print('TOP 10 largest coffee producers over years')
top10_yearly = merged_pop.loc[merged_pop['country'].isin(top10_largest_producers_list)]
top10_yearly = top10_yearly[['Year','country','coffee_production_tonnes']]
top10_yearly = top10_yearly.sort_values(['Year','coffee_production_tonnes'], ascending = [True, False])
# print(top10_yearly.tail(20))

fig2 = plt.figure(num = 2, figsize=(8, 6), constrained_layout = True)
ax1 = sns.lineplot(x="Year", y="coffee_production_tonnes",
             hue="country",
             data=top10_yearly)
sns.move_legend(ax1, "upper left", bbox_to_anchor=(1,1),  frameon=True)
plt.title('TOP 10 Coffee producers: 1961 - 2018')
plt.ylabel('Coffee production (tonnes)')
plt.xlabel('Year - 1961 to 2018')

print('Countries to investigate:')
countries_of_interest_list = ['Brazil', 'Colombia', 'Viet Nam', 'Indonesia']
countries_of_interest = merged_pop.loc[merged_pop['country'].isin(countries_of_interest_list)]
countries_of_interest = countries_of_interest.sort_values(['Year','coffee_production_tonnes'], ascending = [True,False])
countries_of_interest['rural_pop_percent'] = countries_of_interest['rural_population']/countries_of_interest['population']*100
countries_of_interest['total_pop_percent'] = 100 - countries_of_interest['rural_pop_percent']

print(countries_of_interest.head())
# countries_of_interest.to_csv('countries_of_interest.csv')

print('----- Sorting coffee production of Brazil, Colombia, VietNam and Indonesia over time' )
fig3 = plt.figure(num = 3, figsize=(8, 6), constrained_layout = True)
ax2 = sns.lineplot(x="Year", y="coffee_production_tonnes",
             hue="country",
             data= countries_of_interest)
sns.move_legend(ax1, "upper left", bbox_to_anchor=(1,1),  frameon=True)
plt.title('Coffe Production in Brazil, Colombia, VietNam and Indonesia')
plt.ylabel('Coffee production (tonnes)')
plt.xlabel('Year - 1961 to 2018')

print('----- KR3. How did the population of Brazil, Colombia, VietNam and Indonesia changed over time?----' )
fig4 = plt.figure(num = 4, figsize=(8, 6), constrained_layout = True)
ax3 = sns.lineplot(x="Year", y="rural_pop_percent",
             hue="country",
             data= countries_of_interest)
sns.move_legend(ax1, "upper left", bbox_to_anchor=(1,1),  frameon=True)
plt.title('Rural Population in Brazil, Colombia, Viet Nam, and Indonesia')
plt.ylabel('Rural population(%)')
plt.xlabel('Year - 1961 to 2018')

# plt.show()
# print('----- KR3. How did the population of Brazil, Colombia, VietNam and Indonesia changed over time?----' )
# x = countries_of_interest[['population','coffee_production_tonnes','Year','rural_pop_percent']]
# pca = PCA(n_components=3)
# components = pca.fit_transform(x)
# fig = px.scatter(components,x=0,y=1,color=ci['country'])
# fig.show()
#
#
