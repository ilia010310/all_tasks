import time

import aiohttp
import asyncio
from bs4 import BeautifulSoup


total = 0

async def get_num_or_search(page: str, session: aiohttp.client.ClientSession) -> None:
    """Получение числа со страницы, и рекурсивный поиск страниц с числами"""
    global total
    async with session.get(page) as response:
        text = await response.text()
        soup = BeautifulSoup(text, 'html.parser')
        number_tag = soup.find('p', {'id': 'number'})
        links = soup.find_all('a', {'class': 'link'})
        if number_tag:
            total += (int(number_tag.text))
        if links:
            tasks = []
            for link in links:
                tasks.append(asyncio.create_task
                             (get_num_or_search('/'.join(page.split('/')[:-1]) + '/' + str(link).split('"')[3],
                                                session)))
            await asyncio.gather(*tasks)





async def main():
    """Запуск функции и замер времени работы программы"""
    stat = time.monotonic()
    page = 'https://asyncio.ru/zadachi/3/index.html'
    async with aiohttp.ClientSession() as session:
        await asyncio.create_task(get_num_or_search(page, session))
    print(f'Воемя выполнения программы: {time.monotonic() - stat}')
    print(total)


asyncio.run(main())
