import requests

def get_joke() -> str:
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            joke = joke_data["value"]
            return joke
    except requests.exceptions.RequestException as e:
        print("Error", str(e))


if __name__ == "__main__":
    active = True
    while active:
        print(get_joke())
        print("(1) Another Joke (2) Quit: ")
        if input() != "1":
            active = False