import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Load Dataset
file_path="Market_Resercher_excel.xlsx"
data=pd.read_excel(file_path, sheet_name='market_researcher_dataset')
print("Load Successfully")

#Cleaning of the data
#Data Information
# Gives the information about the data
data.info()

#Perform the statistical function on the data
print(data.describe())

#Is any null values are present or not if it is present then print how many null values are there 
print("Total null values: \n",data.isnull().sum())
