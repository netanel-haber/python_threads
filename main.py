import requests
from time import time
from concurrent.futures import ThreadPoolExecutor

NUM_REQUESTS = 5


def url(i):
    return f"https://jsonplaceholder.typicode.com/todos/{i}"


def fetch(i):
    return requests.get(url(i)).json()["id"]


def single_threaded():
    return list(map(fetch, range(1, NUM_REQUESTS + 1)))


def multi_threaded():
    with ThreadPoolExecutor(max_workers=NUM_REQUESTS) as executor:
        return list(executor.map(fetch, range(1, NUM_REQUESTS + 1)))


def execute(func, name):
    start = time()
    results = func()
    print(f"{name} results:", "\n", results)
    print(f"{name} took {time()-start}s.\n")


if __name__ == "__main__":
    print({"number_of_requests": NUM_REQUESTS})
    execute(single_threaded, "single_threaded")
    execute(multi_threaded, "multi-threaded")
