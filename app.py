import streamlit as st
st.header('Data of Iris')
import plotly.express as px
df = px.data.iris()
with st.expander('show data'):
    st.write(df)
st.subheader('Scatter plot')
with st.sidebar:
    option = st.selectbox('select xaxis',('sepal_length','sepal_width'))
    option2 = st.selectbox('select yaxis',('petal_length','petal_width'))
    option3 = st.selectbox('select histogram',('sepal_length','sepal_width','petal_length','petal_width'))

fig = px.scatter(df,x=option,y=option2)
st.plotly_chart(fig)
st.subheader('Histogram')
fig = px.histogram(df,x=option3)
st.plotly_chart(fig)

