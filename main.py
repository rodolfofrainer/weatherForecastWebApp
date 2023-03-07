import streamlit as st
import plotly.express as px
import backend
import os

st.title('Weather Forecast for the next days')

cities_box_choice = st.selectbox('Place:', ['Dublin', 'Limerick'])
forecasted_days = st.slider(
    'Forecast Days', 1, 5, value=3, help='Select number of forecasted days')
data_selection = st.selectbox('Select data to view', ['Temperature', 'Sky'])
st.subheader(
    f'{data_selection} for the next {forecasted_days} in {cities_box_choice}')


days_quantity, temp = backend.get_data(
    cities_box_choice, forecasted_days, data_selection)
figure = px.line(x=days_quantity, y=temp, labels={
                 "x": "Date", "y": "Temperatures"})

st.plotly_chart(figure)
