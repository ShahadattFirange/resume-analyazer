import streamlit as st
import pandas as pd
import numpy as np
st.title("Helllo GPT")

question = st.text_input("Ask your question")
st.write("This is my first streamlit app")
st.text("let's get started")

name = st.text_input("enter your name")

if st.button("greet"):
    st.success(f"Hello, {name}")

upload_file = st.file_uploader("upload a csv", type='csv')
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.header("thismis header")
st.subheader("this is sub header")
st.markdown("[Link](https://streamlit.io/)")
st.text_area("write your message")
st.number_input('pick a number', min_value=0, max_value=10)
st.slider("choose a range", 0, 100)
st.selectbox("select a fruit", ["apple", "banana", "chicku"])
st.multiselect("select language", ["java", "python", "c"])
st.radio("pick one", ["option A", "option B"])
st.checkbox("i agree terms & conditions")



if st.checkbox("show details"):
    st.text("here vare more details")

#form tag
with st.form("login form"):
    username = st.text_input("enter your username")
    password = st.text_input("enter your password", type="password")
    submitted = st.form_submit_button("login")
    if submitted:
        st.success(f"welcome {username}")



df = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B","C"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

st.video("https://youtu.be/XvMUH1pvY58?si=icErUFKYfUo9c9rb")
st.image("https://images.unsplash.com/photo-1682685790910-1e3f5c7b8d4e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8c2VhJTIwYmVhY2h8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60")