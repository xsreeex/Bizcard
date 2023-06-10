!pip install streamlit
!pip install easyocr

import easyocr

import streamlit as st
import sqlite3
import easyocr
from PIL import Image
reader = easyocr.Reader(['en'], gpu = False)

import PIL
from PIL import ImageDraw

im = PIL.Image.open('/content/1.png')
im

im2 = PIL.Image.open('/content/2.png')
im2

im3 = PIL.Image.open('/content/3.png')
im3

im4 = PIL.Image.open('/content/4.png')
im4

im5 = PIL.Image.open('/content/5.png')
im5

bounds = reader.readtext('1.png')
bounds

bounds2 = reader.readtext('2.png')
bounds2

bounds3 = reader.readtext('3.png')
bounds3

bounds4 = reader.readtext('4.png')
bounds4

bounds5 = reader.readtext('5.png')
bounds5

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0,p1,p2,p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

draw_boxes(im, bounds)

draw_boxes(im2, bounds2)
draw_boxes(im3, bounds3)
draw_boxes(im4, bounds4)
draw_boxes(im5, bounds5)

len(bounds)

len(bounds2)

len(bounds3)

len(bounds4)

len(bounds5)

for i in bounds:
    print(i[1])

for i in bounds2:
    print(i[1])

for i in bounds3:
    print(i[1])

for i in bounds4:
    print(i[1])

for i in bounds5:
    print(i[1])

!pip install pandas

import pandas as pd
pd.DataFrame(bounds, columns = ['coordinates', 'words', 'confidence interval'])

pd.DataFrame(bounds2, columns = ['coordinates', 'words', 'confidence interval'])

pd.DataFrame(bounds3, columns = ['coordinates', 'words', 'confidence interval'])

pd.DataFrame(bounds4, columns = ['coordinates', 'words', 'confidence interval'])

pd.DataFrame(bounds5, columns = ['coordinates', 'words', 'confidence interval'])

import sqlite3

conn = sqlite3.connect('bussiness_card.db')

cur = conn.cursor()

# Create the table
cur = conn.cursor()
cur.execute('''CREATE TABLE business_cards
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                title TEXT,
                phone TEXT,
                email TEXT,
                website TEXT,
                company TEXT,
                address TEXT,
                city TEXT,
                state TEXT,
                zip TEXT,
                industry TEXT)''')

# Insert the data
cur.execute("INSERT INTO business_cards (name, title, phone, email, website, company, address, city, state, zip, industry) \
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Amitkumar', 'CEO & FOUNDER', '123-456-7569', 'hello@global.com', 'WWW global.com', '123 global', 'Erode',
             'GLOBAL', 'TamilNadu', '600115', 'INSURANCE'))

cur.execute("INSERT INTO business_cards (name, title, phone, email, website, company, address, city, state, zip, industry) \
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
            ('Selva', 'DATA MANAGER', '+123-456-7890', 'hello@XYZ1.com', 'WWW XYZI.com', '123 ABC St , Chennai', 'selva',
             'TamilNadu', '600113', 'digitals', ''))

cur.execute("INSERT INTO business_cards (name, title, phone, email, website, company, address, city, state, zip, industry) \
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('KARTHICK', 'General Manager', '+123-456-7890', 'hello@Borcelle.com', 'www Borcelle.com', 'BORCELLE', '123 ABC St',
             'Salem', 'TamilNadu', '6004513', 'AIRLINES'))

cur.execute("INSERT INTO business_cards (name, title, phone, email, website, company, address, city, state, zip, industry) \
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('REVANTH', 'Marketing Executive', '+91-456-1234', 'hello@CHRISTMAS.com', 'wWW.CHRISTMAS.com', 'Family', '123 ABC St',
             'HYDRABAD', 'TamilNadu', '600001', 'Restaurant'))

cur.execute("INSERT INTO business_cards (name, title, phone, email, website, company, address, city, state, zip, industry) \
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('SANTHOSH', 'Technical Manager', '+123-456-1234', 'hello@Sun.com', 'www.Suncom', 'Sun Electricals', '123 ABC St',
             'Tirupur', 'TamilNadu', '641603', 'Electricals'))

# Commit the changes
conn.commit()

# Close the connection
conn.close()


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





