from pyfiglet import figlet_format      #https://pypi.org/project/pyfiglet/
from termcolor import colored           #https://pypi.org/project/colored/
import requests                         #https://pypi.org/project/requests/
import random                           #https://pypi.org/project/random2/y
from mailmodule import send_message

print(colored(figlet_format("Dad joke 2022"), color="red"))
topic = ("dog", "money", "man", "woman", " ", "school", "cat", "life", "football")
topic = random.choice(topic)

url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers = {"Accept": "application/json"},
    params = {"term": topic, "limit": 20}
)
data = response.json()
quantity_of_jokes = len(data['results'])
if (quantity_of_jokes > 0):
    random_joke = random.choice(data['results'])
    joke = random_joke['joke']
    print(joke)
    send_message(joke)
else:
    print(f"Sory, I don't have any jokes about '{topic}'! Please try again.")

