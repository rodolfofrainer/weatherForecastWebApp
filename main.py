import streamlit as st

st.title('Weather Forecast for the next days')

cities_box_choice = st.selectbox('Place:', ['Dublin', 'Limerick'])
forecasted_days = st.slider(
    'Forecast Days', 1, 5, value=3, help='Select number of forecasted days')
data_selection = st.selectbox('Select data to view', ['Temperature', 'Sky'])
st.subheader(
    f'{data_selection} for the next {forecasted_days} in {cities_box_choice}')
