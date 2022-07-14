import pandas as pd 
'''
Initially we create an object of the entire xlsx file 
then we read excel for each different sheet as dataframe 

'''

xlsx=pd.ExcelFile("Data_Excel\Data_For_testing.xlsx") #Complete Excel file with both sheets as one object
df1=pd.read_excel(xlsx,'Sheet1') #From the entire excel file get single sheet value.
df2=pd.read_excel(xlsx,'Sheet2')
