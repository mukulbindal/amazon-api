from amazon.GetPage import GetPage
from amazon.PageParser import parse

page = GetPage()
html = page.get_page()
result = parse(html)
#print(result)
print(len(result))

for parent in result:
    child_divs = parent.children
    for child in child_divs:
        print(child)
        print()
    break
