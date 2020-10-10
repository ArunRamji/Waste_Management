import streamlit as st
from Image_Classification import *
import time

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style.css")
st.title("Image Classification of ""Bio-degradable"" and ""Non Bio-degradable"" waste ")
st.header("We are going predict whether uploaded object image is Degradable or Not")
st.write("Created on Oct'03 2020")
st.write("@Author: Arun Ramji Shanmugam")
st.write("________________________")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write("Please upload an Image")


uploaded_file = st.file_uploader("Choose an Image ...", type="jpg")
if uploaded_file is not None:
    #image = Image.open(uploaded_file)
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = machine_classification(uploaded_file,'model1.h5')
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
    if label == 1:
        st.subheader('RESULT :')
        t = "<div>As per our AI Engine - There is a higher chance that it is a<span class='highlight'> <span class='bold'> benign</span> </span> Non Degradable Object!</div>"
        st.markdown(t, unsafe_allow_html=True)
    else:
        st.subheader('RESULT :')
        t = "<div>As per our AI Engine - There is a chance that it is a<span class='highlight'> <span class='bold'> Degradable Object</span> </span> melanoma!</div>"
        st.markdown(t, unsafe_allow_html=True)
        
     
  
    
    
    st.write("______________________________________")
    st.write(" ")
    st.write("Disclaimer : What ever the prediction made by our App is purely for educational and training purpose!!")   


