import pandas as pd
import matplotlib.pyplot as plt

print("Pandas version --> " + pd.__version__)

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

data_frame = pd.DataFrame({ 'City name': city_names, 'Population': population })


california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
describe = california_housing_dataframe.describe()
head = california_housing_dataframe.head()
hist = california_housing_dataframe.hist('housing_median_age')
plt.savefig('image.png')

print ("Data Frame: ")
print (data_frame)
print ("\nCalifornia Housing Dataframe: ")
print (california_housing_dataframe)
print ("\nDescribe: ")
print (describe)
print ("\nHead: ")
print (head)