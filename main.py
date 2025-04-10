#Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset
file_path="Market_Resercher_excel.xlsx"
data=pd.read_excel(file_path, sheet_name='market_researcher_dataset')
print("Market Resercher excel file successfully loaded")

#Cleaning the data
#Data Information
# Gives the information about the data
data.info()

#Perform the statistical function on the data
print(data.describe())

#Print the first 10 values.
df=data.head(10)
print("Printing the first ten rows",df)
#Pint last 10 rows
td=data.tail(10)
print("Printing the last 10 columns: \n",td)

#Is any null values are present or not if it is present then print how many null values are there 
print("Total null values: \n",data.isnull().sum())

#Objectives

#1. Finding the dominating Crop(product) in the market based on the demand and visualize the overall crop distribution 
products = data.groupby('Product')['Demand_Index'].count()
product=products.sort_values(ascending=False)
print("Total Products: ",product)
top=product.head(1)
print("Dominant crop(product) with count: \n",top)

plt.figure(figsize=(10,6))
plt.pie(product,labels=product.index,
        autopct="%1.1f%%", startangle=90)
plt.title("Crop Distribution in market")
plt.legend(title="Crops")
plt.show()

#2. To analyse the distribution of the Market price per ton to identify the market trends.
plt.figure(figsize=(10,5))
a=sns.histplot(data['Market_Price_per_ton'], bins=20, color="turquoise", edgecolor='black')
for i in a.patches:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width() / 2,height + 5,int(height),ha='center',fontsize=9)
        
plt.title("Distribution of Market Price")
plt.xlabel("Market Price (Per Ton)")
plt.ylabel("Frequency")
plt.show()


#3. To identify the relationship between comsumer trend and demand index using scatterplot
plt.figure(figsize=(10,6))
a=data['Consumer_Trend_Index'].head(1000)
b=data['Demand_Index'].head(1000)
sns.scatterplot(x=a, y=b,data=data,hue='Product', alpha=0.7)
plt.title('Consumer Trend vs Demand Index')
plt.xlabel('Consumer Trend Index')
plt.ylabel('Demand Index')

# 4. Finding the correlation between Market_Price and Competitor_Price
correlation=data[['Market_Price_per_ton', 'Competitor_Price_per_ton']].corr()
print("Correlation between Market_Price and Competitor_Price:")
print(correlation)
print(data[['Demand_Index', 'Supply_Index']].corr())


#5. Understand the relation between Market_Price, Demand_Index, Supply Index and Consumer_Trend_Index
plt.figure(figsize=(10,7))
corr=data[['Market_Price_per_ton','Demand_Index','Supply_Index','Consumer_Trend_Index']].corr()
sns.heatmap(corr, annot=True)
plt.title("Correlatipn Heatmap")
plt.show()

# 6. Line and bar plots for understanding the pricing trends of Product(Crops) by using market price (in tons) and competitior price (in tons)
price=data.groupby('Product')[['Market_Price_per_ton', 'Competitor_Price_per_ton']].mean()
val=price.plot(kind='bar', figsize=(10, 5))
plt.title("Average Market vs Competitor Price by Product")
plt.ylabel("Price (per ton)")
for container in val.containers:
    val.bar_label(container, fmt='%.2f', padding=3)
plt.show()

price.plot(kind='line', marker='^', figsize=(10, 5))
plt.title("Average Market vs Competitor Price by Product (Line Chart)")
plt.ylabel("Price (per ton)")
plt.xlabel("Product")
plt.grid(True)
plt.show()

# 7. Find over and under priced products using IQR
arr=np.array(data['Market_Price_per_ton'])
Q1=np.percentile(arr,25)
Q3=np.percentile(arr,75)

print("Q1: ",Q1)
print("Q3: ",Q3)
IQR=Q3-Q1
upper_bound = Q3 + 1.5*IQR
lower_bound = Q1 - 1.5*IQR
print("Upper bound of the market price: ",upper_bound)
print("Lower bound of the market price : ",lower_bound)
outlier_iqr=arr[(arr<lower_bound) | (arr>upper_bound)]
print("Outlier is: ",outlier_iqr)

#Boxplot Visualization of the market_price_per_ton
plt.figure(figsize=(6,4))
plt.boxplot(data['Market_Price_per_ton'],vert=False)    #(data)
plt.xlabel("Values")
plt.title("Box plot for Market outlier detection")
plt.show()

#8. Finding any invalid or an outlier that is present in Compettior_price 

arr=np.array(data['Competitor_Price_per_ton'])
mean_i=arr.mean()
std_i=arr.std(ddof=1)
z_score_i=(arr-mean_i)/std_i
outlier=arr[np.abs(z_score_i)>3]
print(outlier)
