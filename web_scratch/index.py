from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphodite"

page = urlopen(url)  # urlopen() returns HTTP responce onject

# page < http.client.HTTPResponse object at 0x150fef820 >

html_bytes = page.read()  # returns a sequence bytes
html = html_bytes.decode("utf-8")  # convert to the str format
