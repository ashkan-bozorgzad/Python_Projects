import requests

NUMBER_OF_QUESTIONS = 10
TYPE_OF_QUESTIONS = "boolean"

parameters = {
    "amount": NUMBER_OF_QUESTIONS,
    "type": TYPE_OF_QUESTIONS,
    "category": 18,
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]