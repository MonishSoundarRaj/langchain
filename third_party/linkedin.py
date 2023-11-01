import os
import requests
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

def scarpe_linkedin(Linkedin_url: str):
    api_key = os.environ['proxycurl']
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {
        'linkedin_profile_url': Linkedin_url,
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=headers)
    
    return response

def scrape_gists(url: str):
    response = requests.get(url)
    return response

# if __name__ == "__main__":
#     response = scrape_gists('https://gist.githubusercontent.com/MonishSoundarRaj/ef483b2d2d9e532679317e32bec23412/raw/41edbff0907f9c931d9451f7a146fee2d6fa8be0/linkedin_json')
#     result = response.json()
#     # print(result)
#     print(result.public_identifier)
    
    