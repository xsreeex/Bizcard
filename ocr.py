import streamlit as st
import sqlite3
import easyocr
from PIL import Image

# Create a connection to the SQLite database
conn = sqlite3.connect('business_card.db')
c = conn.cursor()

# Create a table to store the business card information
c.execute('CREATE TABLE IF NOT EXISTS business_cards (id INTEGER PRIMARY KEY, image BLOB, company_name TEXT, card_holder_name TEXT, designation TEXT, mobile_number TEXT, email_address TEXT, website_url TEXT, area TEXT, city TEXT, state TEXT, pin_code TEXT)')

# Create an instance of the OCR reader
reader = easyocr.Reader(['en'])

# Define a function to extract information from a business card image
def extract_info(image):
    results = reader.readtext(image)
    info = {}
    for result in results:
        if 'company' in result[1].lower():
            info['company_name'] = result[0]
        elif 'name' in result[1].lower():
            info['card_holder_name'] = result[0]
        elif 'designation' in result[1].lower():
            info['designation'] = result[0]
        elif 'mobile' in result[1].lower():
            info['mobile_number'] = result[0]
        elif 'email' in result[1].lower():
            info['email_address'] = result[0]
        elif 'website' in result[1].lower():
            info['website_url'] = result[0]
        elif 'area' in result[1].lower():
            info['area'] = result[0]
        elif 'city' in result[1].lower():
            info['city'] = result[0]
        elif 'state' in result[1].lower():
            info['state'] = result[0]
        elif 'pin' in result[1].lower():
            info['pin_code'] = result[0]
    return info

# Define the Streamlit application
def app():
    st.title("Business Card Reader")

    # Define the sidebar
    st.sidebar.title("Actions")
    action = st.sidebar.selectbox("Select an action", ["Upload a business card", "View saved business cards"])

    # Define the main content area
    if action == "Upload a business card":
        st.header("Upload a business card")
        uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            if st.button("Extract Information"):
                info = extract_info(image)
                st.write("## Extracted Information")
                for key, value in info.items():
                    st.write(f"**{key}:** {value}")
                if st.button("Save Information"):
                    # Save the extracted information to the database
                    image_bytes = uploaded_file.read()
                    c.execute('INSERT INTO business_cards (image, company_name, card_holder_name, designation, mobile_number, email_address, website_url, area, city, state, pin_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (image_bytes, info.get('company_name'), info.get('card_holder_name'), info.get('designation'), info.get('mobile_number'), info.get('email_address'), info.get('website_url'), info.get('area'), info.get('city'), info.get('state'), info.get('pin_code')))
                    conn.commit()




