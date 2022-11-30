from mimetypes import suffix_map
import streamlit as st
import os


st.set_page_config(page_title = 'TDS GA', page_icon = ':wave:', layout = 'wide')

st.title('Odd or Even')

number = st.number_input("Enter the number",step=1)

if number%2==0:
  st.write("The Number ' {} ' is EVEN".format(number))
else:
  st.write("The Number ' {} ' is ODD".format(number))
        
