import requests
from dailyMeanings import todaysWords


class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def getUsers(self):
        updates = self.get_updates()
        users = {120293283}
        for update in updates:
            users.add(update['message']['chat']['id'])
        return users

    def sendDailyMessage(self):
        users = self.getUsers()
        resp = todaysWords()
        msg = "Word : "
        msg = msg + resp['word'] + "\n"
        if resp.get('pronunciation'):
            msg = msg + "Pronunciation : " + resp['pronunciation'] + "\n"
        if resp.get('definitions'):
            msg = msg + "Definitions : \n"
            definitions = resp['definitions']
            for definition in definitions:
                if definition.get('type'):
                    msg = msg + "Type :" + definition['type'] + "\n"
                if definition.get('definition'):
                    msg = msg + "Definition : " + definition['definition'] + "\n"
                if definition.get('example'):
                    msg = msg + "Example : " + definition['example'] + "\n"
        print(msg)
        for user in users:
            print(self.send_message(user, msg))



token = '1263401899:AAHBGl0tNG_LoiksP0NO_l2BfJmBuQSHlBY' #Token of your bot
dailyMeanings_bot = BotHandler(token) #Your bot's name



def main():
    new_offset = 0
    print('hi, now launching...')
    
    dailyMeanings_bot.sendDailyMessage()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()