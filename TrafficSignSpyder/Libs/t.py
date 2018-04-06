# -*- coding: utf-8 -*-

import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup
from urllib.request import urljoin
import re
import multiprocessing as mp

async def job(t):
    pass

async def func(loop):
    tasks = [loop.create_task(job(t))]
    await asyncio.wait(tasks)

def Main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(func(loop))
    loop.close()