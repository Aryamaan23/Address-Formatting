from fastapi import FastAPI
import requests
from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError
from geopy.geocoders import Nominatim
from pydantic import BaseModel
from urllib.request import urlopen
import json
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import googletrans
from googletrans import Translator
app = FastAPI()
geolocator = Nominatim(user_agent="geoapiExercises")

key = 'd908ec2a841244e0892ac9b12db8a453'
geocoder = OpenCageGeocode(key)


translator=Translator()

 
@app.get("/")
def first_example():
    return {"Corrected Address": "Hello World!"}



@app.post("/addressformatter/")
async def addressformatterlanguage(address: str):
    list=address.split(',')
    joined_string = ",".join(list[0:2])
    print(list)
    print(joined_string)
    first_component_addr=list[0]
    second_component_addr=list[1]
    third_component_addr=list[2]
    print(first_component_addr)
    print(second_component_addr)
    print(third_component_addr)
    results = geocoder.geocode(address)
    latitude=results[0]['geometry']['lat']
    longitude=results[0]['geometry']['lng']
    #print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        #results[0]['geometry']['lng'],
                        #results[0]['components']['country_code']))
    
    location = geolocator.reverse(str(latitude)+","+str(longitude))
    print(location)
    address = location.raw['address']
    print(address)
    
    try:
        results = geocoder.reverse_geocode(latitude, longitude, language='en', no_annotations='1')
        print(results)
        if results and len(results):
           res=results[0]['formatted'].replace("unnamed road",joined_string)
           return {"Formatted address": res,"address": address}
    except RateLimitExceededError as ex:
           print(ex)






    


@app.post("/addressformatterregionallanguages/")
async def addressformatter(text: str):
    y=translator.detect(text)
    address2= translator.translate(text,src=y.lang,dest= "en")
    xa=address2.text
    print(xa)
    list=xa.split(',')
    joined_string = ",".join(list[0:2])
    print(list)
    print(joined_string)
    first_component_addr=list[0]
    second_component_addr=list[1]
    third_component_addr=list[2]
    print(first_component_addr)
    print(second_component_addr)
    print(third_component_addr)


    
    print(xa.split(','))
    results = geocoder.geocode(xa)
    latitude=results[0]['geometry']['lat']
    longitude=results[0]['geometry']['lng']
    #print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        #results[0]['geometry']['lng'],
                        #results[0]['components']['country_code']))
    
    location = geolocator.reverse(str(latitude)+","+str(longitude))
    print(location)
    xa= location.raw['address']
    print(xa)
    
    #try:
    results = geocoder.reverse_geocode(latitude, longitude, language='en', no_annotations='1')
    print(results)
    #x= translator.translate(results[0]['formatted'],src='en',dest=y.lang)
    if(y.lang=="hi"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.DEVANAGARI)

        #y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.DEVANAGARI)
        #z=transliterate(xa['road'], sanscript.ITRANS, sanscript.DEVANAGARI)
        a=transliterate(xa['neighbourhood'], sanscript.ITRANS, sanscript.DEVANAGARI)
        b=transliterate(xa['suburb'], sanscript.ITRANS, sanscript.DEVANAGARI)
        c=transliterate(xa['city_district'], sanscript.ITRANS, sanscript.DEVANAGARI)
        d=transliterate(xa['city'], sanscript.ITRANS, sanscript.DEVANAGARI)
        e=transliterate(xa['county'], sanscript.ITRANS, sanscript.DEVANAGARI)
        f=transliterate(xa['state_district'], sanscript.ITRANS, sanscript.DEVANAGARI)
        g=transliterate(xa['state'], sanscript.ITRANS, sanscript.DEVANAGARI)
        h=transliterate(xa['postcode'], sanscript.ITRANS, sanscript.DEVANAGARI)
        i=transliterate(xa['country'], sanscript.ITRANS, sanscript.DEVANAGARI)
        j=transliterate(xa['country_code'], sanscript.ITRANS, sanscript.DEVANAGARI)

        final_updated={"address": {
            #"amenity": y,
            #"road": z,
            "neighbourhood": a,
            "suburb": b,
            "city_district": c,
            "city": d,
            "county": e,
            "state_district": f,
            "state": g,
            "postcode": h,
            "country": i,
            "country_id": j
        }
    }


    elif(y.lang=="gu"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.GUJARATI)

        #y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.GUJARATI)
        #z=transliterate(xa['road'], sanscript.ITRANS, sanscript.GUJARATI)
        a=transliterate(xa['neighbourhood'], sanscript.ITRANS, sanscript.GUJARATI)
        b=transliterate(xa['suburb'], sanscript.ITRANS, sanscript.GUJARATI)
        c=transliterate(xa['city_district'], sanscript.ITRANS, sanscript.GUJARATI)
        d=transliterate(xa['city'], sanscript.ITRANS, sanscript.GUJARATI)
        e=transliterate(xa['county'], sanscript.ITRANS, sanscript.GUJARATI)
        f=transliterate(xa['state_district'], sanscript.ITRANS, sanscript.GUJARATI)
        g=transliterate(xa['state'], sanscript.ITRANS, sanscript.GUJARATI)
        h=transliterate(xa['postcode'], sanscript.ITRANS, sanscript.GUJARATI)
        i=transliterate(xa['country'], sanscript.ITRANS, sanscript.GUJARATI)
        j=transliterate(xa['country_code'], sanscript.ITRANS, sanscript.GUJARATI)

        final_updated={"address": {
            #"amenity": y,
            #"road": z,
            "neighbourhood": a,
            "suburb": b,
            "city_district": c,
            "city": d,
            "county": e,
            "state_district": f,
            "state": g,
            "postcode": h,
            "country": i,
            "country_id": j
        }
    }


    elif(y.lang=="bn"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.BENGALI)

        #y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.BENGALI)
        #z=transliterate(xa['road'], sanscript.ITRANS, sanscript.BENGALI)
        a=transliterate(xa['neighbourhood'], sanscript.ITRANS, sanscript.BENGALI)
        b=transliterate(xa['suburb'], sanscript.ITRANS, sanscript.BENGALI)
        c=transliterate(xa['city_district'], sanscript.ITRANS, sanscript.BENGALI)
        d=transliterate(xa['city'], sanscript.ITRANS, sanscript.BENGALI)
        e=transliterate(xa['county'], sanscript.ITRANS, sanscript.BENGALI)
        f=transliterate(xa['state_district'], sanscript.ITRANS, sanscript.BENGALI)
        g=transliterate(xa['state'], sanscript.ITRANS, sanscript.BENGALI)
        h=transliterate(xa['postcode'], sanscript.ITRANS, sanscript.BENGALI)
        i=transliterate(xa['country'], sanscript.ITRANS, sanscript.BENGALI)
        j=transliterate(xa['country_code'], sanscript.ITRANS, sanscript.BENGALI)

        final_updated={"address": {
            #"amenity": y,
            #"road": z,
            "neighbourhood": a,
            "suburb": b,
            "city_district": c,
            "city": d,
            "county": e,
            "state_district": f,
            "state": g,
            "postcode": h,
            "country": i,
            "country_id": j
        }
    }

    elif(y.lang=="bn"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.BENGALI)

        #y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.BENGALI)
        #z=transliterate(xa['road'], sanscript.ITRANS, sanscript.BENGALI)
        a=transliterate(xa['neighbourhood'], sanscript.ITRANS, sanscript.BENGALI)
        b=transliterate(xa['suburb'], sanscript.ITRANS, sanscript.BENGALI)
        c=transliterate(xa['city_district'], sanscript.ITRANS, sanscript.BENGALI)
        d=transliterate(xa['city'], sanscript.ITRANS, sanscript.BENGALI)
        e=transliterate(xa['county'], sanscript.ITRANS, sanscript.BENGALI)
        f=transliterate(xa['state_district'], sanscript.ITRANS, sanscript.BENGALI)
        g=transliterate(xa['state'], sanscript.ITRANS, sanscript.BENGALI)
        h=transliterate(xa['postcode'], sanscript.ITRANS, sanscript.BENGALI)
        i=transliterate(xa['country'], sanscript.ITRANS, sanscript.BENGALI)
        j=transliterate(xa['country_code'], sanscript.ITRANS, sanscript.BENGALI)

        final_updated={"address": {
            #"amenity": y,
            #"road": z,
            "neighbourhood": a,
            "suburb": b,
            "city_district": c,
            "city": d,
            "county": e,
            "state_district": f,
            "state": g,
            "postcode": h,
            "country": i,
            "country_id": j
        }
    }


    elif(y.lang=="kn"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.KANNADA)

        #y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.KANNADA)
        #z=transliterate(xa['road'], sanscript.ITRANS, sanscript.KANNADA)
        a=transliterate(xa['neighbourhood'], sanscript.ITRANS, sanscript.KANNADA)
        b=transliterate(xa['suburb'], sanscript.ITRANS, sanscript.KANNADA)
        c=transliterate(xa['city_district'], sanscript.ITRANS, sanscript.KANNADA)
        d=transliterate(xa['city'], sanscript.ITRANS, sanscript.KANNADA)
        e=transliterate(xa['county'], sanscript.ITRANS, sanscript.KANNADA)
        f=transliterate(xa['state_district'], sanscript.ITRANS, sanscript.KANNADA)
        g=transliterate(xa['state'], sanscript.ITRANS, sanscript.KANNADA)
        h=transliterate(xa['postcode'], sanscript.ITRANS, sanscript.KANNADA)
        i=transliterate(xa['country'], sanscript.ITRANS, sanscript.KANNADA)
        j=transliterate(xa['country_code'], sanscript.ITRANS, sanscript.KANNADA)

        final_updated={"address": {
            #"amenity": y,
            #"road": z,
            "neighbourhood": a,
            "suburb": b,
            "city_district": c,
            "city": d,
            "county": e,
            "state_district": f,
            "state": g,
            "postcode": h,
            "country": i,
            "country_id": j
        }
    }


    
    elif(y.lang=="ml"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.MALAYALAM)

        #y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.MALAYALAM)
        #z=transliterate(xa['road'], sanscript.ITRANS, sanscript.MALAYALAM)
        a=transliterate(xa['neighbourhood'], sanscript.ITRANS, sanscript.MALAYALAM)
        b=transliterate(xa['suburb'], sanscript.ITRANS, sanscript.MALAYALAM)
        c=transliterate(xa['city_district'], sanscript.ITRANS, sanscript.MALAYALAM)
        d=transliterate(xa['city'], sanscript.ITRANS, sanscript.MALAYALAM)
        e=transliterate(xa['county'], sanscript.ITRANS, sanscript.MALAYALAM)
        f=transliterate(xa['state_district'], sanscript.ITRANS, sanscript.MALAYALAM)
        g=transliterate(xa['state'], sanscript.ITRANS, sanscript.MALAYALAM)
        h=transliterate(xa['postcode'], sanscript.ITRANS, sanscript.MALAYALAM)
        i=transliterate(xa['country'], sanscript.ITRANS, sanscript.MALAYALAM)
        j=transliterate(xa['country_code'], sanscript.ITRANS, sanscript.MALAYALAM)

        final_updated={"address": {
            #"amenity": y,
            #"road": z,
            "neighbourhood": a,
            "suburb": b,
            "city_district": c,
            "city": d,
            "county": e,
            "state_district": f,
            "state": g,
            "postcode": h,
            "country": i,
            "country_id": j
        }
    }


    elif(y.lang=="te"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.TELUGU)

        #y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.TELUGU)
        #z=transliterate(xa['road'], sanscript.ITRANS, sanscript.TELUGU)
        a=transliterate(xa['neighbourhood'], sanscript.ITRANS, sanscript.TELUGU)
        b=transliterate(xa['suburb'], sanscript.ITRANS, sanscript.TELUGU)
        c=transliterate(xa['city_district'], sanscript.ITRANS, sanscript.TELUGU)
        d=transliterate(xa['city'], sanscript.ITRANS, sanscript.TELUGU)
        e=transliterate(xa['county'], sanscript.ITRANS, sanscript.TELUGU)
        f=transliterate(xa['state_district'], sanscript.ITRANS, sanscript.TELUGU)
        g=transliterate(xa['state'], sanscript.ITRANS, sanscript.TELUGU)
        h=transliterate(xa['postcode'], sanscript.ITRANS, sanscript.TELUGU)
        i=transliterate(xa['country'], sanscript.ITRANS, sanscript.TELUGU)
        j=transliterate(xa['country_code'], sanscript.ITRANS, sanscript.TELUGU)

        final_updated={"address": {
            #"amenity": y,
            #"road": z,
            "neighbourhood": a,
            "suburb": b,
            "city_district": c,
            "city": d,
            "county": e,
            "state_district": f,
            "state": g,
            "postcode": h,
            "country": i,
            "country_id": j
        }
    }

    elif(y.lang=="ta"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.TAMIL)

        #y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.TAMIL)
        #z=transliterate(xa['road'], sanscript.ITRANS, sanscript.TAMIL)
        a=transliterate(xa['neighbourhood'], sanscript.ITRANS, sanscript.TAMIL)
        b=transliterate(xa['suburb'], sanscript.ITRANS, sanscript.TAMIL)
        c=transliterate(xa['city_district'], sanscript.ITRANS, sanscript.TAMIL)
        d=transliterate(xa['city'], sanscript.ITRANS, sanscript.TAMIL)
        e=transliterate(xa['county'], sanscript.ITRANS, sanscript.TAMIL)
        f=transliterate(xa['state_district'], sanscript.ITRANS, sanscript.TAMIL)
        g=transliterate(xa['state'], sanscript.ITRANS, sanscript.TAMIL)
        h=transliterate(xa['postcode'], sanscript.ITRANS, sanscript.TAMIL)
        i=transliterate(xa['country'], sanscript.ITRANS, sanscript.TAMIL)
        j=transliterate(xa['country_code'], sanscript.ITRANS, sanscript.TAMIL)

        final_updated={"address": {
            #"amenity": y,
            #"road": z,
            "neighbourhood": a,
            "suburb": b,
            "city_district": c,
            "city": d,
            "county": e,
            "state_district": f,
            "state": g,
            "postcode": h,
            "country": i,
            "country_id": j
        }
    }


    elif(y.lang=="or"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.ORIYA)

        #y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.ORIYA)
        #z=transliterate(xa['road'], sanscript.ITRANS, sanscript.ORIYA)
        a=transliterate(xa['neighbourhood'], sanscript.ITRANS, sanscript.ORIYA)
        b=transliterate(xa['suburb'], sanscript.ITRANS, sanscript.ORIYA)
        c=transliterate(xa['city_district'], sanscript.ITRANS, sanscript.ORIYA)
        d=transliterate(xa['city'], sanscript.ITRANS, sanscript.ORIYA)
        e=transliterate(xa['county'], sanscript.ITRANS, sanscript.ORIYA)
        f=transliterate(xa['state_district'], sanscript.ITRANS, sanscript.ORIYA)
        g=transliterate(xa['state'], sanscript.ITRANS, sanscript.ORIYA)
        h=transliterate(xa['postcode'], sanscript.ITRANS, sanscript.ORIYA)
        i=transliterate(xa['country'], sanscript.ITRANS, sanscript.ORIYA)
        j=transliterate(xa['country_code'], sanscript.ITRANS, sanscript.ORIYA)

        final_updated={"address": {
            #"amenity": y,
            #"road": z,
            #"neighbourhood": a,
            "suburb": b,
            "city_district": c,
            "city": d,
            "county": e,
            "state_district": f,
            "state": g,
            "postcode": h,
            "country": i,
            "country_id": j
        }
    }



    elif(y.lang=="pa"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.GURMUKHI)

        #y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.GURMUKHI)
        #z=transliterate(xa['road'], sanscript.ITRANS, sanscript.GURMUKHI)
        a=transliterate(xa['neighbourhood'], sanscript.ITRANS, sanscript.GURMUKHI)
        b=transliterate(xa['suburb'], sanscript.ITRANS, sanscript.GURMUKHI)
        c=transliterate(xa['city_district'], sanscript.ITRANS, sanscript.GURMUKHI)
        d=transliterate(xa['city'], sanscript.ITRANS, sanscript.GURMUKHI)
        e=transliterate(xa['county'], sanscript.ITRANS, sanscript.GURMUKHI)
        f=transliterate(xa['state_district'], sanscript.ITRANS, sanscript.GURMUKHI)
        g=transliterate(xa['state'], sanscript.ITRANS, sanscript.GURMUKHI)
        h=transliterate(xa['postcode'], sanscript.ITRANS, sanscript.GURMUKHI)
        i=transliterate(xa['country'], sanscript.ITRANS, sanscript.GURMUKHI)
        j=transliterate(xa['country_code'], sanscript.ITRANS, sanscript.GURMUKHI)

        final_updated={"address": {
            #"amenity": y,
            #"road": z,
            "neighbourhood": a,
            "suburb": b,
            "city_district": c,
            "city": d,
            "county": e,
            "state_district": f,
            "state": g,
            "postcode": h,
            "country": i,
            "country_id": j
        }
    }

   

    if results and len(results):
        return {"Formatted address": x,"address": final_updated}
    #except RateLimitExceededError as ex:
          #print(ex)















"""
    am= transliterate("amenity",sanscript.ITRANS, sanscript.DEVANAGARI)
    am2=transliterate("road",sanscript.ITRANS, sanscript.DEVANAGARI)
    am3=transliterate("neighbourhood",sanscript.ITRANS, sanscript.DEVANAGARI)
    am4=transliterate("suburb",sanscript.ITRANS, sanscript.DEVANAGARI)
    am5=transliterate("city_district",sanscript.ITRANS, sanscript.DEVANAGARI)
    am6=transliterate("city",sanscript.ITRANS, sanscript.DEVANAGARI)
    am7=transliterate("county",sanscript.ITRANS, sanscript.DEVANAGARI)
    am8=transliterate("state_district",sanscript.ITRANS, sanscript.DEVANAGARI)
    am9=transliterate("state",sanscript.ITRANS, sanscript.DEVANAGARI)
    am10=transliterate("postcode", sanscript.ITRANS, sanscript.DEVANAGARI)
    am11=transliterate("country",sanscript.ITRANS, sanscript.DEVANAGARI)
    am12=transliterate("country_code",sanscript.ITRANS, sanscript.DEVANAGARI)
    final_updated={"address": {
            am: y,
            am2: z,
            am3: a,
            am4: b,
            am5: c,
            am6: d,
            am7: e,
            am8: f,
            am9: g,
            am10: h,
            am11: i,
            am12: j

        }
    }
"""




"""

@app.post("/addressformatter/language")
async def addressformatter(text: str , lang:str):
    print(text)
    translate_text1=translator.translate(text,src=lang,dest='en')
    print(translate_text1)
    translate_text=translate_text1.text
    list=translate_text.split(',')
    joined_string = ",".join(list[0:4])
    print(list)
    print(joined_string)
    first_component_addr=list[0]
    second_component_addr=list[1]
    third_component_addr=list[2]
    print(first_component_addr)
    print(second_component_addr)
    print(third_component_addr)
    results = geocoder.geocode(translate_text)
    latitude=results[0]['geometry']['lat']
    longitude=results[0]['geometry']['lng']
    #print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        #results[0]['geometry']['lng'],
                        #results[0]['components']['country_code']))
    
    text = geolocator.reverse(str(latitude)+","+str(longitude))
    print(text)
    translate_text= text.raw['address']
    print(translate_text)
    
    try:
        text1 = geocoder.reverse_geocode(latitude, longitude, language='en', no_annotations='1')
        print(text1)
        if text1 and len(text1):
           text2=text1[0]['formatted'].replace("unnamed road",joined_string)
           #translated_addr= translator.translate(res,lang_tgt=lang)
           translated_addr=translator.translate(text,src='en',dest=lang)
           return {"Formatted address": translated_addr,"address": translate_text}
    except RateLimitExceededError as ex:
           print(ex)

"""

"""

#URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"
    #api_key = '1KA1QFOkN14SsIr0AtksGQG9RXK0dC8noQOHQrEfPf0'
    #PARAMS = {
	#		'at': '{},{}'.format(latitude,longitude),
	#		'apikey': api_key
    #    }

    # Sending get request and saving the response as response object 
    #r = requests.get(url = URL, params = PARAMS) 
  
    # Extracting data in json format 
    #data = r.json() 

    #Taking out title from JSON
    #address = data['items'][0]['title'] 
    #return {"Address with all the fields":data}

    
    #return {"address": address, "latitude": results[0]['geometry']['lat'], "longitude":results[0]['geometry']['lng'],"Country Code":results[0]['components']['country_code']}



#geo_url = 'http://maps.googleapis.com/maps/api/geocode/json'
#my_address = {'address': '21 Ramkrishana Road, Burdwan, East Burdwan, West Bengal, India', 
             #'language': 'en'}
#response = requests.get(geo_url, params = my_address)
#results = response.json()['results']
#print(results)
#my_geo = results[0]['geometry']['location']
#print("Longitude:",my_geo['lng'],"\n","Latitude:",my_geo['lat'])

"""