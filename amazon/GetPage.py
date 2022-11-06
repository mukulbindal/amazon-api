import requests
from requests_html import HTMLSession

from utils.FilePropertyReader import get_property

class GetPage:
    def __init__(self, url=get_property("AMAZON_URL"), key="") -> None:
        self.url = url + "s?k=beard+oil"
    
    def get_page(self):
        print("Fetching::" , self.url)
        session = HTMLSession()
        self.response = session.get(self.url)
        self.response.html.render()
        if self.response.status_code==200:
            return self.response.text
        else:
            raise Exception(self.response.headers['status'])
        
    
        
        