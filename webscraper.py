from bs4 import BeautifulSoup
import requests
import csv

# COLDWELL BANKER
# Grab properties from main page
url_parent = 'https://cbnorthbay.com/real-estate-properties/?addressmls=&status=For+sale&minprice=&maxprice=&minbed=&minbath=&property_type=&townvillages=North+Bay&structure_type=&waterfront=&listingssearch_submit=Search&df=1'
response_parent = requests.get(url_parent, timeout=5)
content_parent = BeautifulSoup(response_parent.content, "html.parser")
#print(content_parent.prettify())
# Loop through list and parse data
for properties_list in content_parent.findAll('h3', attrs={"class": "property_address"}):
    #print (f"Text: {properties_list.a.text}")
    property_title = properties_list.a.get('title')
    print (f"Title: {property_title}")
    property_link = properties_list.a.get('href')
    print (f"Link: {property_link}")
    # Grab each link and output content
    url_child = property_link
    response_child = requests.get(url_child, timeout=5)
    content_child = BeautifulSoup(response_child.content, "html.parser")
    #print(content_child.prettify())
    # Parse details
    # Price
    property_price_raw = content_child.find('h4', attrs={"class": "property_price"}).text
    property_price = property_price_raw.split(' - ')[0]
    print (f"Price: {property_price}")
    # Description
    property_description = content_child.find('p', attrs={"class": "prop_description"}).text
    print (f"Description: {property_description}")
    # Loop over unordered list for property details
    property_details_section = content_child.find('div', id='properties_details')
    for property_details in property_details_section.find_next('ul').find_all('li'):
        property_details_raw = property_details.find_next('li').text.split(':')
        print (f"{property_details_raw[0]}: {property_details_raw[1]}")
    # Output to CSV
    with open('output/property_data_coldwellbanker.csv', 'w') as property_file:
        property_writer = csv.writer(property_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Write headers
        property_writer.writerow(['TITLE', 'LINK', 'PRICE', 'DESCRIPTION'])
        # Write rows
        property_writer.writerow([property_title, property_link, property_price, property_description])
    # Break for testing/limit one loop iteration
    break