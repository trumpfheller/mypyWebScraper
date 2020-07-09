from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

match = html.find('title')
print(match)
#1print(match[0])
#1OUTPUT: <Element 'title'>

#2print(match[0].html)
#2OUTPUT: <title>Test - A sample website</title>

#3print(match[0].text)
#3OUTPUT: Test - A sample website

#4 match = html.find('title', first=True)
#4 print(match.text)
#4 Output   Test - A sample website