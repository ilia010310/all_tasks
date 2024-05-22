import asyncio
import time
import aiohttp

status_codes = []


async def get_page(
        page_num: int,
        session: aiohttp.client.ClientSession,
        semaphore: asyncio.locks.Semaphore
) -> None:
    global status_codes
    async with semaphore, session.get(f"https://asyncio.ru/zadachi/5/{page_num}.html") as response:
        status_codes.append(int(response.status))
        print(f'Запрос на страницу: {page_num}, вернул статус: {response.status}')


async def main():
    semaphore = asyncio.Semaphore(100)
    start = time.monotonic()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 1001):
            tasks.append(asyncio.create_task(get_page(i, session, semaphore)))

        await asyncio.gather(*tasks)
    print(sum(status_codes))
    print(f'Время работы программы: {time.monotonic() - start}')


if __name__ == '__main__':
    asyncio.run(main())
