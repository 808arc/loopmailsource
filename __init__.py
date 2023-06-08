from instagram_private_api import Client, ClientCompatPatch, ClientError
from random import randint
from time import sleep
import re


user_name = 'searcher.beats'
password = 'instagram.com9'


api = Client(user_name, password)