from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphodite"

page = urlopen(url)  # urlopen() returns HTTP responce onject

# page < hsttp.client.HTTPResponse object at 0x150fef820 >

html_bytes = page.read()  # returns a sequence bytes
html = html_bytes.decode("utf-8")  # convert to the str format

print(html)
html = """
<html>
<head>ss
<title> Profile: Aphrodite </title >
</head>
<body bgcolor = "yellow">
<center>
<br><br>
Favorite animal: Dove
<br><br>
Favorite color: Red
<br><br>
Hometown: Mount Olympus
</center>
</body>
</html>
"""
title_index = html.find("<title>")
title_index

start_index = title_index + len("<title>")
start_index

end_index = html.find("</title>")
end_index

title = html[start_index:end_index]
title
