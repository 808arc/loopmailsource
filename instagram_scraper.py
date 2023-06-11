from time import sleep
from random import randint
from instagram_private_api import Client
from instagram_private_api.errors import ClientError

def scrape_instagram_usernames(user_name, password, instagram_usernames, email_public, bio_list):
    for name_unit in instagram_usernames:
        delay = randint(12, 30)
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
                email_public.append(" ")
                print(f"No public email found for {name_unit}")

            if 'biography' in target_user_info['user']:
                bio = target_user_info['user']['biography']
                bio_list.append(bio)
                print(f"Bio of {name_unit}: {bio}")
            else:
                bio_list.append("_")
                print(f"No bio found for {name_unit}")
        
        except ClientError as e:
            if e.code == 'user_not_found':
                print(f"User '{name_unit}' not found")
                bio_list.append("_")
                email_public.append(" ")
            else:
                print(f"Error occurred for user '{name_unit}': {e}")
