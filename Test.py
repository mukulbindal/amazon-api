from amazon.GetPage import GetPage
from amazon.PageParser import parse

page = GetPage()
html = page.get_page()
result = parse(html)
#print(result)
print(len(result))

for parent in result:
    child_divs = list(parent.children)
    heading_div = child_divs[0]
    print(heading_div.get_text())
    heading_div = child_divs[1]
    print(heading_div.get_text())
    heading_div = child_divs[2]
    print(heading_div.get_text())
    break
