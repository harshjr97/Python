import pandas as pd
import matplotlib as mlb

# series
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
print(s)
print('\n\n')

##################################################################################

# data frame
data = {
    'Country': ['Belgium', 'India', 'Brazil'],
    'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
    'Population': [11190846, 13031035, 207847528]
}
df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
print(df)
print('\n\n')

##################################################################################

# read and write csv
pd.read_csv('weather.csv', header=None, nrows=5)
# df.to_csv('filename.csv')

##################################################################################

# read and write excel
# pd.read_excel('filename.xlsx')
# df.to_excel('name.xlsx', sheet_name='sheet1')

##################################################################################

# getting elements
# get one element by indexing
print(s['b'])
print('\n\n')

# get a subset of dataframe by slicing
print(df[1:])
print('\n\n')

##################################################################################

# selecting by position
# select single value by row
print(df.iloc[[0], [0]])
print('\n\n')

# select single value by column
print(df.iat[0, 0])
print('\n\n')

##################################################################################

# select by label
# select single value by row labels
print(df.loc[[0], ['Country']])
print('\n\n')

# by column label
print(df.at[0, 'Country'])
print('\n\n')

##################################################################################

# selecting by label/position
# selecting single row of subset of rows
# print(df.ix[2])

# select row and column
# print(df.ix[1, 'Capital'])

# select a single column of subset of column
# print(df.ix[:, 'Capital'])

##################################################################################

# selecting by boolean indexing
# series s where value is not > 1
print(s[~(s > 1)])
print('\n\n')

# s where value is <-1 or >2
print(s[(s > -1) & (s < 7)])
print('\n\n')

# use filter to adjust dataframe
print(df[df['Population'] < 13031035])
print('\n\n')

##################################################################################

# changing value by indexing
# set index a of series s to 6
s['a']=6
print(s)
print('\n\n')

##################################################################################

# dropping values
# drop values from rows (axis=0)
print(s.drop(['a', 'c']))
print('\n\n')

# drop values from columns (axis=1)
print(df.drop('Country', axis=1))
print('\n\n')

##################################################################################

# retrieving info about dataframe
print(df.shape)
print('\n\n')
print(df.index)
print('\n\n')
print(df.columns)
print('\n\n')
print(df.info())
print('\n\n')
print(df.count())
print('\n\n')

##################################################################################

# applying function
f = lambda x: x*2          # function
df.apply(f)                # apply function to dataframe
df.applymap(f)             # apply function to element wise
print('\n\n')

##################################################################################

# retrieving summary
print(df.sum())              # sum of values
print('\n\n')
print(df.cumsum())           # cummulatives sum of values
print('\n\n')
print(df.min())              # min value
print('\n\n')
print(df.max())              # max value
print('\n\n')
# print(df.idxmax())           # max index value
# print('\n\n')
# print(df.idxmin())           # min index value
print('\n\n')
print(df.describe())         # summary statistics
print('\n\n')
print(df.mean())             # mean of values
print('\n\n')
print(df.median())           # median of values
print('\n\n')

##################################################################################

# help
# help(pd.Series.loc)

##################################################################################

# internal data alignment
# NA values are introduced in the indices that don't overlap
s3 = pd.Series([17, -2, 3], index=['a', 'c', 'd'])
print(s + s3)
print('\n\n')

##################################################################################

# sort and rank
df.sort_index()
print('\n\n')
df.sort_values(by='Country')
print('\n\n')
df.rank()
print('\n\n')

##################################################################################

# arithmetic operations with fill methods
# print(s.add(s3, fill_value=0))
# print(s.sub(s3, fill_value=2))
# print(s.div(s3, fill_value=4))
# print(s.mul(s3, fill_value=3))

##################################################################################

# plot
# df.plot()                      line plot
# df.plot.bar()                  bare plot
# df.plot.hist(bins=12)          histogram
# df.plot.box()                  box plot
# df.plot.area()                 area plot
# df.scatter(x='a', y='b')       scatter plot
# df.pie()                       pie chart





