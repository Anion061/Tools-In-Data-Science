from mimetypes import suffix_map
import streamlit as st
import os

PORT = os.environ["PORT"]

st.set_page_config(page_title = 'TDS GA', page_icon = ':wave:', layout = 'wide')

st.title('Odd or Even')

number = int(st.text_input('Enter the number'))

if number//2==0:
  st.write('The Number {number} is even'.format(number))
else:
  st.write('The Number {number} is odd'.format(number))
        
