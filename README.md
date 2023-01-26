# **Dilated cardiomyopathy (DCM) prediction app using RNA-seq data**

## **Table of contents:**

- [About the web application](#about-the-webapp)
- [Structure of the repository](#structure-of-the-repository)
- [Credits](#credits)
- [Further details](#details)
- [Contact](#contact)

## **About the project**

App to predict if a patient has DCM or not based on RNA-seq data.

<a href="https://rnaseq-cardiomyopathies-pred.streamlit.app/" title="rnaseq-cardiomyopathies-pred"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"></a><br>

![ampredst-gif](./RnaseqCMs.gif)

## **Structure of the repository**

The main files and directories of this repository are:

|File|Description|
|:-:|---|
|[RandomForestClassifier_NF_DCM_impgenes.bin](RandomForestClassifier_NF_DCM_impgenes.bin)|Bin file of the best classifier|
|[streamlit_app.py](streamlit_app.py)|Script for the streamlit web application|
|[requirements.txt](requirements.txt)|File with names of the packages required for the streamlit web application|
|[style.css](style.css)|css file to customize specific feature of the web application|

## **Credits**

- This app was developed for a group project of a course from the [Master's degree in Systems Biology](https://www.maastrichtuniversity.nl/education/master/systems-biology) at [Maastricht University](https://www.maastrichtuniversity.nl/).
- Developed by [Sebastián Ayala Ruano](https://sayalaruano.github.io/).
- The training [dataset](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE141910) was obtained from the The [Myocardial Applied Genomics Network (MAGNet)](https://www.med.upenn.edu/magnet/) project.

## **Further details**
More details about the exploratory data analysis, data preparation, and model selection are available in this [GitHub repository](https://github.com/sayalaruano/Project3Period-SysBioMaster).


## **Contact**
If you have comments or suggestions about this project, you can [open an issue](https://github.com/sayalaruano/ML_AMPs_prediction_streamlitapp/issues/new) in this repository, or email me at sebasar1245@gamil.com.
