# So I looked up python projects at Youtube that I might work on and saw this channel called "Coding Is Fun".
# There are several videos, tutorials, and tips & techniques available for any newbie to learn from. I then
# remembered that I wanted to make a webpage for our home business, and I thought that this would be a good
# opportunity for me to try learning how to do build one as a beginner in this field.

# DEADLINE: FEB. 10, 2024!!!

# psuedocode

import streamlit as st

# Setting the title page for the webpage
st.set_page_config(page_title="Edrick's Delights", page_icon=":shortcake:", layout="wide")

# Adding subheader, title and descriptions
with st.container():
    st.subheader("Hi there :wave:")
    st.title("Welcome to Edrick's Delights!")
    st.write("A home bakery where we make different kinds of pastries, breads, pasta and cakes, all baked with love!")
    st.write("[Learn More >](https://www.youtube.com/watch?v=haf67eKF0uo)")