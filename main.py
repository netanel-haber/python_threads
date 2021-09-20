from requests import Session
from time import time
from functools import partial
from concurrent.futures import ThreadPoolExecutor
import requests


def fetch(i, fetch_object=requests):
    return fetch_object.get(f"https://jsonplaceholder.typicode.com/todos/{i}").json()[
        "id"
    ]


def session_fetcher(session):
    return partial(fetch, fetch_object=session)


NUM_REQUESTS = 100


def getRange():
    return range(1, NUM_REQUESTS + 1)


def naive():
    with Session() as session:
        return list(map(session_fetcher(session), getRange()))


def multi_threaded():
    with ThreadPoolExecutor(max_workers=NUM_REQUESTS) as executor:
        with Session() as session:
            return list(executor.map(session_fetcher(session), getRange()))

def execute(func, name):
    start = time()
    results = func()
    print(f"{name} results:", "\n", results)
    print(f"{name} took {time()-start}s.\n")


if __name__ == "__main__":
    print({"number_of_requests": NUM_REQUESTS})
    execute(naive, "naive")
    execute(multi_threaded, "multi-threaded")
