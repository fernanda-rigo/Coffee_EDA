import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('coffee-bean-production.csv', index_col=False)

coffee_production = df.rename(columns={'Crops - Coffee, green - 656 - Production - 5510 - tonnes' : 'production_tonnes'} ).drop (
	columns="Code")
to_remove = ['Africa','Americas','Asia','Caribbean','CentralAmerica','EasternAfrica','EasternAsia','EthiopiaPDR','Europe','EuropeanUnion','LandLockedDeveloping','Countries','Least','DevelopedCountries','LowIncomeFoodDeficitCountries','MiddleAfrica','Nicaragua','NorthernAmerica','Oceania','Polynesia','SouthAmerica','SouthEasternAsia','SouthernAsia','Southern','Europe','WesternAfrica','WesternAsia','World']

# print(coffee_production.Entity.unique())

# # print(to_remove)
entity_cp = coffee_production.loc[~coffee_production['Entity'].isin(to_remove)]
regions = coffee_production.loc[coffee_production['Entity'].isin(to_remove)]
country_cp= entity_cp.rename(columns={'Entity':'country', 'Year':'year'})
# print(country_cp.head())

country_cp_conv = country_cp.convert_dtypes()
# print(country_cp_conv.dtypes)

print(country_cp_conv.info())
# # to transform in numbers, we need to strip the whitespaces. I did it directly in the spreadsheet.
#
#
# df2 = pd.read_csv('pop_by_country.csv', index_col=False)
# # print(df2.head())
# population = df2
# # print(population.dtypes)
#
# coffee_prod_pop = country_cp_conv.merge(population, how = 'inner')
# # print(coffee_prod_pop.head())
# # print(coffee_prod_pop.dtypes)
# #
#
# # print(coffee_prod_pop.info())
#
#
# # Is there any relation between population size and coffe production?
# # considering only data were Minimum number of observations required per pair of columns to have a valid result.
# # correlation_pop_prod = coffee_prod_pop.corr(method= 'spearman', min_periods=1)
# # print(correlation_pop_prod)
#
# # New column:
#
# coffee_prod_pop['production_per_population'] = coffee_prod_pop['production_tonnes'] / coffee_prod_pop['population']
# # print('--------------production per population -----------------')
# notbr_coffe_production = coffee_prod_pop.loc[coffee_prod_pop.country != 'Brazil']
# notbr_cp_pop = notbr_coffe_production.groupby('year',as_index=False).sum()
# # print(notbr_cp_pop.head())
#
# brazil_coffee_production = coffee_prod_pop.loc[coffee_prod_pop.country == 'Brazil'].drop(columns = 'country')
# brazil_cp_pop = brazil_coffee_production
# brazil_cp_pop = brazil_cp_pop.rename(columns={'production_tonnes': 'brazil_production_tonnes'})
# # print(brazil_cp_pop.head())
# # print(type(brazil_cp_pop))
# print('-------------------------------')
#
# br_production = pd.DataFrame()
# # the population data is a str.
# br_production['year'] = brazil_cp_pop['year']
# br_production['brazil_production_tonnes'] = brazil_cp_pop['brazil_production_tonnes']
# notbr_production = pd.DataFrame()
# notbr_production['year'] = notbr_cp_pop['year']
# notbr_production['notbr_production_tonnes'] = notbr_cp_pop['production_tonnes']
# # print('--------------in Brazil-----------------')
# # # print(br_production.info())
# # print(br_production.head(5))
# # print('--------------not in Brazil-----------------')
# # print(notbr_production.head(5))
# print('--------------next-----------------')
#
# participation = br_production.merge(notbr_production, how='inner')
# print(participation.head(5))
#
# print('--------------total production population-----------------')
#
# total_coffee_production = coffee_prod_pop
# total_cp_pop = total_coffee_production.groupby('year',as_index=False).sum()
# total_cp_pop = total_cp_pop.rename(columns={'production_tonnes': 'total_production_tonnes'})
# # print(total_cp_pop.head(5))
# #
# # print('--------------total production-----------------')
#
# total_production = pd.DataFrame()
# total_production['year'] = total_cp_pop['year']
# total_production['total_production_tonnes'] = total_cp_pop['total_production_tonnes']
# # print(total_production.head(5))
# # print(total_production.info())
#
# # adding it to our participation dataset
#
# participation = br_production.merge(notbr_production, how='inner')
# # print(participation.head(5))
#
# # print('-------------- adding info -----------------')
#
# participation = participation.merge(total_production, how='inner')
# # print(participation.head())
# # participation.to_csv('br_participation_coffe_production_tones.csv')
#
# print('-------------- describing -----------------')
# # print(participation.describe())
# # print(participation.columns)
# participation['brazilian_participation_%'] = (participation['brazil_production_tonnes']*100)/participation[
# 	'total_production_tonnes']
# participation['nonbrazilian_participation_%'] = (participation['notbr_production_tonnes']*100)/participation[
# 	'total_production_tonnes']
# participation.to_csv('br_participation_coffe_production_tones.csv')
#
# print(participation.info())
#
# # # creating a plot
# # Coffe production compating Brazil, other countries and total
#
# fig2 = plt.style.use("seaborn")
# plt.plot(participation.year,participation.brazil_production_tonnes, label='Brazil')
# plt.plot(participation.year,participation.total_production_tonnes, label='World production')
# plt.plot(participation.year, participation.notbr_production_tonnes, label='Other countries')
# plt.xlabel('Years (1961 to 2018)')
# plt.title('Brazil vs. World coffe production')
# plt.legend()
# plt.show()
#
#
