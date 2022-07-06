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
# Population and coffee production...
merged_pop = population_by_country.merge ( rural_population , how='inner') \
	.merge ( coffe_production , how='inner' )
merged_pop = merged_pop.dropna ()
countries_of_interest_list = ['Brazil', 'Colombia', 'Viet Nam', 'Indonesia']
countries_of_interest = merged_pop.loc[merged_pop['country'].isin(countries_of_interest_list)]
countries_of_interest = countries_of_interest.sort_values(['Year','coffee_production_tonnes'], ascending = [True,False])

# print(countries_of_interest.head())

print('------- agregando mais dados-------------')
# produto interno bruto

pib = pd.read_csv('gdp_value_per_capita_countriesofinterest.csv')
pib = pib.drop ( columns=['Domain' , 'Item','Element'])
pib = pib.rename ( columns={'Area' : 'country', 'Value':'GDP_dollars_per_capita'} )
# print(pib['country'].unique())

# renda nacional bruta

rnb = pd.read_csv('gross_national_income_value_per_capita_countriesofinterest.csv')
rnb = rnb.drop ( columns=['Domain', 'Item', 'Element'])
rnb = rnb.rename ( columns={'Area' : 'country', 'Value':'GNI_dollars_per_capita'} )
# print(rnb['country'].unique())

# gross_output_agriculture_value_countriesofinterest


gpv = pd.read_csv('gross_production_values_countriesofinterest.csv')
gpv = gpv.drop(columns=['Domain', 'Item', 'Element', 'Unit' ])
gpv = gpv.rename(columns={'Area': 'country', 'Value': 'GPV*100'})
# print(gpv['country'].unique())

# employment_agriculture_countriesofinterest

employment = pd.read_csv('employment_agriculture_countriesofinterest.csv')
employment = employment.drop(columns=['Domain','Indicator', 'Sex', 'Source','Unit'])
employment = employment.rename(columns={'Area': 'country', 'Value': 'Employment*1000'})
# print(employment['country'].unique())
# coffe_export_quantity_countriesofinterest
#
# coffee_exported = pd.read_csv('coffe_export_quantity_countriesofinterest.csv')
# coffee_exported = coffee_exported.drop(columns = ['Domain','Element', 'Item','Unit'])
# coffee_exported = coffee_exported.rename(columns={'Area': 'country', 'Value': 'coffe_exported_tonnes'})
# # roasted coffe export
#
# roasted_coffee_exported = pd.read_csv('roasted_coffe_export_quantity_countriesofinterest.csv')
# roasted_coffee_exported = roasted_coffee_exported.drop(columns = ['Domain','Element', 'Item','Unit'])
# roasted_coffee_exported = roasted_coffee_exported.rename(columns={'Area': 'country', 'Value': 'roasted_coffe_exported_tonnes'})

# Preparing data for PCA
PCA_data = countries_of_interest.merge(pib, how='inner') \
	.merge(rnb, how='inner') \
	.merge(gpv, how='inner')\
	.merge(employment, how='inner')
x = PCA_data[['Year', 'coffee_production_tonnes', 'GDP_dollars_per_capita','GNI_dollars_per_capita', 'GPV*100']]
pca = PCA(n_components=4)
components = pca.fit_transform(x)
fig = px.scatter(components,x=1,y=0,color=PCA_data['country'])
fig.show()





