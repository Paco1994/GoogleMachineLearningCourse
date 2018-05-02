#
# The reindex method allows index values that are not in the original DataFrame's index values. 
# Try it and see what happens if you use such values! Why do you think this is allowed?
# 

import pandas as pd
import numpy as np

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']


# Starts the exercise
print(cities.reindex(np.random.permutation(cities.index)))
# np.random.permutation(cities.index) shuffles the values of the array

print(cities.reindex[0,0,0]); # San Francisco, San Francisco, San Francisco
print(cities.reindex[1,1,1]); # San José, San José, San José
print(cities.reindex[2,2,2]); # Sacramento, Sacramento, Sacramento

print(cities.reindex[0,4,2]); # San Francisco, NaN, Sacramento
print(cities.reindex[5,3,1]); # NaN, NaN, San José