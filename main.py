import pandas as pd

# name=['python','java','c#','html','css',"ruby",'php']
# age=[30,24,54,2,5,9,12]
# data={'name':name,'age':age}

# df = pd.DataFrame(data) # this is for creating a dataframe 
# df.to_excel('data.xlsx',index=False) # to store the df as a excel sheet , index false means it will drop the index column 

# # print(df)

# df=pd.read_excel("data.xlsx") # read excel
# print(df.iloc[2])#to get the single  row 
# print(df['name'][2])  #  to get the single cell 
# print(df.tail())

# new_df=df.drop_duplicates() # drop duplicates 
# new_df = df.dropna() # drop null value 
# new_df.to_excel('na.xlsx')

# print(new_df)

# df['name'][2]='sharukh' # to edit cell data 
# df.to_csv("data.csv",index=False)


name=['python','java','c#','html','css',"ruby",'php']
print(name)
ds=pd.Series(name)
print(ds)