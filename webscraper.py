from bs4 import BeautifulSoup
import requests

url = 'https://cbnorthbay.com/real-estate-properties/?addressmls=&status=For+sale&minprice=&maxprice=&minbed=&minbath=&property_type=&townvillages=North+Bay&structure_type=&waterfront=&listingssearch_submit=Search&df=1'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
print(content.prettify())

for property_item in content.findAll('h3', attrs={"class": "property_address"}):
    #print (f"Text: {property_item.a.text}")
    print (f"Title: {property_item.a.get('title')}")
    print (f"Link: {property_item.a.get('href')}\n")
