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
    def build_url(account_type=None):
        base_url = f"https://fortnite-api.com/v2/stats/br/v2?name={username}"

        if season == 'season':
            base_url += "&timeWindow=season"

        if account_type:
            base_url += f"&accountType={account_type}"

        return base_url

    account_types = [None, 'psn', 'xbl']

    for account_type in account_types:
        url = build_url(account_type)
        response = api_request(url, "GET")

        if response.status_code == 200:
            return parce_stat(response.json(), username)

        if response.status_code == 403:
            return 'Треба відкрити стату'

    return f'Такого користувача {username} не знайдено, або ти ще не катав в цьому сезоні'



def stat(wins, kills, deaths, kd, matches, winRate, minutes, username, top3, top5, kpm):
    template = (
        f'{username}\n'
        f"{'🐓'*len(username)}\n"
        'Ваша ст<b>ass</b>тистика: \n'
        f'За весь цей час ти насовав за щоку {kills} чувакам 🧟\n'
        f'В твоєму роті побувало  {deaths} школярів!  🧟\n'
        f'КД: {kd} 🏅\n'
        f'Кількість ударів тобі по губах за хвилину: {kpm} 🏆\n'
        f'Кількість перемог: {wins}🏆\n'
        f'Топ-3 защеканів: {top3}🏆\n' 
        f'Кількість матчів: {matches}  🏆\n'
        f'Відсоток виграшів: {winRate}%\n'
        f'Проїбав життя на: {round(minutes/60, 1)} годин'
    )

    if 'SHOORIK88' in username and minutes <= 60:
        time_to_play = 60 - minutes
        template = (
            f'<b>🐓🐓Пан Пітушурік🐓🐓</b>\n'
            'Ваша ст<b>ass</b>тистика заблокована \n'
            f''
            f'Для повернення доступу до стати ви маєте просидіти на гарячих хуйцях ще {time_to_play} хвилин\n'


    )
    elif 'SHOORIK88' in username and minutes <= 12381:
        time_to_play = 12381  - minutes
        template = (
            f'<b>🐓🐓Пан Пітушурік🐓🐓</b>\n'
            'Ваша ст<b>ass</b>тистика заблокована \n'
            f''
            f'Для повернення доступу до стати ви маєте просидіти на гарячих хуйцях ще {time_to_play} хвилин\n'

        )
    return template



def parce_stat(resp, username):
    wins = resp['data']['stats']['all']['overall']['wins']
    top3 = resp['data']['stats']['all']['overall']['top3']
    top5 = resp['data']['stats']['all']['overall']['top5']
    kills_per_minute = resp['data']['stats']['all']['overall']['killsPerMin']
    kills = resp['data']['stats']['all']['overall']['kills']
    deaths = resp['data']['stats']['all']['overall']['deaths']
    kd = resp['data']['stats']['all']['overall']['kd']
    matches = resp['data']['stats']['all']['overall']['matches']
    winRate = resp['data']['stats']['all']['overall']['winRate']
    minutes = resp['data']['stats']['all']['overall']['minutesPlayed']
    message = stat(wins, kills, deaths, kd, matches, winRate, minutes, username, top3, top5, kills_per_minute)
    print(message)
    return message


if __name__ == '__main__':
    log.info('Starting...')
    get_fn_user_info('dmitryshane')



