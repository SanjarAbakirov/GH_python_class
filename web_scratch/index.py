from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphodite"

page = urlopen(url)  # urlopen() returns HTTP responce onject
