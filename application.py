import streamlit as st
from streamlit_option_menu import option_menu

# Display images on the left and right top corners
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.image("logo.png", width=150)
with col3:
    st.image("logo.png", width=250)  

     
# Define the options for the menu
menu_options = ["Home", "Projects", "Contact"]
menu_icons = ["house", "book", "envelope"]

# Display the menu as a top bar
selected = option_menu(
    menu_title=None,  # No title for the menu
    options=menu_options,  # Menu options
    icons=menu_icons,  # Icons for menu options
    menu_icon="menu",  # Icon for the menu button
    default_index=0,  # Default selected index
    orientation="horizontal",  # Display menu horizontally
)

# Display content based on the selected menu option
if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")








#footer
footer = """
<style>
.footer {
    background-color: #4B64FF;
    color: #ffffff;
    text-align: center;
    padding: 20px 0;
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
}
</style>

<div class="footer">
    <p>This is the footer of the Streamlit app.</p>
    <p>Feel free to customize the design!</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
