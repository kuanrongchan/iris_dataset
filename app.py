import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud


st.set_page_config(layout="wide")
st.title('Data analysis of iris dataset from PlotlyExpress')
df = px.data.iris()


st.markdown('***Iris dataset from PlotlyExpress***')
st.write(df)

columns = df.select_dtypes(include='number').columns
column = st.selectbox('Select data column to explore stats', options=columns)
column = df[column]

# To render metrics
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Mean", column.mean())
col2.metric("Max", column.max())
col3.metric("Min", column.min())
col4.metric("Std", column.std())
col5.metric("Count", int(column.count()))

# Build wordcloud
non_num_cols = df.select_dtypes(include=object).columns
column = st.selectbox("Select column to generate wordcloud", non_num_cols)
column = df[column]
wc = WordCloud(max_font_size=25, background_color="white", repeat=True, height=500, width=800).generate(' '.join(column.unique()))
st.image(wc.to_image())

st.markdown('***Counts in selected column for generating WordCloud***')
unique_values = column.value_counts()
st.write(unique_values)