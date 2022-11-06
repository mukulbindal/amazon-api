from unittest import result
from bs4 import BeautifulSoup

def parse(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    #results = soup.find_all(attrs={"data-component-type": "s-impression-counter"})
    #results = soup.find_all(attrs={"class": "s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border"})
    results = soup.find_all(attrs={"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-3"})
    
    print(results)
    return [r.parent.parent for r in results]
    

