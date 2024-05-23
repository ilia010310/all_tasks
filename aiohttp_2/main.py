import asyncio
import time

import aiohttp
from bs4 import BeautifulSoup

total = 0


async def pars_page(page, session):
    global total
    async with session.get(page) as response:
        text = await response.text()
        soup = BeautifulSoup(text, 'html.parser')
        p_tags = soup.find('p', id='number').text
        total += int(p_tags)


async def get_somthing(page, session):
    async with session.get(page) as response:
        text = await response.text()
        tasks = []
        for num_page in text.split():
            final_page = f"https://asyncio.ru/zadachi/2/html/{num_page}.html"
            tasks.append(asyncio.create_task(pars_page(final_page, session)))
        await asyncio.gather(*tasks)


async def main():
    stat = time.monotonic()
    async with aiohttp.ClientSession() as session:
        page = f"https://asyncio.ru/zadachi/2/problem_pages.txt"
        await asyncio.create_task(get_somthing(page, session))
    print(f'Время выполнения программы: {time.monotonic() - stat}')
    print(total)


asyncio.run(main())
