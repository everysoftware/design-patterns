import os
from multiprocessing import Process


def task() -> None:
    while True:
        pass  # Бесконечный цикл, чтобы процесс занимал ресурсы


def main() -> None:
    cpu_count = os.cpu_count()
    assert cpu_count is not None
    processes = [Process(target=task) for _ in range(cpu_count * 2)]

    for p in processes:
        p.start()

    # Ваш компьютер может стать неработоспособным


if __name__ == "__main__":
    main()
