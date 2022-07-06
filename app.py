import urllib.request   

website = input("https://")

#Check if the url works

print(urllib.request.urlopen(f'https://{website}').getcode())

