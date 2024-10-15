import requests

def get(num_words=35):
    # fetch
    api_url = f"https://random-word-api.herokuapp.com/word?number={num_words}"
    
    # Send request to API
    response = requests.get(api_url)
    
    # Using a Json
    if response.status_code == 200:
        words = response.json()
        return words
    else:
        print("Failed to fetch words. Status code:", response.status_code)
        return []

if __name__ == "__main__":
    # Test
    random_word = get()
    print(random_word)
