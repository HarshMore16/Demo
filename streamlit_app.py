import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


data =pd.read_csv('Data/iris.csv')
st.title("IRIS flower Dashboard")
with st.sidebar:
    st.subheader("Description")
    st.caption("The Iris flower data set or Fisher's Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.[1] It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.[2] Two of the three species were collected in the Gaspé Peninsula all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus")


col1, col2  = st.columns(2)
with col1:
    class_data= data['Species'].value_counts()
    st.subheader("Pie chart of species")
    fig1 ,ax = plt.subplots()
    x=["setosa","versicolor","virginica"]
    ax.pie(class_data,labels=x)
    st.pyplot(fig1)

with col2:
    class_data= data['Species'].value_counts()   
    st.subheader("Pie chart of species")
    fig ,ax = plt.subplots()
    x=["setosa","versicolor","virginica"]
    ax.bar(x,class_data)
    st.pyplot(fig)
st.line_chart(data[['SepalLength','SepalWidth','PetalLength','PetalWidth']])

col3, col4, col5  = st.columns(3)   
with col3:
    st.subheader("scatter plot")
    st.scatter_chart(data=data, x='SepalLength',y='SepalWidth')

with col4:
    sc_x=px.scatter_3d(data,x='SepalLength',y='SepalWidth',z='PetalLength')
    col4.plotly_chart(sc_x,use_container_width=True)

with col5:
    st.subheader("scatter plot")
    st.scatter_chart(data=data, x='PetalLength',y='PetalWidth')

