# Web app
import streamlit as st
from annotated_text import annotated_text
from millify import millify
import plotly.express as px
# OS and file management
import os
import pickle
from PIL import Image
import zipfile
# Data analysis
import pandas as pd

# General options
im = Image.open("favicon.ico")
st.set_page_config(
    page_title="Cardiomiopathy prediction app",
    page_icon=im,
    layout="wide",
)

# Attach customized ccs style
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Function load the best ML model
@st.experimental_singleton 
def load_model(model_file):
    with open(model_file, 'rb') as f_in:
        model = pickle.load(f_in)
    return model 

# Add a title and info about the app
st.title('Dilated cardiomyopathy (DCM) prediction app using RNA-seq data')

with st.expander('About this app'):
    st.write('''
    App to predict if a patient has DCM or not based on RNA-seq data. 
    
    **Credits**
    - This app was developed for a group project of a course from the [Master's degree in Systems Biology](https://www.maastrichtuniversity.nl/education/master/systems-biology) at [Maastricht University](https://www.maastrichtuniversity.nl/).
    - Developed by [Sebastián Ayala Ruano](https://sayalaruano.github.io/).
    - The training [dataset](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE141910) was obtained from the The [Myocardial Applied Genomics Network (MAGNet)](https://www.med.upenn.edu/magnet/) project.
      ''')

# Input peptide
st.sidebar.subheader('Input Rnaseq data')

rnaseq_data = st.sidebar.file_uploader("Upload your Rnaseq data in CSV format", type=['csv'], help='Be sure to upload a CSV file with the RNA-seq data in the same format as the example file.')

st.sidebar.write('You can find examples of healthy and DCM RNAseq data in csv file [here](https://github.com/sayalaruano/RNAseq_cardiomyopathies_pred/tree/main/Examples).')

# Predict button
if st.sidebar.button('Predict'):
    load_data = pd.read_csv(rnaseq_data)

    st.subheader('Input data:')
    st.write(load_data)

    # Load the model
    model_file = 'RandomForestClassifier_NF_DCM_impgenes.bin'
    model = load_model(model_file)
    
    # Predict the AMP activity
    y_pred = model.predict_proba(load_data)[0, 1]
    active = y_pred >= 0.5

    # Print results
    st.subheader('Prediction of the cardiomiopathy status using the best ensemble-based model:')
    if active == True:
      annotated_text(
      ("The sample has DCM", "", "#ea9999"))
      annotated_text(
      "Probability of DCM:",
      (f"{y_pred}","", "#ea9999"))
    else:
      annotated_text(
      ("The sample is healthy", "", "#b6d7a8"))
      annotated_text(
      "Probability of DCM:",
      (f"{y_pred}","", "#b6d7a8"))
else:
    st.subheader('Welcome to the app!')
    st.info('Upload your Rnaseq data in CSV format in the sidebar to proceed', icon='👈')

st.sidebar.header('Code availability')

st.sidebar.write('The code for this project is available under the [MIT License](https://mit-license.org/) in this [GitHub repo](https://github.com/sayalaruano/RNAseq_cardiomyopathies_pred). If you use or modify the source code of this project, please provide the proper attributions for this work.')

st.sidebar.header('Support')

st.sidebar.write('If you like this project, please give it a star on the [GitHub repo](https://github.com/sayalaruano/ML_AMPs_prediction_streamlitapp) and share it.')

st.sidebar.header('Contact')

st.sidebar.write('If you have any comments or suggestions about this work, please DM by [twitter](https://twitter.com/sayalaruano) or [create an issue](https://github.com/sayalaruano/RNAseq_cardiomyopathies_pred/issues/new) in the GitHub repository of this project.')


