"""Convert string to phone format."""
from fastapi import FastAPI, Form, Cookie, Body
from fastapi.responses import Response
from typing import Optional
from loguru import logger

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="5:00")

app = FastAPI()

def from_string_to_phone(input_str: str):
    "There remains a string of only numbers from 0 to 9. If the quantity of numbers is 11 and the first 2 numbers are '89' or '79',if the number is 10 and the first character is '9', then the string is converted to the format '8 (9xx) xxx xx xx'. Otherwise, it will be converted to the format 'xxx...'."
    logger.info(f'input_str:{input_str!r}')
    digit_str = ''.join(i for i in input_str if i.isdigit())
    logger.info(f'digit_str:{digit_str!r}')
    if len(digit_str) == 11 and digit_str[0:2] == '79' or digit_str[0:2] == '89':
        message_to_client = f"8 (9{digit_str[2:4]}) {digit_str[4:7]}-{digit_str[7:9]}-{digit_str[9:11]}"
    elif len(digit_str) == 10 and digit_str[0:1] == '9':
        message_to_client = f"8 (9{digit_str[1:3]}) {digit_str[3:6]}-{digit_str[6:8]}-{digit_str[8:10]}"
    else:
        message_to_client = digit_str
    logger.info(f'message_to_client:{message_to_client!r}')
    return message_to_client

#Gets data in the format 'json'.
@app.post("/unify_phone_from_json")
def response_to_client(data: dict = Body(...)):
    logger.info(f'data:{data!r}')
    input_str = str(data)
    message_phone = from_string_to_phone(input_str)
    logger.info(f'message_phone:{message_phone!r}')
    msg = Response(f"{message_phone}", media_type="text/html")
    return msg

#Gets data in the format 'Form'.
@app.post("/unify_phone_from_form")
def response_to_client(phone: str = Form(...)):
    logger.info(f'phone:{phone!r}')
    message_phone = from_string_to_phone(phone)
    logger.info(f'message_phone:{message_phone!r}')
    msg = Response(f"{message_phone}", media_type="text/html")
    return msg

#Gets data in the format 'Query Parameters'.
@app.get("/unify_phone_from_query")
def response_to_client(phone: str = ''):
    logger.info(f'phone:{phone!r}')
    message_phone = from_string_to_phone(phone)
    logger.info(f'message_phone:{message_phone!r}')
    msg = Response(f"{message_phone}", media_type="text/html")
    return msg

#Gets data in the format 'Cookie Parameters'.
@app.get("/unify_phone_from_cookies")
def response_to_client(phone: Optional[str] = Cookie(default=None)):
    data =str({"phone": phone})
    logger.info(f'phone:{data!r}')
    message_phone = from_string_to_phone(data)
    logger.info(f'message_phone:{message_phone!r}')
    msg = Response(f"{message_phone}", media_type="text/html")
    return msg