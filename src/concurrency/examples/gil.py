import threading

x = 0


def increment_global() -> None:
    global x
    x += 1


def task_of_thread() -> None:
    for _ in range(100000):
        increment_global()


def main_task() -> None:
    global x
    x = 0

    t1 = threading.Thread(target=task_of_thread)
    t2 = threading.Thread(target=task_of_thread)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def run_tasks() -> None:
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))


if __name__ == "__main__":
    run_tasks()
