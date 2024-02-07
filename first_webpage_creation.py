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

# Edrick's Delights log open file location section
img_edrick_logo = Image.open("images/edrickslogo.png")

# Adding subheader, title and descriptions
with st.container():
    left_column, right_column = st.columns(2)
    st.subheader("Hi there :wave:")
    st.title("Welcome to Edrick's Delights!")
    st.write("A home bakery where we make different kinds of pastries, breads, pasta and cakes, all baked with love!")
    st.write("[Learn More >](https://www.youtube.com/watch?v=xvFZjo5PgG0)")

# Describing what Edrick's Delights serve their customers
with st.container():
    st.write("---")
    text1_column, edrick_column = st.columns((1, 0.4))
    with text1_column:
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
    with edrick_column:
        st.image(img_edrick_logo)

# Adding a file to redesign the contact information section by using Local CSS
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}<harrystyles>", unsafe_allow_html=True)

local_css("harrystyles/style.css")

# Images open file location section
img_banana_loaf = Image.open("images/bananaloaf.png")

# Creating a section where it shows our products
with st.container():
    st.write("---")
    st.header("Our products")
    st.write("##")
    image_column, text2_column = st.columns((1, 2))

    # Image Column
    with image_column:
        st.image(img_banana_loaf)

        # Text Column
        with text2_column:
            st.header("Banana Loaf")
            st.write(
            """
            A delicious, tasteful and delightful pastry that has been our top seller since 2022, 
            the Banana Loaf is a unique delicacy on its own. With its flavorful texture in every
            bite, you will be hungry for more.
            """
            )
        st.markdown("")

# Contact information section
        st.write("---")
        st.header("Get in touch with us!")
        st.write("##")
        
        # Adding the contact information tabs
        contact_forms = """
        <form action="https://formsubmit.co/edward.borboran714@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Enter your name" required>
            <input type="email" name="email" placeholder="Enter your email" required>
            <textarea name="message" placeholder="Enter your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """

        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_forms, unsafe_allow_html=True)
        with right_column:
            st.empty()