import time
import json
import requests
import colored
from colored import fg
import geocoder
import folium




red = fg('red')
purple = fg('dark_sea_green_1')
white = fg('white')
orange = fg('dark_orange')
lgreen = fg('light_green_2')
blue = fg('sky_blue_2')

#189.68.210.198


target_ip = input(red + "Target: ")
api = "http://ip-api.com/json/?fields=country,city,lat,lon,mobile,proxy,"

res = requests.get(api + target_ip)

data = res.json()

country = data["country"]
city = data["city"]
lat = data["lat"]
lon = data["lon"]
mobile = data["mobile"]
proxy = data["proxy"]


print(blue + "Country: ", purple + country)
print(blue + "City: ", purple + city)
print(blue + "Latitude: ", orange + str(lat))
print(blue + "Longitude: ", orange + str(lon))
if mobile == False:
    print(blue + "Mobile? ", red + "No")
else:
    print(blue + "Mobile? ", lgreen + "Yes")
    print(white)
if proxy == False:
    print(blue + "Proxy? ", red + "No")
else:
    print(blue + "Proxy? ", lgreen + "Yes")
print(white)


g = geocoder.ip(target_ip)

ip = g.latlng

map = folium.Map(location = ip, zoom_start = 150)

folium.Marker(ip, popup = "Taget's Location").add_to(map)


map.save("map.html")
