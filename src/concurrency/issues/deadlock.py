import time
from multiprocessing import Lock, Process
from typing import Any


def task(lock1: Any, lock2: Any) -> None:
    print("Task started")
    with lock1:
        time.sleep(0.1)
        print(f"Lock {lock1} acquired")
        print(f"Waiting for lock {lock2}")
        with lock2:
            # This code will never be executed
            print("Lock {lock2} acquired")


def main() -> None:
    lock_a = Lock()
    lock_b = Lock()

    p1 = Process(target=task, args=(lock_a, lock_b))
    p2 = Process(target=task, args=(lock_b, lock_a))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    # Процессы зависнут из-за deadlock


if __name__ == "__main__":
    main()
