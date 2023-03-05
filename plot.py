import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns = ['a','b','c']
)

st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe
share -> watch
}
""")


chart = alt.Chart(data).mark_circle().encode(
    x = 'a' , y= 'b', tooltip = ['a','b']
)

city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})

st.map(city)

st.altair_chart(chart)
st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

plt.scatter(data['a'], data['b'])
plt.title('Scatter')

st.pyplot()