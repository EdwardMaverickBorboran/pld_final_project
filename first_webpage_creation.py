# So I looked up python projects at Youtube that I might work on and saw this channel called "Coding Is Fun".
# There are several videos, tutorials, and tips & techniques available for any newbie to learn from. I then
# remembered that I wanted to make a webpage for our home business, and I thought that this would be a good
# opportunity for me to try learning how to do build one as a beginner in this field.

# DEADLINE: FEB. 10, 2024!!!

# psuedocode

from PIL import Image
import streamlit as st

# Setting the title page for the webpage
st.set_page_config(page_title="Edrick's Delights", page_icon=":shortcake:", layout="wide")

# Adding subheader, title and descriptions
with st.container():
    st.subheader("Hi there :wave:")
    st.title("Welcome to Edrick's Delights!")
    st.write("A home bakery where we make different kinds of pastries, breads, pasta and cakes, all baked with love!")
    st.write("[Learn More >](https://www.youtube.com/watch?v=haf67eKF0uo)")

# Describing what Edrick's Delights serve their customers
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we serve to please our customers:")
        st.write("##")
        st.write(
            """
            On our business, we service our customers who are:
            - blah
            - blah
            - blah
            - blah
            - blah
            - blah
            """
        )
        st.write("[Facebook Page >](https://www.facebook.com/edricksdelights)")

# Images file location and open them
img_banana_loaf = Image.open("images/bananaloaf.png")

with st.container():
    st.write("---")
    st.header("Our products")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_banana_loaf)
        with text_column:
            st.header("Banana Loaf")
            st.write(
            """
            A delicious, tasteful and delightful pastry that has been our top seller since 2022, 
            the Banana Loaf is a unique delicacy on its own. With its flavorful texture in every
            bite, you will be hungry for more.
            """
            )
        st.markdown("")