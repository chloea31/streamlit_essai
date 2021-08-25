#! /usr/bin/python3
#-*-coding: utf-8-*-

import streamlit as st
import numpy as np
import pandas as pd 
import time

# add a title
st.title('My first app')

# write a dataframe
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


# draw charts and maps

## draw a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.line_chart(chart_data)

## plot a map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)


# add interactivity with widgets

## use checkboxes to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    chart_data

## use a selectbox for options
df = pd.DataFrame({
    'first column':[1, 2, 3, 4],
    'second column':[10, 20, 30, 40]
})
df

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected: ', option


# Lay out your app

option_bis = st.sidebar.selectbox(
    'Which other number do you like best?',
    df['first column']
)
'You selected: ', option_bis

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


# show progress
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'and now we\'re done!'

# share your app
