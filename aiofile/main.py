import asyncio
import time
import aiofiles
import aiocsv
import json
import aiofiles.os as aos

semaphore = asyncio.Semaphore(1000)
cars_dict = {}


async def process_file(path):
    global cars
    async with semaphore, aiofiles.open(path, mode='r',
                                        encoding='Windows-1251') as afp:
        print(f"Processing file: {path}")
        reader = aiocsv.AsyncReader(afp, delimiter=';', quotechar='"')
        headers = await reader.__anext__()
        async for row in reader:
            if row[4] == 'Новый':
                cars_dict['Новый'] = cars_dict.get('Новый', 0) + int(row[3])

            elif row[4] == 'Б/У':
                cars_dict['Б/У'] = cars_dict.get('Б/У', 0) + int(row[3])


async def process_directory(path):
    global cars_dict

    tasks = []
    entries = await aos.listdir(path)
    for entry in entries:
        full_path = f"{path}/{entry}"
        if await aos.path.isfile(full_path) and entry.endswith(".csv"):
            tasks.append(asyncio.ensure_future(process_file(full_path)))

        elif await aos.path.isdir(full_path):
            tasks.append(asyncio.ensure_future(process_directory(full_path)))
    await asyncio.gather(*tasks)
    return cars_dict


async def write_to_json(cars: dict, file_name="cars.json"):
    async with aiofiles.open(file_name, mode='w', encoding='utf-8') as afp:
        print(f"Writing to JSON file: {file_name}")
        await afp.write(json.dumps(cars, ensure_ascii=False, indent=4))


async def main():
    start = time.monotonic()
    path = 'auto'
    cars = await process_directory(path)

    await write_to_json(cars)
    end = time.monotonic()
    print(round(end - start, 2))


asyncio.run(main())
