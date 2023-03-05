import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

plt.style.use("ggplot")

data = {
    "num" : [x for x in range(1,11)],
    "square" : [x**2 for x in range(1,11)],
    "twice": [x*2 for x in range(1,11)],
    "thrice" : [x*3 for x in range(1,11)]
}

rad = st.sidebar.radio("Navigation", ["Home", "About Us"])

if rad == "Home":

    df = pd.DataFrame(data = data)

    col = st.sidebar.multiselect("Select a column ", df.columns)

    plt.plot(df['num'], df[col])

    st.pyplot()

if rad == "About Us":
    st.write("you are in the About Us page")