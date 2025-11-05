from asyncio import gather, create_task, run, sleep
from fake_useragent import UserAgent
from aiohttp import ClientSession
from time import sleep as ssleep
from datetime import datetime

global success_number
success_number = 0

headers = {}
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["cookie"] = "_ga=GA1.2.911762608.1640089286; _gid=GA1.2.1225094414.1640089286; __oagr=true"
headers["sec-ch-ua"] = '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"'
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = "Windows"
headers["sec-fetch-dest"] = "document"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-site"] = "none"
headers["sec-fetch-user"] = "?1"
headers["upgrade-insecure-requests"] = "1"
headers["user-agent"] = UserAgent().random


async def get_user_info(url, unique_id):
    global success_number
    async with ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            date_time = datetime.now().strftime('%d.%m.%Y | %H:%M:%S')
            if response.status == 200:
                success_number += 1
            print(str(date_time) + ' | ' + str(response.status) +
                  ' ID: ' + str(unique_id) + ' SUCCESS: ' + str(success_number))


async def runner():
    min_id = 0
    max_id = 10000
    tasks = []
    chunk = 500
    pended = 0
    for current_id in range(max_id):
        unique_id = min_id + current_id
        url = f'https://lardi-trans.ua/user/{unique_id}/'
        tasks.append(create_task(get_user_info(url, unique_id)))
        if len(tasks) == chunk or pended == max_id:
            await gather(*tasks)
            tasks = []


if __name__ == '__main__':
    run(runner())
