# ADDRESS-FORMATTING


## Architecture
![image](https://user-images.githubusercontent.com/60667917/139524901-0a25e1ba-6038-4600-8f88-ec42369715c8.png)



## Introduction

Address Formatter is built from the ground-up with a JSON API that makes it easy for developers and sysadmins to optimize the uneven complex residential address.


## Use Cases

Address Formatter Api incorporates various use cases related to address formatting. The most common use case is to update the address for Aadhar Card, if there is some big typo or errors in the address. It supports 15 regional languages because in India apart from English lot of other languages are also spoken.


## Authorization

All API requests require the use OpenCage API key. You can create your own API key, by navigating to the OpenCage docs.

## Requests

#### 1. Formatting the English Address
```http
POST /localhost:8000/docs#/Address-Formatting/addressformattereng_addressformatter__post
```

| Parameter | Type 
| :--- | :--- |
| `address` | `string` | 

#### Response

Many API endpoints return the JSON representation of the resources created or edited. Address Formatter returns a JSON response in the following format:

```javascript
{
  "Formatted Address" : string,
  "address": {
    "city": "string",
    "county": "string",
    "state_district": "string",
    "state": "string",
    "postcode": "string",
    "country": "string",
    "country_code": "string"
  }
}
```

The `Formatted address` attribute contains the optimized address in a pretty format

The `address` attribute contains all the details related to address like  zipcode, city_district, city, country, state in a JSON format.


#### 2. Formatting the Regional Address

```http
POST /http://localhost:8000/docs#/Address-Formatting/addressformatterregional_addressformatterregionallanguages__post
```

| Parameter | Type 
| :--- | :--- |
| `text(in regional language)` | `string` | 

#### Response

Address Formatter for regional language returns a JSON response in the following format:

```javascript
{
  "Formatted address": "ग़्ट्ःPष् आउस्तिन्तोव्न्, Oल्द् ऱचे छोउर्से ऱोअद्, आगरम्, Bएन्गलुरु - ५६००९५, ख़र्नतक, ईन्दिअ",
  "address": {
    "address": {
      "amenity": "ग़्ट्ःPष् आउस्तिन्तोव्न्",
      "road": "Oल्द् ऱचे छोउर्से ऱोअद्",
      "neighbourhood": "य़ेल्लगोन्दन्पल्य",
      "suburb": "आगरम्",
      "city_district": "Eअस्त् Zओने",
      "city": "Bएन्गलुरु",
      "county": "Bअन्गलोरे णोर्थ्",
      "state_district": "Bअन्गलोरे ऊर्बन्",
      "state": "ख़र्नतक",
      "postcode": "- ५६००९५",
      "country": "ईन्दिअ",
      "country_id": "इन्"
    }
  }
}
```

The `Formatted address` attribute contains the optimized address in a pretty format

The `address` attribute contains all the details related to address like road ,neighbourhood ,suburb ,zipcode, city_district, city, country, amenity in a JSON format.

## Status Codes

Gophish returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 400 | `BAD REQUEST` |
| 422 | `VALIDATION ERROR` |

