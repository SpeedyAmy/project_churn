# How to predict a Fintech's client from churning

The objective of this project is to predict whether a client (enterprise) of a B2B fintech will churn or not.
The fintech provides a software that helps companies to manage their finance.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

### Data

I worked on this project in collaboration with a fintech who provided me with their real business data. They asked me to challenge their machine learning prediction model. 
I used a csv file where clients related data was extracted every month with informations like churning date if exists, usage of the budget solution maangement, general informations about the client, marketing data ...
The file can not be shared in this repo for abvious confidentiality reasons.

### Prerequisites

The source code is written in Python 3
The python packages can be installed with pip : pip3 install or !pip install if in jupyter notebook

### Installing

You will need the following Python libraries to be installed or imported

* mlxtend 
* pandas as pd
* numpy as np
* sklearn libraries
* matplotlib.pyplot as plt
* seaborn as sns
* plotly.express as px
* plotly.graph_objects as go
* plotly.io as pio
* plotly.offline as py
* plotly.subplots import make_subplots
* time
* warnings
* warnings.filterwarnings("ignore", category=DeprecationWarning) # to avoid deprecation warnings


## Deployment

If you need to deploy this repo, you will have to have the datastet (private for now)

## Built With

* understanding_data.ipynb : 
Automates some computations of basic statistics for most features in the dataset (as no documentation was available to get the meaning of all features)
* preprocessing.ipynb :
Creates a new dataset after cleaning the raw data, automates other visualisations, preprocesses data with sklearn and trains some classifiers from scikit-learn and compare their performances

## Authors

**Amina Nasri** - [SpeedyAmy](https://github.com/SpeedyAmy)

## Acknowledgments

Many thanks to the company's data science team who trusted me with their data and provided me with precious explanations and business insights
I was inspired by this Kaggle competition for the vizualisation and exploration of data https://www.kaggle.com/code/mekhdigakhramanian
