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
merged_pop = population_by_country.merge ( rural_population , how='inner' )
merged_pop_cp = merged_pop.merge ( coffe_production , how='inner' )
merged_pop_cp = merged_pop_cp.dropna ()
# ANALYSE
print('-------- ANALYSE... -------')
highest_producers_alltime = merged_pop_cp.pivot_table(merged_pop_cp)
