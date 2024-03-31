import phonenumbers
import opencage
import folium
import myphone  # Import the entire module

from phonenumbers import geocoder

# Access the variable from myphone module
pepnumber = phonenumbers.parse(myphone.number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
# Access the variable from myphone module
service_pro = phonenumbers.parse(myphone.number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key = "your_key"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat,lng], zoom_start = 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
