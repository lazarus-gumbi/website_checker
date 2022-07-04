import urllib.request   

website = input("website address:")

print(urllib.request.urlopen(str(website)).getcode())

