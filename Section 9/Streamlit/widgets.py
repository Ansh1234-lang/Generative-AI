import streamlit as st
import pandas as pd


st.title("streamlit Text Input")

name = st.text_input("enter your name: ")
if name :
    st.write(f"Hello {name}")


age = st.slider("select your age: " ,0,100,25)

st.write(f"your age is : {age}")

option = ['python', 'java', 'c++']
choice = st.selectbox("choose your favourite language: " , option)

st.write(f"you selected {choice}")

if name :
    st.write(f"hello, {name}")
    
data = {
    "Name": ["Yash", 'john','bob'],
    "Age": [23,31,24],
    "city":['NYC', 'LA', 'chicago']
}
df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)


uploaded_file = st.file_uploader("choose a CSV file ", type="csv")
if uploaded_file is not None:
    pd.read_csv(uploaded_file)
    st.write(df)
    