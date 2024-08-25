# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kod0EzMOEFWcKD0t5U7nC2ErpATi98uh
"""

import pandas as pd

pd.__version__
#gives pandas version
#2.1.4

#series using list

lst=[1,2,3,4,5,6]
print(lst)
#[1, 2, 3, 4, 5, 6]

series = pd.Series(lst)
print(series)
#key->value pair(with indexs)
#0    1
#1    2
#2    3
#3    4
#4    5
#5    6
#dtype: int64

empty = pd.Series()
print(empty)
#empty series
#Series([], dtype: object)

a = pd.Series(['p','q','r','s','t'],index=[10,11,12,13,14])
print(a)
#key->value pair(with custom indexs)
#10    p
#11    q
#12    r
#13    s
#14    t
#dtype: object

a = pd.Series(['p','q','r','s','t'],index=[10,11,12,13,14],name='alphabets')
print(a)
#key->value pair(with custom indexs) and name
#10    p
#11    q
#12    r
#13    s
#14    t
#Name: alphabets, dtype: object

scalar_series = pd.Series(0.5)
print(scalar_series)
#0    0.5
#dtype: float64

scalar_series = pd.Series(0.5,index=[1,2,3])
print(scalar_series)
#0    0.5
#1    0.5
#2    0.5
#dtype: float64
#all values filled with 0.5

#series using dictionary

dict_series= pd.Series({'p':1,'q':2,'r':3,'s':4,'t':5})
print(dict_series)
#key->value pair
#p     1
#q     2
#r     3
#s     4
#t     5
#dtype: int64

dict_series[0]
#gives value at index 0
dict_series.index[0]
#gives index at index 0

dict_series[0:3]
#p	1
#q	2
#r	3
# dtype: int64

max(dict_series)
#gives max value

dict_series =pd.Series({'p':[1,5,6],'q':[2,5,6],'r':[3,5,6],'s':[4,5,6],'t':[5,5,6]})
print(dict_series)
#dictionary along with list
#p    [1, 5, 6]
#q    [2, 5, 6]
#r    [3, 5, 6]
#s    [4, 5, 6]
#t    [5, 5, 6]
# dtype: object

#dataframes
#collection of data that contains rows and columns
df=pd.DataFrame()
print(df)
#empty dataframe
#Columns: []
#Index: []

lst=[1,2,3,4,5]
df=pd.DataFrame(lst)
print(df)
#dataframe using list
#    0
#0  1
#1  2
#2  3
#3  4
#4  5

lst =[[1,2,3,4,5],[11,12,13,14,15]]
df =pd.DataFrame(lst)
print(df)
#dataframe using list
#   0  1  2  3  4
#0  1  2  3  4  5
#1 11 12 13 14 15

a = [{'a':5,'b':7,'c':9,'d':2},{'a':4,'b':8,'c':19,'d':12}]
df=pd.DataFrame(a)
print(df)
#dataframe using dictionary
#   a  b  c  d
#0  5  7  9  2
#1  4  8 19 1

b ={'RollNo':pd.Series([1,2,3,4,5]),'Maths':pd.Series([67,89,23,90,56]),'Physics':pd.Series([12,98,44,90,78])}
df=pd.DataFrame(b)
print(df)
#dataframe using dictionary
#    RollNo  Maths  Physics
#0       1     67       12
#1       2     89       98
#2       3     23       44

#common seperated value
d =pd.read_csv('/content/sample_data/california_housing_test.csv')
d

type(d)

# functions on data frame

df = pd.read_csv('/content/sample_data/california_housing_test.csv')
df

df.columns
#gives list of columns

df.shape
#(row,col)

df.size
#total number of elements row*col

df.head()
#gives first 5 rows

df.head(2)
#gives first 2 rows

df.tail()
#gives last 5 rows

df.tail(3)
#gives last 3 rows

df.describe()
#gives statistical values
#eg count-total entries
#std
#min
#mean,etc

df.info()
#gives info about data
#info about columns

# how to handle missing and null values
df.isnull()
#if true then null
#if false then not null

df.isnull().sum()
#gives total null values in each column

df.isnull().sum().sum()
#gives total null values

#drop row having null value
df2 = df.dropna()
df2

df2.shape

#drop colums with null values
df3=df.dropna(axis=1)
df3

df.dropna(how='any') #drop row if any row value is null

df.dropna(how='all')
#drop row if all values are null

df.dropna(inplace=True)
#replace original data frame eith not null data frame

# fill the empty values with 0
df.fillna(0)

df.fillna(2)
#fill na with 2

df.fillna({'	longitude':'none','latitude':35})

df.fillna(method='ffill')
#fill na with previous value
#forward fill

df.fillna(method='bfill')
#fill na with next value
#backward fill

df.fillna(method='bfill',axis=1)#col wise

df['longitude'].fillna(value=df['longitude'].mean())
#fill na with mean of column

df.fillna(method='ffill',inplace=True)
#change original df

df.replace(to_replace=37.37,value=38.38)
#replace 37.37 with 38.38

df.replace(to_replace=[50,51,52,53,54,55,56,57,58,59],value='A')
#replace values with A

df.replace(to_replace=[50,51,52,53,54,55,56,57,58,59],value=['A','B','C','D','E','F','G','H','I','J'])
#replace values with list

df.replace('[A-Za-z]',0,regex=True)
#replace alphabets with 0

df.replace(to_replace='A',method='ffill')
#replace A with previous value

#loc and iloc
df.loc[1]
#gives row at index 1 data

df.loc[10]

df.loc[[5,6,7,8,1]]
#gives rows (col values) at index 5,6,7,8,1

df.loc[5,'longitude']
#gives value of longitude at index 5

df.loc[5:15,'longitude']
#gives values of longitude from index 5 to 15

df.loc[df['longitude']<-120]
#gives rows where longitude is less than -120

df.loc[df['latitude']>37,'longitude']
#gives values of longitude where latitude is greater than 37

#index location iloc
df.iloc[0]
#gives row at index 0

df.iloc[[0]]
#gives row at index 0

df.iloc[:,0]
#gives all rows of column at index 0

df.iloc[0:5,1]
#gives rows from index 0 to 5 of column at index 1

df.iloc[0:5,1:4]
#gives rows from index 0 to 5 of columns from index 1 to 4

#GROUPING DATA
latitude_group=df.groupby(by='latitude')
latitude_group

latitude_group.groups
#gives groups

df.groupby(['latitude','longitude']).groups
#group by longitude and latitude

for group,data_frame in latitude_group:
  print(group)
  print(data_frame)

df1=pd.DataFrame({'Roll No.':[1,2,3,4,5],'Chemistry':[78,33,39,81,90]})
df2=pd.DataFrame({'Roll No.':[1,2,3,4,5],'Maths':[78,33,39,81,9]})
df3=pd.DataFrame({'Roll No.':[1,2,3,4,5],'Physics':[78,33,39,81,9]})

pd.merge(df1,df2,on='Roll No.')
#merge data frame 1 and 2 on roll number

pd.merge(df2,df3)
#merge data frame 2 and 3
#based on roll number by default

df4=pd.DataFrame({'Roll No.':[1,2,3,4,5],'Chemistry':[78,33,39,81,90]})
df5=pd.DataFrame({'Roll No.':[1,2,3,7,8],'Maths':[70,80,90,81,9]})
df6=pd.merge(df4,df5,on='Roll No.')
df6
#merge only common roll numbers

pd.merge(df4,df5,on='Roll No.',how='left')
#merge only roll numbers in left that is df4

pd.merge(df4,df5,on='Roll No.',how='right')
#merge only roll numbers in right that is df5

pd.merge(df4,df5,on='Roll No.',how='outer')
#merge all roll numbers

df7 = pd.DataFrame({'Roll No.':[1,2,3,4,5],'Maths':[78,33,39,81,90]})
df8= pd.DataFrame({'Roll No.':[6,7,8,9,10],'Maths':[30,34,56,78,90]})

#df7.append(df8) not a function now was in older version
result=pd.concat([df7,df8])
result

pd.concat([df7,df8],ignore_index=True)
#ignore index

pd.concat([df7,df8],ignore_index=True,sort=True)
#sort by index

df9=pd.DataFrame({'Roll No.':[1,2,3,4,5],'Maths':[78,33,39,81,90],'Physics':[40,50,60,70,80]})
df10=pd.DataFrame({'Roll No.':[6,7,8,9,10],'Maths':[80,90,20,30,70],'Chemistry':[70,13,25,70,69]})

pd.concat([df9,df10])

pd.pivot_table(df,index=['latitude'],aggfunc='mean')
#avg and corresponding columns

pd.pivot_table(df,index=['latitude'],aggfunc='sum')
#sum and corresponding columns

pd.pivot_table(df,index=['latitude'],aggfunc='count')
#count and corresponding columns

pd.pivot_table(df,index=['latitude'],aggfunc='max')
#max and corresponding columns
