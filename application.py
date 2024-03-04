import streamlit as st
from streamlit_option_menu import option_menu
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import openpyxl
# wide layout  by defult
st.set_page_config(layout="wide")
# Function to scrape <span> elements
def scrape_span(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        spans = soup.find_all("span")
        return [span.text.strip() for span in spans]
    else:
        return "Failed to retrieve the webpage."

# Function to scrape <strong> elements
def scrape_strong(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        strongs = soup.find_all("strong")
        return [strong.text.strip() for strong in strongs]
    else:
        return "Failed to retrieve the webpage."

# Function to scrape <td> elements
def scrape_td(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        tds = soup.find_all("td")
        return [td.text.strip() for td in tds]
    else:
        return "Failed to retrieve the webpage."

# Function to scrape <h3> elements
def scrape_h3(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        h3s = soup.find_all("h3")
        return [h3.text.strip() for h3 in h3s]
    else:
        return "Failed to retrieve the webpage."

# Function to scrape <div class> elements
def scrape_div(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        divs = soup.find_all("div", class_="your-class-name")
        return [div.text.strip() for div in divs]
    else:
        return "Failed to retrieve the webpage."

# Function to scrape <a> elements
def scrape_href(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        hrefs = soup.find_all("a")
        return [a.get("href") for a in hrefs]
    else:
        return "Failed to retrieve the webpage."

# Define a Streamlit app
def main():
    st.title("Web Scraping Project")
    
    # User inputs for name and surname
    champ1 = st.text_input("Entrez le premier champ:")
    champ2 = st.text_input("Entrez le deuxième champ:")
    search_term = f"{champ1}.{champ2}@uit.ac.ma"

    # Button to trigger the search
    if st.button("Search"):
        # URLs to scrape
        urls = {
            "https://fs.uit.ac.ma/biologie/": scrape_span,
            "https://fs.uit.ac.ma/chimie/": scrape_span,
            "https://fs.uit.ac.ma/geologie/": scrape_span,
            "https://fs.uit.ac.ma/informatique/": scrape_span,
            "https://fs.uit.ac.ma/mathematiques/": scrape_span,
            "https://fs.uit.ac.ma/physique/": scrape_span,
            "https://fsjp.uit.ac.ma/personnel-enseignants/": scrape_strong,
            "https://est.uit.ac.ma/corps-enseignants/": scrape_td,
            "https://encg.uit.ac.ma/corps-enseignant/": scrape_td,
            "https://feg.uit.ac.ma/corps-professoral/": scrape_h3,
            "https://esef.uit.ac.ma/?page_id=774": scrape_div,
            "https://ensa.uit.ac.ma/ensa/departements/": scrape_href,
        }

        # Create a DataFrame to store the scraped data
        scraped_data = {'URL': [], 'Data': []}

        # Iterate over URLs and scrape elements
        for url, scraper_function in urls.items():
            data = scraper_function(url)
            if isinstance(data, list):
                for item in data:
                    scraped_data['URL'].append(url)
                    scraped_data['Data'].append(item)

        # Convert the scraped data into a DataFrame
        df = pd.DataFrame(scraped_data)

        # Display the scraped data
        st.write("Scraped Data:")
        st.write(df)

        # Search for data based on name and surname
        result = df.loc[df['Data'] == search_term]

        # Display the search result
        st.write("Search Result:")
        st.write(result)

# Display images on the left and right top corners
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.image("logo.png", width=150)
with col3:
    st.image("logo2.png", width=250)  

     
# Define the options for the menu
menu_options = ["Home", "Projects", "Contact"]
menu_icons = ["house", "book", "envelope"]

# Display the menu as a top bar
selected = option_menu(
    menu_title=None,  # No title for the menu
    options=menu_options,  # Menu options
    icons=menu_icons,  # Icons for menu options
    menu_icon="menu",  # Icon for the menu button
    default_index=1,  # Default selected index (Projects)
    orientation="horizontal",  # Display menu horizontally
)

# Display content based on the selected menu option
if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    main()
if selected == "Contact":
    st.title(f"You have selected {selected}")

# Footer
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
st.markdown(footer, unsafe_allow_html=True)
