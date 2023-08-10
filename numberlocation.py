import phonenumbers
import folium
from phonenumbers import geocoder
from mynumber import number


key = "ff523731a74c42009dfa44ebdadc4cab"
sanNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(sanNumber, "en")
print(yourLocation)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location= [lat, lng], zoom_start = 9)
folium.Marker([lat, lng],popup= yourLocation).add_to((myMap))

myMap.save("mylocation.html")