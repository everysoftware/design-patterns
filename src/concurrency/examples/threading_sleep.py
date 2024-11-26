import threading
import time


def compute_square(number: int) -> int:
    print(
        f"Thread {threading.current_thread().name} is processing number {number}"
    )
    time.sleep(2)
    return number * number


def sequential(numbers: list[int]) -> list[int]:
    results = []
    start = time.perf_counter()
    for number in numbers:
        results.append(compute_square(number))
    finish = time.perf_counter()
    print(f"Sequential processing time: {finish - start} seconds")
    return results


def concurrent(numbers: list[int]) -> list[int]:
    threads = []
    results = []

    start = time.perf_counter()
    for number in numbers:
        thread = threading.Thread(
            target=lambda: results.append(compute_square(number))
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    finish = time.perf_counter()
    print(f"Concurrent processing time: {finish - start} seconds")

    return results


def main() -> None:
    numbers = [1, 2, 3, 4, 5]
    sequential(numbers)
    concurrent(numbers)


if __name__ == "__main__":
    main()
