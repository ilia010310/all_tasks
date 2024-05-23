import time
import aiohttp
import asyncio
from bs4 import BeautifulSoup


total = 0
pages_list = []


async def get_length(page: str, session: aiohttp.client.ClientSession, semaphore: asyncio.locks.Semaphor) -> None:
    global total
    async with semaphore, session.head(page) as data:
        if data.status == 200:
            content_length = data.headers.get('Content-Length')
            total += int(content_length)
            print(content_length)
        else:
            print('Error')

async def get_photos(page: str, session: aiohttp.client.ClientSession, semaphore: asyncio.locks.Semaphor) -> None:
    global pages_list
    async with semaphore, session.get(page) as response:
        result = await response.text()
        soup = BeautifulSoup(result, 'html.parser')
        main_tag = soup.find('main')

        img_tags = main_tag.find_all('img')
        for img in img_tags:
            one_photo = page[:-10] + '/' + img.get('src')
            pages_list.append(one_photo)
    await asyncio.gather(*[asyncio.create_task(get_length(page_photo, session, semaphore)) for page_photo in pages_list])


async def main():
    """Запуск функции и замер времени работы программы"""
    stat = time.monotonic()
    semaphore = asyncio.Semaphore(10)
    page = 'https://asyncio.ru/zadachi/4/index.html'
    async with aiohttp.ClientSession() as session:
        await asyncio.create_task(get_photos(page, session, semaphore))
    print(f'Воемя выполнения программы: {time.monotonic() - stat}')
    print(total)


asyncio.run(main())
