import streamlit
import pandas

streamlit.title('this is first streamlit')

streamlit.header('this is the menu')
streamlit.text('add different texts')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
