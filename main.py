import streamlit as st
import plotly.express as px
import backend
import os

st.title('Weather Forecast for the next days')

cities_box_choice = st.text_input('Place:')
forecasted_days = st.slider(
    'Forecast Days', 1, 5, value=3, help='Select number of forecasted days')
data_selection = st.selectbox('Select data to view', ['Temperature', 'Sky'])


if cities_box_choice:
    try:
        filtered_data = backend.get_data(
            cities_box_choice, forecasted_days)
        st.subheader(
            f'{data_selection} for the next {forecasted_days} in {cities_box_choice}')
        if data_selection == 'Temperature':
            temperatures = [dict['main']['temp'] -
                            272.15 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={
                "x": "Date", "y": "Temperatures"})
            st.plotly_chart(figure)

        elif data_selection == 'Sky':
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main']
                              for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.error('City provided doesn\'t exist', icon="🚨")
