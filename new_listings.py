import requests

def get_new_listings(api_url):
    """
    Fetch new token listings from a cryptocurrency exchange API.

    :param api_url: The API endpoint for new listings.
    :return: A list of new token listings.
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        listings = response.json()
        return listings['data']  # Assuming the API returns listings under 'data'
    else:
        print("Failed to fetch new listings")
        return []

# Example usage
api_url = "https://api.binance.com/api/v3/exchangeInfo"
new_listings = get_new_listings(api_url)
print(new_listings)

