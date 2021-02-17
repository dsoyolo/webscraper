from bs4 import BeautifulSoup
import requests

url = 'https://cbnorthbay.com/real-estate-properties/?addressmls=&status=For+sale&minprice=&maxprice=&minbed=&minbath=&property_type=&townvillages=North+Bay&structure_type=&waterfront=&listingssearch_submit=Search&df=1'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

print(content)