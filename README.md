# Address-Formatting

## Steps to Access
-  To check the API, you can visit this link--->[Backend API Swagger Documentation](https://addressformatteruidai.herokuapp.com/docs)
-  [Video Demonstration](https://drive.google.com/file/d/1W7t3_yy6i-Whm_kMqNL27vasFH5qVRfF/view?usp=sharing)
-  [Google Slides Presentation](https://docs.google.com/presentation/d/12xOHlllMnZzDm7Psc9FV188bEZRKF1FIRM8Ce2vzSe4/edit?usp=sharing)



## FastAPI Server
- Clone the repo in your local machine and setup python environment. Create .env file with `API_KEY` of Opencage.
- Install all the required packages in python virtual enviroment `pip install requirements.txt`
- Run `python main.py` in the root directory of the project.

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
POST /https://addressformatteruidai.herokuapp.com/docs#/Address-Formatting/addressformattereng_addressformatter__post
```

| Parameter | Type 
| :--- | :--- |
| `address` | `json` | 

#### Request Body
```json
{
  "building": "string",
  "street": "string",
  "landmark": "string",
  "locality": "string",
  "vtc": "string",
  "district": "string",
  "state": "string"
}
```

#### Response

Many API endpoints return the JSON representation of the resources created or edited. Address Formatter returns a JSON response in the following format:

```json
{
  "status": 200,
  "data": {
    "Formatted address": "string",
    "address": {
      "suburb": "string",
      "city": "string",
      "county": "string",
      "state_district": "string",
      "state": "string",
      "postcode": "string",
      "country": "string",
      "country_code": "string",
      "house no.": "string"
    }
  }
}
```

The `Formatted address` attribute contains the optimized address in a pretty format

The `address` attribute contains all the details related to address like  zipcode, city_district, city, country, state in a JSON format.


#### 2. Formatting the Regional Address

```http
POST /https://addressformatteruidai.herokuapp.com/docs#/Address-Formatting/addressformatterregional_addressformatterregionallanguages__post
```

| Parameter | Type 
| :--- | :--- |
| `text(in regional language)` | `string` | 

#### Response

Address Formatter for regional language returns a JSON response in the following format:

```javascript
{
  "status": 200,
  "data": {
    "Formatted address": "string",
    "address": {
      "address": {
        "amenity": "string",
        "road": "string",
        "neighbourhood": "string",
        "suburb": "string",
        "city_district": "string",
        "city": "string",
        "county": "string",
        "state_district": "string",
        "state": "string",
        "postcode": "string",
        "country": "string",
        "country_id": "string"
      }
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

