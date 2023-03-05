import streamlit as st

st.title("WIDGETS")

if st.button("Subscribe"):
    st.write("Like this video too")

name  = st.text_input("Name")
st.write(name)

address = st.text_area("Enter your address")
st.write(address)

st.date_input("enter a date")

st.time_input("enter a time")

if st.checkbox("you accept the T&C",value = False):
    st.write("Thank you")

st.radio("Colors",["r", "g", "b"], index = 1)

st.selectbox("Colors",["r", "g", "b"], index = 1)

v3 = st.multiselect("Colors", ["r","g", "b"])
st.write(v3)

st.slider("age", min_value=18, max_value=80, value=30, step=2)