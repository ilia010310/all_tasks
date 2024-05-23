import asyncio
import time

import aiohttp
from bs4 import BeautifulSoup

total = 0


async def pars_page(page: str, session: aiohttp.client.ClientSession) -> None:
    """Функция отправляет GET запрос на страницу и парсит ее, получает число в тегах <p>
    с di=number и прибавляет его к глобальной переменной total"""
    global total
    async with session.get(page) as response:
        text = await response.text()
        soup = BeautifulSoup(text, 'html.parser')
        p_tags = soup.find('p', id='number').text
        total += int(p_tags)


async def get_somthing(page: str, session: aiohttp.client.ClientSession) -> None:
    """Функция отправляет GET запрос на страницу с текстом и получает каждую строку из него,
    после чего подставляет ее в url"""
    async with session.get(page) as response:
        text = await response.text()
        tasks = []
        for num_page in text.split():
            final_page = f"https://asyncio.ru/zadachi/2/html/{num_page}.html"
            tasks.append(asyncio.create_task(pars_page(final_page, session)))
        await asyncio.gather(*tasks)


async def main():
    """Открывает сессию подключения aiohttp, выполняет запрос на сраницу
    и засекает время работы всей программы"""
    stat = time.monotonic()
    async with aiohttp.ClientSession() as session:
        page = f"https://asyncio.ru/zadachi/2/problem_pages.txt"
        await asyncio.create_task(get_somthing(page, session))
    print(f'Время выполнения программы: {time.monotonic() - stat}')
    print(total)


asyncio.run(main())
