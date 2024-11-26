from multiprocessing import Process, Value
from typing import Any


def increment(counter: Any) -> None:
    for _ in range(1000):
        # Несинхронизированный доступ к разделяемому ресурсу
        counter.value += 1


def main() -> None:
    counter = Value("i", 0)  # Общий разделяемый ресурс

    # Создаём 10 процессов
    processes = [Process(target=increment, args=(counter,)) for _ in range(10)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    # Ожидаемое значение: 10 * 1000 = 10000
    print("Expected:", 10 * 1000)
    print("Actual:", counter.value)  # Итог может быть меньше ожидаемого


if __name__ == "__main__":
    main()
