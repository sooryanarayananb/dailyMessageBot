import requests
import json
import random

def getMeaning(word):
    owlbot_api = "https://owlbot.info/api/v4/dictionary/" + word
    response = requests.get(
        owlbot_api,
        headers={'Authorization': 'Token <token>'},
    )
    json_response = response.json()
    return json_response

def getWord():
    print("Started..")
    f = open('result.json',)
    data = json.load(f)
    print("Ended..")
    random_id = random.randrange(178186)
    print(data[str(random_id)])
    return data[str(random_id)]

def todaysWords():
    word = getWord()
    resp = getMeaning(word)
    while True:
        try:
            if 'message' in resp[0].keys():
                word = getWord()
                resp = getMeaning(word)
            else:
                break
        except KeyError:
            break
    print(resp) 
    return resp


if __name__ == "__main__":
     
     word = getWord()
     resp = getMeaning(word)

     while True:
        try:
            if 'message' in resp[0].keys():
                word = getWord()
                resp = getMeaning(word)
            else:
                break
        except KeyError:
            break 
     print(resp)
        
