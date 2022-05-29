# standardphone
Convert string to phone format.
There remains a string of only numbers from 0 to 9. If the quantity of numbers is 11 and the first 2 numbers are '89' or '79',if the number is 10 and the first character is '9', then the string is converted to the format '8 (9xx) xxx xx xx'. Otherwise, it will be converted to the format 'xxx...'.<br/>
Four options for receiving a request are implemented. Through form data, json, query and coockies.

#### Development Requirements

#### Python 3.10.0

* fastapi
* loguru
* typing


### Run server
#### On localhost:
##### Installing
* start the command processing server: **uvicorn server_phone:app --reload**
    Default IP = **127.0.0.1**, PORT = **8000**
    <br>
* install and run the "POSTMAN" client.
##### Request process from "POSTMAN" client.
###### Processing incoming JSON data.
* URI: http://localhost/unify_phone_from_json
* POST request. Raw JSON in Body: {"phone": "8902356xx35_45"}
###### Processing incoming FORM data.
* URI: http://localhost/unify_phone_from_form
* POST request. Form-data in Body: Key: phone, Value: 9012345678
###### Processing incoming QUERY parameters data.
* URI: http://localhost/unify_phone_from_query
* GET request. Request string: http://localhost/unify_phone_from_query?phone=8903_568n74-10
###### Processing incoming COOKIES data.
* URI: http://localhost/unify_phone_from_cookies
* GET request. Headers: Key: Coockie, Value: phone=79012345678


#### Web request:
The **server_phone.py** service is located at host **standardrksok.ru** 
* Change part of the URI:**http://localhost/** to: **https://standardrksok.ru/**
* Request with QUERY parameters is possible from the Browser string: **https://standardrksok.ru/unify_phone_from_query?phone=8903_568n74-10**
