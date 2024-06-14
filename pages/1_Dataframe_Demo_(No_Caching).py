import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib inline
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import plotly.express as px
import calendar
import matplotlib.ticker as mticker
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title('Consumer Behavior at Retail Store')

st.markdown(
    """
    Berikut adalah insight-insight yang ditemukan mulai dari EDA sampai Machine Learning
    """
)
    df=pd.read_csv("dataset/Retail_Transaction_Dataset.csv")

    df_prod = df.groupby('ProductCategory')
Product_sales = df_prod['Quantity'].sum().sort_values(ascending=False).rename('Total Sales')
Product_sales

plt.figure(figsize=(5, 3))
sns.barplot(data=df, x='ProductCategory', y='Quantity', estimator=sum, errorbar=None)
plt.title('Total Sales Quantity by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Quantity')
plt.ylim(122000, 127000)  # Adjust the range of y-axis here
plt.tight_layout()
plt.show()
