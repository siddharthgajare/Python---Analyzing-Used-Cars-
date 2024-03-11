import ax as ax
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv('CarsDekho.csv')
#print(df)

df1 = df.head(5)
#print(df1)

df2 = df.shape
#print(df2) # Rows*Columns

#df3 = df.info()

df4 = df.isnull().sum() #Checking if there are Null values in the dataset. (0 null values found)

#Finding Dataset Data

(df.name.unique()) #print
(sorted(df.year.unique())) #print
(df.fuel.unique()) #print
(df.owner.unique()) #print
(df.seller_type.unique()) #print
(df.transmission.unique()) #print


# Top 5 Brand Sold Most Cars (Text)

Brand_Sold = df["brand"] = df.name.apply(lambda x : ' '.join(x.split(' ')[:1]))
Brand_Sold = df.brand.value_counts().sort_index(ascending=False).sort_values(ascending=False).head(5)
print('\nThe top 5 most cars sold by brands are:\n')
print(Brand_Sold)

# Most Sold Car Models(Bar Plot)

df["name"].value_counts(normalize = False)[:10].plot(kind = 'bar',color='skyblue',figsize=(20,25))
plt.suptitle('Most Cars Sold By Models', fontsize=30,fontweight="bold")
plt.xticks(fontsize=18, rotation=90,fontweight="bold")
plt.yticks(fontsize=20, rotation=90,fontweight="bold")
plt.xlabel('Models', fontsize=25)
plt.ylabel('Total Sold', fontsize=25)
plt.savefig('Most Sold Cars')
plt.show()

# Percentage Sales of the Brands
df["brand"] = df.name.apply(lambda x : ' '.join(x.split(' ')[:1]))
labels = df["brand"][:20].value_counts().index
sizes = df["brand"][:20].value_counts()
data = df.groupby(['brand'])['brand'].count().sort_values(ascending=False)
x = data.index
y = data.values
colors = ['#76EEC6','#E3CF57','#8A2BE2','#EE3B3B',"#76EE00","#FF7D40","#FF34B3"]
plt.figure(figsize = (10,10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%',colors=colors, startangle=90)
plt.title('Percent Sales by Brands',color = 'black',fontsize = 30,fontweight="bold")
plt.legend(title = "Cars")
plt.savefig('Percent Sales of Brands')
plt.show()

# Average Selling Price of Brand
df["brand"] = df.name.apply(lambda x : ' '.join(x.split(' ')[:1]))
price = df.groupby(['brand'])[['selling_price']].mean()
price.sort_values(by='selling_price', ascending=True, inplace=True)
AvgBrand = price.plot(kind='barh', figsize=(15,15) ,title= 'Average Brand Selling Price',color='green')
for c in AvgBrand.containers:
    AvgBrand.bar_label(c, fmt='%.0f',label_type='center', color='white')
plt.savefig('Average Brand Selling Price')
plt.show()


# Which model year people are purchasing
df.year.value_counts()

sns.countplot(data=df,x="year",palette="Blues_d")
plt.xticks(rotation=90)
plt.xlabel("Model Year",fontsize=15,color="red")
plt.ylabel("Cars Sold",fontsize=12,color="red")
plt.title("Model Year Most Purchased",color="RED",fontweight="bold")
plt.savefig('Model Year')
plt.show()

# Most cars sold to type of owner

df["owner"].value_counts(sort = True).plot(kind="bar", color=["#8B2252"], figsize=(15, 20))
plt.xlabel("Type of the Owner",fontsize=22,color="#8B2252")
plt.ylabel("Cars Sold",fontsize=22,color="#8B2252")
plt.title("Cars Owners Type",color="#8B2252",size = 25,fontweight="bold")
plt.savefig('Owner Type')
plt.show()


# Most cars purchased by the fuel type
df["fuel"].value_counts(sort =True).plot(kind="bar", color=["#FFEC8B"], figsize=(10,10))
plt.xlabel("Fuel Type",fontsize=12,color="red")
plt.ylabel("Total Car's Purchased",fontsize=12,color="red")
plt.title("Fuel Type Purchases",color="RED",fontweight="bold")
plt.savefig('Fuel Type')
plt.show()

# Most cars purchased by the transmission type
df["transmission"].value_counts(sort = True).plot(kind="barh", color=["#9F79EE"], figsize=(10, 6) , title='Transmission')
plt.xlabel("Number of cars Purchased",fontsize=12,color="#5D478B")
plt.ylabel("Transmission Type",fontsize=12,color="#5D478B")
plt.title("Transmission People Preferred",color="#5D478B",fontweight="bold")
plt.savefig('Transmission Type')
plt.show()

# RELATIONSHIP BETWEEN VARIOUS FACTORS

# Factors affecting the prie of car.
#1. Year - Price
def line_plot(data, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, palette="summer", linewidth=5.0)
    plt.title(title, fontsize=16,fontweight="bold")
    plt.ylabel(ylabel, size=14)
    plt.xlabel(xlabel, size=15)

df_price_move = df.groupby(['year'])[['selling_price']].mean()
line_plot(df_price_move, 'Price to Year', 'Year Manufactured', "Price Range")
plt.savefig('Price_Year Relationship')
plt.show()

#2. Km Driven - Price
df.plot(x="km_driven", y="selling_price", kind="scatter", figsize=(10, 6), color="#8B2252")
plt.xlabel("Km Car Driven",fontsize=18,color="black")
plt.ylabel("Sold For Range",fontsize=18,color="black")
plt.title("Km Driven to Price Relationship",color="black",size = 25,fontweight="bold")
plt.savefig('KmDriven_Price_Relationship')
plt.show()

# Correlation Matrix
corr = df.corr()
corr = corr['selling_price']
corr = corr.sort_values(ascending=False)
sns.heatmap(df.corr(), annot=True, cmap='plasma')
plt.savefig('Corr Price')
plt.show()

# WordCloud

WordC = df["brand"] = df.name.apply(lambda x : ' '.join(x.split(' ')[:1]))
text = ' '.join(df['brand'])
plt.rcParams['figure.figsize'] = (12,12)
wordcloud = WordCloud(background_color = 'Grey',colormap='Accent', width = 1200,  height = 1200, max_words = 121).generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('WordCloud')
plt.show()



