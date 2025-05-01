import json

import requests
from bs4 import BeautifulSoup
import datetime

import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}

year, month, day = datetime.date.today().isoformat().split("-")
url_list = [f"https://www.tennisexplorer.com/madrid/{year}/atp-men/",
       f"https://www.tennisexplorer.com/madrid-wta/{year}/wta-women/"]


def get_soup(url: str, headers: dict):
    """Получаем ответ с обработкой ошибок"""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Request error: {e}')
        exit()
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def get_player_info(url: str, headers: dict):
    """получаем полные имена игроков и ссылки на их профили из полученной ссылки теннисного матча"""

    players_list = []
    soup = get_soup(url, headers=headers)
    players = soup.find_all("th", class_="plName")
    for player in players:
        name = player.find("a").text
        url = f'https://www.tennisexplorer.com{player.find("a")["href"]}'

        d_players = {
            "name": name,
            "url": url
        }
        players_list.append(d_players)
    return players_list[0], players_list[1]


def get_matches_today(url: str, headers: dict) -> list:
    """Основная функция которая собирает из таблицы матчи на сегодня.
    В ней получаем:
    :arg url: URL страницы
    :arg headers: Headers
    :var match_name: сокращенные имена игроков и есть названия матча
    :var match_url: ссылка на сам матч
    :var match_time: - время проведения матча
    :var p1 и p2 (player1 и 2) - игроки полученные со страницы самого матча их полные имена и ссылки
    """
    soup = get_soup(url, headers=headers)

    today_table = soup.find("div", id="tournamentTabs-1-data").find_all("tr")

    today_matches = []

    for row in today_table:
        if row.find("span", class_="today"): # Ищет матчи на сегодня
            match_name = row.find('a', title="Click for match detail").text.replace("-", "-")
            match_url = f"https://www.tennisexplorer.com{row.find('a', title='Click for match detail')['href']}"
            match_time = row.find("td", class_="first time").text

            player1, player2 = get_player_info(match_url, headers=headers)

            match_info = {
                "m_name": match_name,
                "m_time": match_time,
                "m_url": match_url,
                "p1_full_name": player1.get("name"),
                "p1_url": player1.get("url"),
                "p2_full_name": player2.get("name"),
                "p2_url": player2.get("url")
            }

            today_matches.append(match_info)

    return today_matches

def update_matches_data(url_list: list, headers:dict):
    """
    :param url_list: Список URL
    :param headers:
    :return: Пишет json файлы по турнирам на сегодняшний день
    Внутри запускает парсинг данных, извлекает из url названия турниров и записывает под их именами json
    """
    for url in url_list:
        tennis_tour = re.search(r'([^/]+)/?$', url).group(1).replace("-", "_")
        print(tennis_tour)
        today_matches = get_matches_today(url=url, headers=headers)

        with open(f"data/{tennis_tour}today.json", "w", encoding="utf-8") as file:
            json.dump(today_matches, file, ensure_ascii=False, indent=4)



update_matches_data(url_list=url_list, headers=headers)