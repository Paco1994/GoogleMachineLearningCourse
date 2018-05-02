import pandas as pd

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
print(type(cities['City name'][1]))
print(type(cities[0:2]))
cities['City name']