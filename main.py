import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the next days')

cities_box_choice = st.selectbox('Place:', ['Dublin', 'Limerick'])
forecasted_days = st.slider(
    'Forecast Days', 1, 5, value=3, help='Select number of forecasted days')
data_selection = st.selectbox('Select data to view', ['Temperature', 'Sky'])
st.subheader(
    f'{data_selection} for the next {forecasted_days} in {cities_box_choice}')


def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [forecasted_days * i for i in temperatures]
    return dates, temperatures


days_quantity, temp = get_data(forecasted_days)
figure = px.line(x=days_quantity, y=temp, labels={
                 "x": "Date", "y": "Temperatures"})

st.plotly_chart(figure)
