import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px 
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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

## plotting churn proportion in client database 
st.subheader("Proportion of churn")
st.markdown("""
    The dataset is not balanced as less than 20% have churned
""")

c_labels = ['Retain', 'Churn']
fig = go.Figure(data=[go.Pie(labels=c_labels, 
                             values=data['TARGET'].value_counts(), 
                             hole=.3,
                            )
                     ]
               )

# fig.update_trace(color_discrete_sequence=["red", "blue"])

fig.update_layout(
    title_text="Churn distribution",
    title_x = 0.5,
    legend=dict(
        orientation="v",
        yanchor="top",
        y=1.0,
        xanchor="left",
        x=1
    ),
    legend_tracegroupgap = 90
    )
config = {'displaylogo': False}

st.plotly_chart(fig, use_container_width=True)

## plotting categorical features 
st.subheader("Distribution of categorical features")
st.markdown("""
    Few coutries represent the majority of clients""")

fig = px.pie(data,names='COUNTRY',title='Proportion Of country client',hole=0.33)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
    Flagship is a flag to follow important clients by sales teams""")

fig = px.pie(data,names='IS_FLAGSHIP',title='Propotion of flagued clients',hole=0.33)
st.plotly_chart(fig, use_container_width=True)


fig = px.pie(data,names='MAIN_ENTITY',title='Proportion of main entity clients',hole=0.33)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
   Some outliers are shown below """)

fig = px.pie(data,names='PLAN',title='Proportion of plan type',hole=0.33)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
   Few outliers also here """)

fig = px.pie(data,names='BUNDLE',title='Proportion of bundle type',hole=0.33)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
   INdustry type is a key caracteristic """)

fig = px.pie(data,names='AGG_INDUSTRY',title="Client's type of industry",hole=0.33)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Distribution of nuemric features")
st.markdown("""
    """)

#plotting distubiroin and boxplot of temporal features 
st.subheader("Distribution of numeric features")
st.markdown("""
    Few coutries represent the majority of clients""")
fig = make_subplots(rows=2, cols=1)

tr1=go.Box(x=data['TENURE'],name='Tenure Box Plot',boxmean=True)
tr2=go.Histogram(x=data['TENURE'],name='Tenure Histogram')

fig.add_trace(tr1,row=1,col=1)
fig.add_trace(tr2,row=2,col=1)

fig.update_layout(height=500, width=1000, title_text="Distribution of Client Tenure")
st.plotly_chart(fig, use_container_width=True)

#plotting NPS clients distribution
fig = make_subplots(rows=2, cols=1)
tr1=go.Box(x=data['NPS'],name='NPS Box Plot',boxmean=True)
tr2=go.Histogram(x=data['NPS'],name='NPS Histogram')

fig.add_trace(tr1,row=1,col=1)
fig.add_trace(tr2,row=2,col=1)

fig.update_layout(height=500, width=1000, title_text="Distribution of Client NPS")
st.plotly_chart(fig, use_container_width=True)

#distribution of number of plastic card payment by the client
fig = make_subplots(rows=2, cols=1)

tr1=go.Box(x=data['NB_PLASTIC_CARD_PAYMENTS'],name='NB_PLASTIC_CARD_PAYMENTS Box Plot',boxmean=True)
tr2=go.Histogram(x=data['NB_PLASTIC_CARD_PAYMENTS'],name='NB_PLASTIC_CARD_PAYMENTS Histogram')

fig.add_trace(tr1,row=1,col=1)
fig.add_trace(tr2,row=2,col=1)

fig.update_layout(height=500, width=1000, title_text="Distribution of number of plastic card payments per client")
st.plotly_chart(fig, use_container_width=True)

#### Create two columns

### Side bar 
st.sidebar.header("Predicting churn rate")
st.sidebar.markdown("""
    * [Proportion of churn](#proportion-of-churn)
    * [Distribution of categorical features](#distribution-of-churn-by-country)
    * [Distribution of numeric features"](#target-relation-with-categorical-variables)
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