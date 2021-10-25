"""
from geopy.geocoders import Nominatim
from geopy.geocoders import ArcGIS
nom = ArcGIS(timeout=300)
#initialize the Nominatim object
Nomi_locator = Nominatim(user_agent="My App")

address= "Delhi Connaught Place"

#get the location detail 
location = Nomi_locator.geocode(address)

print("You find for the location:", location)
print(f"The Latitude of {location} is: <{location.latitude}>")
print(f"The Longitude of {location} is: <{location.longitude}>")

"""



from opencage.geocoder import OpenCageGeocode

key = 'd908ec2a841244e0892ac9b12db8a453'
geocoder = OpenCageGeocode(key)

query = u'1A2B Minto Road, Allahabad'
results = geocoder.geocode(query)

print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))

results2 = geocoder.reverse_geocode(25.448940,81.833290)
print(results2)
