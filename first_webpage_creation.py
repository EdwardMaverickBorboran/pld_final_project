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
    text_column, edrick_column = st.columns((1, 0.25))

    # Text Column for the short intro
    with text_column:
        st.subheader("Hi there :wave:")
        st.title("Welcome to Edrick's Delights!")
        st.write("A home bakery where we make different kinds of pastries, breads, pasta and cakes, all baked with love!")
        st.write("[Learn More >](https://www.youtube.com/watch?v=xvFZjo5PgG0)")

    # Image column for the logo
    with edrick_column:
        st.image(img_edrick_logo)

# Describing what Edrick's Delights serve their customers
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("We are happy to serve!")
        st.write("##")
        st.write(
            """
            We always do our best to please our customers satisfaction:
            - The products can be based on your own preference of taste. e.g. sugar level
            - The products that you ordered will be the same as you expected.
            - We make sure our products are made in excellent quality.
            - We do door to door delivery or let us book you a delivery rider.
            - We assure you that our products are FDA approved.
            - Our service will be in its greatest shape until the end.

            You can follow our fb page down below and contact us if you have an order in mind.
            """
        )
        st.write("[Facebook Page >](https://www.facebook.com/edricksdelights)")

# Adding a file to redesign the contact information section by using Local CSS
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}<harrystyles>", unsafe_allow_html=True)

local_css("harrystyles/style.css")

# Product images open file location section
img_banana_loaf = Image.open("images/bananaloaf.png")
img_cookies = Image.open("images/cookies.png")
img_revel_bars = Image.open("images/revelbars.png")
img_brownies = Image.open("images/brownies.png")
img_cinnamon_roll = Image.open("images/cinnamonroll.png")

# Creating a section where it shows our products
with st.container():
    st.write("---")
    st.header("Our products")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

# Banana Loaf section
    # Image Column
    with image_column:
        st.image(img_banana_loaf)

        # Text Column
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

# Cookies section
with st.container():
    image_column, text_column = st.columns((1, 2))

    # Image Column
    with image_column:
        st.image(img_cookies)

        # Text Column
        with text_column:
            st.header("Cookies")
            st.write(
            """
            Cookies, one of the most famous delights in the whole world. A go to snack by everyone
            and it still would be a one of a kind goodies to devour. You can never ever forget the
            snack that you and your friends shared with during your school days as you take a break
            before classes starts again.
            """
            )
        st.markdown("")

# Revel Bars section
with st.container():
    image_column, text_column = st.columns((1, 2))

    # Image Column
    with image_column:
        st.image(img_revel_bars)

        # Text Column
        with text_column:
            st.header("Revel Bars")
            st.write(
            """
            You might be wondering what a Revel Bar is. It is simple a brownie but with a touch of
            outmeal on the top. It is an all arounder bites, it can be your protein snack for whenever
            you hit the gym, your short meal when you are driving or just casually enjoy your alone time.
            """
            )
        st.markdown("")

# Brownies section
with st.container():
    image_column, text_column = st.columns((1, 2))

    # Image Column
    with image_column:
        st.image(img_brownies)

        # Text Column
        with text_column:
            st.header("Brownies")
            st.write(
            """
            Brownies, a chocolaty baked delights that are made in square shapes. It may be a common
            delight for everybody, but deep down everybody loves to have a bite of its deliciousness.
            A reminder, just don't smile right after you eat one :)).
            """
            )
        st.markdown("")

# Cinnamon Rolls section
with st.container():
    image_column, text_column = st.columns((1, 2))

    # Image Column
    with image_column:
        st.image(img_cinnamon_roll)

        # Text Column
        with text_column:
            st.header("Cinnamon Rolls")
            st.write(
            """
            You may have ordered it on Starbucks but you probably have never tried our version. The 
            Cinnamon Roll is one of the best choice of food whenever you lay down on your sunday 
            afternoon along with a hot cup of coffee in your hand. Its rich of flavor lets you have
            the best time to relax.
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