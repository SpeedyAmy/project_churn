import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px 
import plotly.graph_objects as go


### Config
st.set_page_config(
    page_title="Predicting churning rate",
    #page_icon="💸 ",
    layout="wide"
)

#DATA_URL = ('https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/e-commerce_data.csv')

### App
st.title("Predicting churn rate")

st.markdown("""
    Welcome to this dashboard. 
    You can learn more about the data used to predict the clients churn a B2B startup. 
    The data comes from the startup cutomer database with informations about customer caracterictics.
    Let's check it out 👇
""")

# Use `st.cache` when loading data is extremly useful
# because it will cache the data so that the app 
# won't have to reload it each time you refresh your app
@st.cache
def load_data(nrows):
    #here we will put raw data with all exploration job done before the preprocessing for training model
    #exploring data from base_client (row=unique client)
    data = pd.read_csv("db_clients.csv", nrows=nrows) 
    #data["Date"] = data["Date"].apply(lambda x: pd.to_datetime(",".join(x.split(",")[-2:])))
    #data["currency"] = data["currency"].apply(lambda x: pd.to_numeric(x[1:]))
    return data

st.subheader("Load and showcase data")
st.markdown("""
    text 
""")

data_load_state = st.text('Loading data...')
data = load_data(100)
data_load_state.text("") # change text from "Loading data..." to "" once the the load_data function has run

## Run the below code if the check is checked ✅
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)    

## Churn rate
st.subheader("Proportion of churn")
st.markdown("""
    text
""")
labels = 'Churned', 'Retained'
sizes = [data.TARGET[df_client['TARGET']==1].count(), data.TARGET[data['TARGET']==0].count()]
explode = (0, 0.1)
fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Proportion of customer churned and retained", size = 20)
st.plt.show()

### TAREGT relation with categorical variables
st.subheader("TAREGT relation with categorical variables")
st.markdown("""
    text
""")  
fig, axarr = plt.subplots(2, 2, figsize=(20, 12))
st.sns.countplot(x='COUNTRY', hue = 'TARGET',data = data, ax=axarr[0][0])
st.sns.countplot(x='INDUSTRY', hue = 'TARGET',data = data, ax=axarr[0][1])
st.sns.countplot(x='AGG_INDUSTRY', hue = 'TARGET',data = data, ax=axarr[1][0])
st.sns.countplot(x='IS_FLAGSHIP', hue = 'TARGET',data = data, ax=axarr[1][1])


### Input data 
st.subheader("Input data")
st.markdown("""
    text
""")

#### Create two columns

### Side bar 
st.sidebar.header("Predicting churn rate")
st.sidebar.markdown("""
    * [Proportion of churn](#proportion-of-churn)
    * [Distribution of churn by country](#distribution-of-churn-by-country)
    * TAREGT relation with categorical variables](#target-relation-with-categorical-variables)
    * [Input Data](#input-data)
""")
e = st.sidebar.empty()
e.write("")
st.sidebar.write("Made with passion by Amina Nasri")

### Footer 
empty_space, footer = st.columns([1, 2])

with empty_space:
    st.write("")

with footer:
    st.markdown("""
        🍇
        If you want to learn more, check out [my repo on github](https://docs.streamlit.io/) 📖
    """)