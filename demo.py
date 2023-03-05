import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello Streamlit")

st.header("Header")

st.subheader("Subheader")

st.text("Subscribe to my channel and please like my video")

st.markdown(""" # h1 tag
## h2 tag
### h3 tag
:moon:<br>
:sunglasses:

""" ,True)

a = [1,2,3,4,5,6,7,8]
arr = np.array(a)

nd = arr.reshape(2,4)

dic = {
    'name': 'Vivek Sharma',

    'age' : 29,
    'city': 'London'
}

st.dataframe(nd)
st.dataframe(dic, width=100, height=100)

st.table(dic)
st.write(dic)