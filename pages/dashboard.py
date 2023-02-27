import streamlit as st
from matplotlib import image
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import os

df=pd.read_csv(r'C:\Users\Naveen\Pictures\Projects\company_data.csv')



st.subheader('Top 10 Companies Based On Market Cap')
fig1=plt.figure(figsize=(10,5))
plt.barh(df.Company_Names[0:10],df['Market_Cap(In_Billion_USD)'][0:10],color='red',edgecolor='blue')
plt.xlabel('Market Cap',fontsize=25)
plt.ylabel('Company_Names',fontsize=25);
st.pyplot(fig1)

st.subheader('Count of Headquarter of Company')

fig=plt.figure()
df['Headquarter_of_Company'].value_counts().plot(kind="bar")
st.pyplot(fig)
