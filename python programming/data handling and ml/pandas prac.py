import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

#giving data to convert it into pandas series(1d array of pands)
data = [1,2,3,4,5]
index = ["a","b","c","d","e"]
#series me ham data or index(a,b,c) dete hai
series = pd.Series(data,index=index)#2nd method to make series"pd.Series(np.random.rand(5))"
#making sries from dict
dic = {"ankit":"coder","deepak":"cse","sanjay":"enge","sangeeta":"house wife"}
dic_series = pd.Series(dic)

#DataFrame
data1 = pd.Series([0.111,0.122,0.133,0.144,0.155])
data2 = pd.Series([0.011,0.122,0.233,0.344,0.455])
data = (data1,data2)
df = pd.DataFrame(data)
#if we want to give name to colums
df = pd.DataFrame({"High":data1,"Close":data2})
df.index = [1,2,3,4,5]#if we want to change index name
df.columns = list("123")#change column name in one line code if we want oto writte singel character name
print("data is",df)
#if we want to change value


#|||Some functions
'''df.to_csv("csv data file.csv")#if we want to convert this data into Excel form.if you dont want see index writte "index=Fals"
print(pd.read_csv("csv data file.csv"))#to read exesting csv file data in python
print(df.head(2))#if you have large data and want to see only limited line from up ward
print(df.tail(2))#if you have large data and want to see only limited line from down ward
print(df.describe())#if you want numeric column count,mean,std,min,25%,50%,75%,max
print(df.index)#to print all index name in dataframe
print(df.to_numpy)#to convert dataframe into numpy array
print(df.sort_index(axis=0,ascending=False))#agar ham index ko ulta kerna chate hai to "ascending=False or axis=0" kerdenge agar column ulte kerne hai to "axis=1" kerdena hai
'''

#Access series element
#print(def[column ka nam] [row ka nam])
#print(df,"\n",df["High"][2])