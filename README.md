# Getting a business’s details from its GSTIN (Goods and Services Tax Identification Number) using GST Verification API.
## By Ruturaj Aher
### Nasik, Maharashtra, India.
#### Video Demo:  https://youtu.be/bnepFXt-rnk

#### Description:
#### The objective of the project is to fetch the details of a business from its GSTIN (Goods and Services Tax Identification Number).


#### ____________________________________________
#### Libraries used:
```
import requests
import datetime as dt
from tabulate import tabulate
```

#### Use of requests library:
> The requests library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application.
```
response = requests.request("POST", url, json=payload, headers=headers)
```

#### Use of datetime library:
> In this project it is used for formatting the date of registration field.
```
# formatting 2017-07-01 to Jul 01, 2017 using strftime('%b %d, %Y')
```
*[Line 17]*

#### Use of tabulate library:
> In this project it is used for formatting the output in a tabular form using "outline" format.
```
print(tabulate(mylist, tablefmt="outline"))
```
*[Line 127]*

#### ____________________________________________
#### API used:
(It is a freemium version, providing 35 requests per month for free)

#### Link: [GST Verification by RapidAPI](https://rapidapi.com/idfy-idfy-default/api/gst-verification)

#### ____________________________________________
#### Working:
> User is prompted for input as follows:
```
project/ $ python project.py
Enter the GSTIN :
```
After user inputs the GSTIN, the API is requested with POST request and the response is stored in a variable and then converted into json format.

> Received response formatted in JSON: (Some fields are represented in * for security purposes.)
```
{
  "action": "verify_with_source",
  "completed_at": "2023-02-19T18:34:47+05:30",
  "created_at": "2023-02-19T18:34:42+05:30",
  "group_id": "8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e",
  "request_id": "190469d8-57ad-410f-9475-389949e64778",
  "result": {
    "source_output": {
      "additional_place_of_business_fields": {},
      "centre_jurisdiction": "M*****N RANGE",
      "centre_jurisdiction_code": null,
      "constitution_of_business": "Proprietorship",
      "date_of_cancellation": null,
      "date_of_registration": "2017-0*-01",
      "gstin": "27CBRP******B",
      "gstin_status": "Active",
      "last_updated_date": "2022-**-16",
      "legal_name": "PRA**** DI******G S****L",
      "nature_of_business_activity": [
        "Works Contract"
      ],
      "principal_place_of_business_fields": {
        "nature_of_principal_place_of_business": "Works Contract",
        "principal_place_of_business_address": {
          "building_name": null,
          "city": null,
          "door_number": "S******G **. *, S*** **. *, N****R * * * * SO*Y L** S****G N*****, N*****",
          "dst": "Dhule",
          "floor_number": null,
          "latitude": null,
          "location": "TAL - Dhule",
          "longitude": null,
          "pincode": "42****",
          "state_name": "Maharashtra",
          "street": "N****R"
        }
      },
      "source": null,
      "state_jurisdiction_code": null,
      "status": "id_found",
      "taxpayer_type": "Regular",
      "trade_name": "J****** *******S"
    }
  },
  "status": "completed",
  "task_id": "74f4c926-250c-43ca-9c53-453e87ceacd1",
  "type": "ind_gst_certificate"
}
```
Stored as
```
jsonify = response.json()
```
#### The fields that the program displays:
> Legal name:
```
jsonify['result']['source_output']['legal_name']
```
> Date of registration:
```
jsonify['result']['source_output']['date_of_registration']
```
> GSTIN Status:
```
jsonify['result']['source_output']['gstin_status']
```
> Trade name:
```
jsonify['result']['source_output']['trade_name']
```
> Address:
```
base_addr = jsonify['result']['source_output']['principal_place_of_business_fields']['principal_place_of_business_address']['door_number']


    dist = jsonify['result']['source_output']['principal_place_of_business_fields']['principal_place_of_business_address']['dst']

    location = jsonify['result']['source_output']['principal_place_of_business_fields']['principal_place_of_business_address']['location']
    #taluka

    pincode = jsonify['result']['source_output']['principal_place_of_business_fields']['principal_place_of_business_address']['pincode']

    state = jsonify['result']['source_output']['principal_place_of_business_fields']['principal_place_of_business_address']['state_name']

    return f"{base_addr}, {location}, {dist}, {state}, {pincode}"
    # returned to the function - addres()
```
> Taxpayer type:
```
jsonify['result']['source_output']['taxpayer_type']
```
> Nature of business activity:
```
# List that stores result from jsonify['result']['source_output']['nature_of_business_activity']

b_a = []
    for i in jsonify['result']['source_output']['nature_of_business_activity']:
        b_a.append(i)
```
> Nature of place of business:
```
jsonify['result']['source_output']['principal_place_of_business_fields']['nature_of_principal_place_of_business']
```

#### The output formated using tabulate module:
```
print(tabulate(mylist, tablefmt="outline"))
```

#### Note:
1. Creation of account on RapidAPI is necessary for sending requests.
2. [API Key] is generated when signed up and is mandatory in the header field.
3. test_project.py file has been attached for executing tests on the functions:
```
trd_name()
nat_of_wok()
date()
```
4. If the length of GSTIN is either too long or too short, then the program will be terminated. Using:
```
sys.exit()
```
