# preparing
import pandas as pd
# import numpy as np
# import matplotlib as plt
# import seaborn as sns

# loading first dataset

coffe_production_v1 = pd.read_csv('coffee_production_countries.csv')
print('-------- coffee production original dataset -------')
print(coffe_production_v1.info(10))
print(coffe_production_v1.head(5))
print('-------- preparing... -------')
coffe_production = coffe_production_v1.drop(columns= ['Domain', 'Element', 'Item', 'Unit'])
coffe_production = coffe_production.rename(columns={'Area': 'country', 'Value': 'coffee_production_tonnes'})
print(coffe_production.info(10))
print(coffe_production.head(5))
print('-------- next  -------')
print('-------- population original dataset -------')
population_by_country_v1 = pd.read_csv('population_bothsexes.csv')
print(population_by_country_v1.info())

print('-------- preparing -------')
population_by_country = population_by_country_v1.drop(columns=['Domain', 'Element', 'Item', 'Unit'])
population_by_country = population_by_country.rename(columns={'Area':'country', 'Value':'population(*1000)'})
population_by_country['population'] = population_by_country['population(*1000)']*1000
population_by_country = population_by_country.drop(columns=['population(*1000)'])
print(population_by_country.info())
print(population_by_country.head(5))

print('--------  rural population original dataset -------')
rural_population_v1 = pd.read_csv('rural_population_bothsexes.csv')

print('-------- preparing  -------')
rural_population = rural_population_v1.drop(columns=['Domain', 'Element', 'Item', 'Unit'])
rural_population = rural_population.rename(columns={'Area':'country', 'Value':'rural_population(*1000)'})
rural_population['rural_population'] = rural_population['rural_population(*1000)']*1000
rural_population= rural_population.drop(columns=['rural_population(*1000)'])
print(rural_population.info())
print(rural_population.head(5))

# merging datasets
print('-------- merging -------')
merged_pop = population_by_country.merge(rural_population, how='inner')
merged_pop_cp = merged_pop.merge(coffe_production, how='inner')
print(merged_pop.head())
print(merged_pop_cp.head())

# dropping NA values
print('-------- dropping NA values -------')
merged_pop_cp = merged_pop_cp.dropna()

print('--------  SAVING CSV FILES -------')
merged_pop_cp.to_csv('coffee_production_population.csv')

