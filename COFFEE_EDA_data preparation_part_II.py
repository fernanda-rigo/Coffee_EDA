# preparing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
print('-------- O1 - KR1 = Who are the largest coffee producers during time?-------')
# selecting rows for top20 largest producers, and organize
print('-------- selecting the largest coffee producers ever -------')
largest_producers = merged_pop.groupby(by=["country"], dropna=True)['coffee_production_tonnes'].sum()
largest_producers = largest_producers.sort_values(ascending=False)
# print(largest_producers.head(20))
top20_largest_producers = largest_producers.iloc[0:20]
top20_largest_producers_list = top20_largest_producers.index.tolist()

top10_largest_producers = largest_producers.iloc[0:10]
top10_largest_producers_list = top10_largest_producers.index.tolist()
print('TOP 20 and 10 largest coffee producers')
print(top20_largest_producers_list)
print(top10_largest_producers_list)
# print(largest_producers.head(20))

print('TOP 20 largest coffee producers over years')
top20_yearly = merged_pop.loc[merged_pop['country'].isin(top20_largest_producers_list)]
top20_yearly = top20_yearly[['Year','country','coffee_production_tonnes']]
top20_yearly = top20_yearly.sort_values(['Year','coffee_production_tonnes'], ascending = [True, False])
print(top20_yearly.tail(20))

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
print(top10_yearly.tail(20))

fig2 = plt.figure(num = 2, figsize=(8, 6), constrained_layout = True)
ax1 = sns.lineplot(x="Year", y="coffee_production_tonnes",
             hue="country",
             data=top10_yearly)
sns.move_legend(ax1, "upper left", bbox_to_anchor=(1,1),  frameon=True)
plt.title('TOP 10 Coffee producers: 1961 - 2018')
plt.ylabel('Coffee production (tonnes)')
plt.xlabel('Year - 1961 to 2018')
plt.show()
