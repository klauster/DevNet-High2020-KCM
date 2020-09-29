
import json
import requests

joke_response = requests.get('https://api.chucknorris.io/jokes/random')

joke_text = joke_response.text

joke_dict = json.loads(joke_text)

print(joke_dict['value'])