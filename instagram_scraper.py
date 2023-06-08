from time import sleep
from random import randint
from instagram_private_api import Client, ClientCompatPatch, ClientError

#test_bio = []

def scrape_instagram_usernames(user_name, password, instagram_usernames, email_public):
    for name_unit in instagram_usernames:
        delay = randint(6, 12)
        print(f'Sleep {delay} sec')
        sleep(delay)

        try:
            api = Client(user_name, password)
            target_user_info = api.username_info(name_unit)
            
            if 'public_email' in target_user_info['user']:
                public_email = target_user_info['user']['public_email']
                email_public.append(public_email)
                print(f"Public email of {name_unit}: {public_email}")
            else:
                print(f"No public email found for {name_unit}")
        
        except ClientError as e:
            print(e)
