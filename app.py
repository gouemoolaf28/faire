import requests
import gspread
from main import add_brand
from fake_useragent import UserAgent
from json.decoder import JSONDecodeError

ua = UserAgent()

url = "https://www.faire.com/api/brand/all-brands"

headers = {
    'content-type': "application/json",
    'User-Agent': ua.random
}

response = requests.get(url, headers=headers)

data = response.json()

brands = data['brands']

print(f"Total number of Brands : {len(brands)}")


for brand in brands:
    token = brand['token']
    resp = requests.get(f"https://www.faire.com/api/brand-view/{token}")

    dat = resp.json()
    try:
        brand_id = dat['brand']['token']
        name = dat['brand']['name'].lower()
        country = dat['brand']['based_in']
        brandView = {
            'brand_id': brand_id,
            'name': name,
            'country': country
        }

        add_brand(brandView['brand_id'], brandView['name'], brandView['country'])

        print(brandView)

    except (KeyError, JSONDecodeError) :
        brandView = {
            'brand_id': brand_id,
            'name': name,
            'country': None
        }
        
        add_brand(brandView['brand_id'], brandView['name'], brandView['country'])
        print(brandView)
        continue
