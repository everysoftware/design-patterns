import asyncio


async def compute_square(number: int) -> int:
    task = asyncio.current_task()
    assert task is not None
    print(f"Task {task.get_name()} is processing number {number}")
    await asyncio.sleep(2)
    return number * number


async def sequential(numbers: list[int]) -> list[int]:
    results = []
    start = asyncio.get_event_loop().time()
    for number in numbers:
        result = await compute_square(number)
        results.append(result)
    finish = asyncio.get_event_loop().time()
    print(f"Sequential processing time: {finish - start} seconds")
    return results


async def concurrent(numbers: list[int]) -> list[int]:
    start = asyncio.get_event_loop().time()
    tasks = [compute_square(number) for number in numbers]
    results = await asyncio.gather(*tasks)
    finish = asyncio.get_event_loop().time()
    print(f"Concurrent processing time: {finish - start} seconds")
    return results


async def main() -> None:
    numbers = [1, 2, 3, 4, 5]
    print("Running sequentially:")
    await sequential(numbers)
    print("Running concurrently:")
    await concurrent(numbers)


if __name__ == "__main__":
    asyncio.run(main())
