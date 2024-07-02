import requests

def weather(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":f"{city}","format":"json","u":"f"}

    headers = {
        "x-rapidapi-key": "2f5624bef6mshb4f1aeef6a5a36cp1d6ebcjsn8e8aeb3e2ec6",
        "x-rapidapi-host": "yahoo-weather5.p.rapidapi.com"
    }

    r = requests.get(url, headers=headers, params=querystring)
    response = r.json()
    data_city = f"""🪩 Joylashuv:
📍 Manzil: {response['location']['country']}
🌄 Quyosh chiqish vaqti:{response['current_observation']['astronomy']['sunrise']}
🌅 Quyosh botish vaqti:{response['current_observation']['astronomy']['sunset']}
🌤️ Havo harotati: {round((response['current_observation']['condition'][ 'temperature'] - 32) * 5 / 9)} ({response['current_observation']['condition']['text']})"""

    return data_city



def chatgpt(message):
    url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"

    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"{message}"
            }
        ],
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256,
        "web_access": False
    }
    headers = {
        "x-rapidapi-key": "2f5624bef6mshb4f1aeef6a5a36cp1d6ebcjsn8e8aeb3e2ec6",
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())
