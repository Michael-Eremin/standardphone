# standardphone
Convert string to phone format.
There remains a string of only numbers from 0 to 9. If the quantity of numbers is 11 and the first 2 numbers are '89' or '79',if the number is 10 and the first character is '9', then the string is converted to the format '8 (9xx) xxx xx xx'. Otherwise, it will be converted to the format 'xxx...'.

####Server start

>uvicorn server_phone:app --reload
