# session 3
'''
Using selenium and other packages can complement our test reports, emails or analysis from a web page

Reference: 
https://www.skytowner.com/explore/beautiful_soup_select_one_method
https://sparkbyexamples.com/pandas/pandas-count-frequency-value-occurs-in-dataframe-column
'''
import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


driver = webdriver.Chrome()
base_url = str("http://localhost:8080/8_using_panda.html")
driver.get(base_url)
time.sleep(3)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
div=soup.select_one("div table")
# with soup and select_one we are going to get the table(s) under a div
table=pd.read_html(str(div))
print(table)
# pandas has the capability to read a html and convert it to an actual "table"
df1 = table[0]['Assisted'].value_counts()
print(df1)
# pandas has the capability to read a html and convert it to an actual "table"
df2 = df1.plot(kind='pie', y='Assisted', autopct='%1.1f%%', startangle=15, shadow=True)

'''
my_data = [300, 500, 700]
my_labels = 'Tasks Pending', 'Tasks Ongoing', 'Tasks Completed'
my_colors = ['lightblue', 'lightsteelblue', 'silver']
my_explode = (0, 0.1, 0)
plt.pie(my_data, labels=my_labels, autopct='%1.1f%%', startangle=15, shadow=True, colors=my_colors, explode=my_explode)
plt.title('My Tasks')
plt.axis('equal')
plt.show()
'''