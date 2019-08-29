# importing pandas package 
import pandas as pd 
from pandas import ExcelWriter
from pandas import ExcelFile

# making data frame from csv file 
data = pd.read_excel("./ARC-DATA/dummy/Un/PGG-SBM_Final_Email_List.all.xlsx") 

# sorting by email address
data.sort_values("Email Address", inplace = True) 

# dropping ALL duplicte values 
data.drop_duplicates(subset ="Email Address", 
					keep = False, inplace = True) 

# displaying data 
data 
# print(data)

df = data

writer = ExcelWriter('./ARC-DATA/dummy/Un/PGG-SBM_Final_Email_List.all-dd.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()