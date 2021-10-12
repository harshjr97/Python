import pyshorteners

s = pyshorteners.Shortener()
url = input("enter your URL : ")
print(s.tinyurl.short(url))
