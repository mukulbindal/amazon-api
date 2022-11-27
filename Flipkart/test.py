import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

#from utils.FilePropertyReader import get_property

def get_page(url):
    print("Fetching::" , url)
    session = HTMLSession()
    response = session.get(url)
    response.html.render(timeout = 30)
    if response.status_code==200:
        return response.text
    else:
        print("Error")

html_doc = get_page('https://www.flipkart.com/search?q=beard%20oil')
soup = BeautifulSoup(html_doc, 'html.parser')
results = soup.find_all(attrs={"class": "s1Q9rs"})

final_list = [r.parent.parent for r in results]
print(len(final_list))


        