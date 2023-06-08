#instaloder 
from instagram_private_api import Client, ClientCompatPatch, ClientError
from random import randint
from time import sleep
import re
from instaloader.exceptions import ProfileNotExistsException

from dotenv import load_dotenv
import os

from test import b, 

load_dotenv()
user_name = os.getenv("user_name")
password = os.getenv("password")


#name_list = b
TARGET_USERNAME = b


for name_unit in TARGET_USERNAME:
    delay = randint(3, 6)
    print(f'Sleep {delay} sec')
    sleep(delay)

    try:
        api = Client(user_name, password)
        target_user_info = api.username_info(TARGET_USERNAME)
        if target_user_info['user']['public_email']:
            public_email = target_user_info['user']['public_email']
            test_bio.append(public_email)
            print(f"Public email of {TARGET_USERNAME}: {public_email}")
        else:
            print(f"No public email found for {TARGET_USERNAME}")
    except ClientError as e:
        print(e)

print(test_bio)