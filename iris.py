import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from scipy.stats import pearsonr
from sklearn import linear_model, metrics
from sklearn.metrics import r2_score
from scipy import stats


st.set_page_config(layout="wide")
st.title('Analysis of Iris dataset - A case study for Streamlit')
df = px.data.iris()


st.markdown('***Iris dataframe***')
st.write(df)

st.subheader('Statistics for numeric variables')
columns = df.select_dtypes(include='number').columns
column = st.selectbox('Select numerical variable to explore column statistics', options=columns)
column = df[column]

# To render metrics
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Mean", column.mean())
col2.metric("Max", column.max())
col3.metric("Min", column.min())
col4.metric("Std", column.std())
col5.metric("Count", int(column.count()))

st.subheader('Statistics for categorical variables')

non_num_cols = df.select_dtypes(include=object).columns
column = st.selectbox("Select categorical variable for analysis", non_num_cols)
column = df[column]
st.markdown('***Unique counts for each species category***')
unique_values = column.value_counts()
st.write(unique_values)


# Data visualisation
st.header('Visualising relationship between numeric variables')
st.subheader('Pairplot analysis')
g = sns.pairplot(df, vars = ["sepal_length", "sepal_width", "petal_length", "petal_width"], dropna = True, hue = 'species', diag_kind="kde")
g.map_lower(sns.regplot)
st.pyplot(g)

st.subheader('Scatterplot analysis')
selected_x_var = st.selectbox('What do you want the x variable to be?', df.columns)
selected_y_var = st.selectbox('What about the y?', df.columns)
fig = px.scatter(df, x = df[selected_x_var], y = df[selected_y_var], color="species")
st.plotly_chart(fig)

#Correlation calculations (Pearson)
st.subheader("Pearson Correlation")
def calc_corr(selected_x_var, selected_y_var):
    corr, p_val = stats.pearsonr(selected_x_var, selected_y_var)
    return corr, p_val

x = df[selected_x_var].to_numpy()
y = df[selected_y_var].to_numpy()

correlation, corr_p_val = calc_corr(x, y)
st.write('Pearson correlation coefficient: %.3f' % correlation)
st.write('p value: %.3f' % corr_p_val)

#Correlation calculations (Spearman)
st.subheader("Spearman Correlation")
def calc_corr(selected_x_var, selected_y_var):
    corr, p_val = stats.spearmanr(selected_x_var, selected_y_var)
    return corr, p_val

x = df[selected_x_var].to_numpy()
y = df[selected_y_var].to_numpy()

correlation, corr_p_val = calc_corr(x, y)
st.write('Spearman correlation coefficient: %.3f' % correlation)
st.write('p value: %.3f' % corr_p_val)
