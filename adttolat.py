from opencage.geocoder import OpenCageGeocode
import os
import haversine as hs
from haversine import Unit

key = 'd908ec2a841244e0892ac9b12db8a453'


geocoder = OpenCageGeocode(key)

query = u'1A/2B,Minto Road,Allahabad'

query2= u'2A/BC,Minto Road,Allahabad'
results = geocoder.geocode(query)
results2 = geocoder.geocode(query2)
print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))


x=results[0]['geometry']['lat'], results[0]['geometry']['lng']
y=results2[0]['geometry']['lat'],results2[0]['geometry']['lng'], 

print(u'%f;%f;%s;%s' % (results2[0]['geometry']['lat'], 
                        results2[0]['geometry']['lng'],
                        results2[0]['components']['country_code'],
                        results2[0]['annotations']['timezone']['name']))



print(hs.haversine(x,y))
print(hs.haversine(x,y,unit=Unit.METERS))

##results2 = geocoder.reverse_geocode(25.448940,81.833290)
#print(results2)