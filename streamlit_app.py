import streamlit

streamlit.title('Moms Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Bacon & Eggs')
streamlit.text('Eggs Benedict')
streamlit.text('Spinach Omelet')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(fruits_to_show)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index, ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')
