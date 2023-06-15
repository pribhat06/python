import pandas as pd
'''df = pd.DataFrame([[1, 2, 3], [3, 4, 5], [5, 6, 7], [7,8, 9]], index = ['a', 'b', 'c', 'd'],
                  columns = ['x', 'y', 'z'])


print(df)'''


weather_df = pd.read_csv("C:/Users/priya/Documents/python-for-data-engineering-main/python-for-data-engineering-main/4. Python Advance/data/weather_2012.csv")
print("Shape:", weather_df.shape)
print("Index: ", weather_df.index)

print(weather_df.head())
print(weather_df['Date/Time'].head())
print(type(weather_df['Date/Time'].head()))

