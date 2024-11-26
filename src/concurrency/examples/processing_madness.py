"""
Multiprocessing is suitable for CPU-bound tasks, where the program spends most of its time performing computations.
This example demonstrates how to use the multiprocessing module to parallelize the computation of fibonacci numbers.
"""

import time
from multiprocessing import Pool


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def parallel(numbers: list[int]) -> list[int]:
    with Pool(processes=2) as pool:
        results = pool.map(fibonacci, numbers)
    return results


def sequential(numbers: list[int]) -> list[int]:
    return [fibonacci(n) for n in numbers]


def main() -> None:
    numbers = list(range(35, 40))

    print("Sequential execution:")
    start_time = time.time()
    sequential_results = sequential(numbers)
    sequential_time = time.time() - start_time
    print(f"Results: {sequential_results}")
    print(f"Time taken (sequential): {sequential_time:.2f} seconds\n")

    print("Parallel execution:")
    start_time = time.time()
    parallel_results = parallel(numbers)
    parallel_time = time.time() - start_time
    print(f"Results: {parallel_results}")
    print(f"Time taken (parallel): {parallel_time:.2f} seconds")


if __name__ == "__main__":
    main()
