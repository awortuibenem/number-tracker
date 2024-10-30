import requests

def get_phone_number_info(phone_number, api_key):
    url = f"https://api.numlookupapi.com/v1/validate/{phone_number}?apikey={api_key}"
    response = requests.get(url)
    return response.json()

phone_number = "+0000000"
api_key = "PUT_YOURS"

info = get_phone_number_info(phone_number, api_key)

print(f"Phone Number Info: {info}")
print(f"Country: {info['country_name']}")
print(f"Carrier: {info['carrier']}")
print(f"Location: {info['country_code']}")