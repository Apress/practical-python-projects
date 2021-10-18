from urllib.request import urlopen

url="http://www.vulnweb.com"
page=urlopen(url)
html=page.read().decode("utf-8")

start_index=html.find("<title>") + len("<title>")
end_index=html.find("</title")

title=html[start_index:end_index]
print(title)


