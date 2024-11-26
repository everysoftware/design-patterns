"""
Multiprocessing is also can be used for I/O-bound tasks, where the program spends most of its time waiting for
I/O operations to complete. However, it does not make sense to this since it's kinda overkill for I/O-bound tasks.
"""

import multiprocessing
import time


def compute_square(number: int) -> int:
    print(
        f"Process {multiprocessing.current_process().name} is processing number {number}"
    )
    time.sleep(2)

    return number * number


def sequential(numbers: list[int]) -> None:
    # Sequential processing
    start = time.perf_counter()
    numbers = [compute_square(number) for number in numbers]
    finish = time.perf_counter()

    print(f"Squares of numbers: {numbers}")
    print(f"Sequential processing time: {finish - start} seconds")


def parallel(numbers: list[int]) -> None:
    # Parallel processing
    start = time.perf_counter()
    with multiprocessing.Pool(processes=5) as pool:
        results = pool.map(compute_square, numbers)
    finish = time.perf_counter()

    print(f"Squares of numbers: {results}")
    print(f"Parallel processing time: {finish - start} seconds")


def main() -> None:
    numbers = [1, 2, 3, 4, 5]
    sequential(numbers)
    parallel(numbers)


if __name__ == "__main__":
    main()
