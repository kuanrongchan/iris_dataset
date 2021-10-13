# PlotlyExpress Iris dataset analysis
Example of how we can use Streamlit for building data dashboards.
The step-by-step explanation for each code synthax is detailed in omicsdiary.com. 

# Part I
Python is often used in back-end programming, which builds functionality in web applications. For instance, Python can be used to connect the web to a database, so that users can query information. By adding the backend components, Python turns a static webpage into a dynamic web application, where users can interact with the webpage based on an updated and connected database. If data provided is big, developers can even use the machine learning tools in Python to make data predictions. However, front-end development, which is the part of making website beautiful and interactive webpages, is often done with other programming languages such as HTML, CSS and JavaScript. The question remains, do I need to be a full-stack developer to master both front-end and back-end web development? This can be time-consuming as this means you have to learn multiple languages. This is where Streamlit, Django and Flask comes into the rescue! These are built on the Python programming language, and allows building of websites with minimal knowledge on CSS and JavaScript. With more experience, I decided to focus on Streamlit as the syntax are easier to understand and the deployment is more rapid.

First, we will create a file called iris.py. Part I will focus on getting basic stats from a dataset. The packages required are:

````````
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
from typing import Any, List, Tuple
````````

Data is obtained from plotlyexpressed, using the iris dataset
``````
df = px.data.iris()
``````

To get basics stats for continuous variables:
``````
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Mean", column.mean())
col2.metric("Max", column.max())
col3.metric("Min", column.min())
col4.metric("Std", column.std())
col5.metric("Count", int(column.count()))
``````

To get stats for categorical variables, 
Wordcloud function:
``````
non_num_cols = df.select_dtypes(include=object).columns
column = st.selectbox("Select column to generate wordcloud", non_num_cols)
column = df[column]
wc = WordCloud(max_font_size=25, background_color="white", repeat=True, height=500, width=800).generate(' '.join(column.unique()))
st.image(wc.to_image())
``````
Number of categories and sample size:
``````
unique_values = column.value_counts()
st.write(unique_values)
``````
