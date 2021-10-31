from fastapi import FastAPI
import requests
from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError
from pydantic import BaseModel
from urllib.request import urlopen
import json
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import googletrans
from googletrans import Translator
from fastapi import APIRouter, HTTPException
from fastapi import Body, FastAPI
import os
import fcntl
from dotenv import load_dotenv



load_dotenv()
API_KEY=os.getenv("API_KEY")
geocoder = OpenCageGeocode(API_KEY)


translator=Translator()



app = FastAPI(title="Address Formatter",
              description="Optimize your address",
              version="0.0.1",
              )


@app.post("/addressformatter/",tags=["Address-Formatting"],description="Optimize your address in english language")
async def addressformattereng(address: str =Body(...)):
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
           house_noo=joined_string
           list2=house_noo.split(',')
           joined_string2 = ",".join(list[0:1])
           address["house no."]=joined_string2
           return {"status":200,"data":{"Formatted address": res,"address": address}}
    except RateLimitExceededError as ex:
           print(ex)









    


@app.post("/addressformatterregionallanguages/",tags=["Address-Formatting"],description="Optimize your address in regional language")
async def addressformatterregional(text : str=Body(...)):
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
        x=transliterate(results[0]['formatted'],sanscript.ITRANS,sanscript.DEVANAGARI )
        y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.DEVANAGARI)
        z=transliterate(xa['road'], sanscript.ITRANS, sanscript.DEVANAGARI)
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
            "amenity": y,
            "road": z,
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

        y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.GUJARATI)
        z=transliterate(xa['road'], sanscript.ITRANS, sanscript.GUJARATI)
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
            "amenity": y,
            "road": z,
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

        y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.BENGALI)
        z=transliterate(xa['road'], sanscript.ITRANS, sanscript.BENGALI)
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
            "amenity": y,
            "road": z,
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

        y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.BENGALI)
        z=transliterate(xa['road'], sanscript.ITRANS, sanscript.BENGALI)
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
            "amenity": y,
            "road": z,
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

        y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.KANNADA)
        z=transliterate(xa['road'], sanscript.ITRANS, sanscript.KANNADA)
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
            "amenity": y,
            "road": z,
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

        y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.MALAYALAM)
        z=transliterate(xa['road'], sanscript.ITRANS, sanscript.MALAYALAM)
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
            "amenity": y,
            "road": z,
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

        y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.TELUGU)
        z=transliterate(xa['road'], sanscript.ITRANS, sanscript.TELUGU)
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
            "amenity": y,
            "road": z,
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

        y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.TAMIL)
        z=transliterate(xa['road'], sanscript.ITRANS, sanscript.TAMIL)
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
            "amenity": y,
            "road": z,
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

        y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.ORIYA)
        z=transliterate(xa['road'], sanscript.ITRANS, sanscript.ORIYA)
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
            "amenity": y,
            "road": z,
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



    elif(y.lang=="pa"):
        x=transliterate(results[0]['formatted'], sanscript.ITRANS, sanscript.GURMUKHI)

        y=transliterate(xa['amenity'], sanscript.ITRANS, sanscript.GURMUKHI)
        z=transliterate(xa['road'], sanscript.ITRANS, sanscript.GURMUKHI)
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
            "amenity": y,
            "road": z,
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

   
    try:
       if results and len(results):
        return {"status":200,"data":{"Formatted address": x,"address": final_updated}}
    except RateLimitExceededError as ex:
          print(ex)
          raise HTTPException(status_code=400, detail=str(e))
