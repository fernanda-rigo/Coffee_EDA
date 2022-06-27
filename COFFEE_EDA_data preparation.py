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

# Dropping and editing...
# drop(Domain, Element, Item, Unit)
coffe_production = coffe_production_v1.drop(columns= ['Domain', 'Element', 'Item', 'Unit'])
# rename('Area' = 'country'
# rename('Value' = 'coffee_production_tonnes')
coffe_production = coffe_production.rename(columns={'Area': 'country', 'Value': 'coffee_production_tonnes'})
print(coffe_production.info(10))
print(coffe_production.head(5))

print('-------- next  -------')


print('-------- population original dataset -------')
population_by_country_v1 = pd.read_csv('population_bothsexes.csv')
print(population_by_country_v1.info())
# population_by_countr
print('-------- preparing -------')
# drop(columns=['Domain', 'Element'])
# rename(columns={'Area':'country', 'Value':'population'})
population_by_country = population_by_country_v1.drop(columns=['Domain', 'Element', 'Item', 'Unit'])
population_by_country = population_by_country.rename(columns={'Area':'country', 'Value':'population(*1000)'})
print(population_by_country.info())
print(population_by_country.head(5))

print('--------  rural population original dataset -------')
rural_population_v1 = pd.read_csv('rural_population_bothsexes.csv')
print(rural_population_v1.info())
print(rural_population_v1.head(5))
print('-------- preparing  -------')
rural_population = rural_population_v1.drop(columns=['Domain', 'Element', 'Item', 'Unit'])
rural_population = rural_population.rename(columns={'Area':'country', 'Value':'rural_population(*1000)'})
print(rural_population.info())
print(rural_population.head(5))

# merging datasets
print('-------- merging -------')

coffeeproduction_population = coffe_production.merge(population_by_country, how='inner')
coffeeproduction_population_rural = coffe_production.merge(rural_population, how='inner')

# dropping NA values
print('-------- dropping NA values -------')
coffeeproduction_population = coffeeproduction_population.dropna()
coffeeproduction_population_rural = coffeeproduction_population_rural.dropna()
print('-------- Coffee_production vs. total population -------')

print(coffeeproduction_population.info())
print('--------  Coffee_production vs. rural population-------')
print(coffeeproduction_population_rural.info())

print('--------  SAVING NEW TABLES -------')


print('--------  LET S TO TABLEAU -------')

coffeeproduction_population.to_csv('coffee_production_population.csv')
coffeeproduction_population_rural.to_csv('coffee_production_rural_population.csv')






