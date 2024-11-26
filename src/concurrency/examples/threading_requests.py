import threading

import requests


def fetch_url(url: str) -> None:
    print(f"Thread {threading.current_thread().name} is fetching {url}")
    response = requests.get(url)
    print(
        f"Thread {threading.current_thread().name} finished fetching {url}, Status Code: {response.status_code}"
    )


def sequential(urls: list[str]) -> None:
    for url in urls:
        fetch_url(url)

    print("All requests finished")


def concurrent(urls: list[str]) -> None:
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads finished")


def main() -> None:
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/1",
    ]
    sequential(urls)
    concurrent(urls)


if __name__ == "__main__":
    main()
