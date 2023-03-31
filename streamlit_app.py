import streamlit

streamlit.title('Moms Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Bacon & Eggs')
streamlit.text('Eggs Benedict')
streamlit.text('Spinach Omelet')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
