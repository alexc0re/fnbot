import logging
import time
import asyncio
import requests
from envsetup import Credentials
from support.logger import log_method
from support.logger import log
from support.texts import *

task = None


headers = {
    'Authorization': f'{Credentials.AUTH_TOKEM}'
}
payload = {}
log = log_method(logLevel=log.INFO)
logging.basicConfig(level=logging.INFO)


def api_request(endpoint, method):

    response = requests.request(method, endpoint, headers=headers, data=payload)
    log.info(f'{method} at {endpoint} response: {response.status_code} ')
    return response




def get_fn_user_info(username, season='all'):
    if season == 'all':
        url = f"https://fortnite-api.com/v2/stats/br/v2?name={username}"
    elif season == 'season':
        url = f"https://fortnite-api.com/v2/stats/br/v2?name={username}&timeWindow={season}"
    message = str
    log.info(f'get_fn_user_info: {username}')
    endpoint = url
    method = "GET"
    response = api_request(endpoint, method)
    log.info(f'Response: {response.status_code}')

    if response.status_code == 200:
        resp = response.json()
        wins = resp['data']['stats']['all']['overall']['wins']
        kills = resp['data']['stats']['all']['overall']['kills']
        deaths = resp['data']['stats']['all']['overall']['deaths']
        kd = resp['data']['stats']['all']['overall']['kd']
        matches = resp['data']['stats']['all']['overall']['matches']
        winRate = resp['data']['stats']['all']['overall']['winRate']
        minutes = resp['data']['stats']['all']['overall']['minutesPlayed']
        message = stat(wins, kills, deaths, kd, matches, winRate, minutes)
        print(message)
        return message

    elif response.status_code == 403:
        message = 'Треба відкрити стату'
        return message

    elif response.status_code == 404:
        message = 'Такого користувача немає 404'
    return message



def stat(wins, kills, deaths, kd, matches, winRate, minutes):
    template = (
        'Ваша ст<b>ass</b>тистика: \n'
        f'За весь цей час ти насовав за щоку {kills} чувакам 🧟\n'
        f'В твоєму роті побувало  {deaths} школярів!  🧟\n'
        f'КД: {kd} 🏅\n'
        f'Кількість перемог: {wins}\n'
        f'Кількість матчів: {matches}  🏆\n'
        f'Відсоток виграшів: {winRate}%\n'
        f'Проїбав життя на: {round(minutes/60, 1)} годин'
    )
    return template



if __name__ == '__main__':
    log.info('Starting...')
    get_fn_user_info('dmitryshane')



