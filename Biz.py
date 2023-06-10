!pip install streamlit
!pip install easyocr

import easyocr

reader = easyocr.Reader(['en'], gpu = False)

import PIL
from PIL import ImageDraw

im = PIL.Image.open('/content/drive/MyDrive/1.png')
im

im2 = PIL.Image.open('/content/drive/MyDrive/2.png')
im2

im3 = PIL.Image.open('/content/drive/MyDrive/3.png')
im3

im4 = PIL.Image.open('/content/drive/MyDrive/4.png')
im4

im5 = PIL.Image.open('/content/drive/MyDrive/5.png')
im5

bounds = reader.readtext('drive/MyDrive/1.png')
bounds

bounds2 = reader.readtext('drive/MyDrive/2.png')
bounds2

bounds3 = reader.readtext('drive/MyDrive/3.png')
bounds3

bounds4 = reader.readtext('drive/MyDrive/4.png')
bounds4

bounds5 = reader.readtext('drive/MyDrive/5.png')
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
