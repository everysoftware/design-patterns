import time
from multiprocessing import Lock, Process
from typing import Any


def long_task(lock: Any) -> None:
    with lock:
        print("Long task starts")
        time.sleep(5)  # Занимаем ресурс на долгое время
        print("Long task ends")


def short_task(lock: Any) -> None:
    with lock:
        print("Short task executed")


def main() -> None:
    lock = Lock()
    processes = [
        Process(target=long_task, args=(lock,)),
        *[Process(target=short_task, args=(lock,)) for _ in range(5)],
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
    # Короткие задачи долго ждут завершения длинной


if __name__ == "__main__":
    main()
