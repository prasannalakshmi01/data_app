import streamlit as st

st.header("Hello :red[everyone],")
st.subheader("I'am Prasannalakshmi")
st.subheader("Welcome to my :blue[app]")

option=st.button("click here to connect")
if option==True:
    st.balloons()

    linkedin="https://www.linkedin.com/in/prasannalakshmi-saili-7a0257246/"
    var1=st.write(format(linkedin))
    