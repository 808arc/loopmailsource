from time import sleep
from random import randint
from instagram_private_api import Client
from instagram_private_api.errors import ClientError

def login_to_instagram(user_name, password):
    api = Client(user_name, password)
    return api

def scrape_instagram_usernames(user_name, password, instagram_usernames, email_public, bio_list):
    api = login_to_instagram(user_name, password)

    for name_unit in instagram_usernames:
        delay = randint(11, 30)
        print(f'Sleep {delay} sec')
        sleep(delay)

        try:
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
            elif e.code == 'rate_limit_error':
                print(f"Rate limit error occurred. Re-logging in...")
                bio_list.append("_")
                email_public.append(" ")
                api = login_to_instagram(user_name, password)
                target_user_info = api.username_info(name_unit)
                # Retry the request or continue with the next username as desired
            else:
                print(f"Error occurred for user '{name_unit}': {e}")
                bio_list.append("_")
                email_public.append(" ")
                # Handle other errors as needed