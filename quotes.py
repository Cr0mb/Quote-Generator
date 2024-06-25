import requests
from random import choice

def fetch_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['content']
    else:
        return "Failed to fetch the quote :("

def main():
    input("Press Enter to get a random quote...")
    quote = fetch_quote()
    print("\nHere's a random quote for you:\n")
    print(quote)

if __name__ == "__main__":
    main()
