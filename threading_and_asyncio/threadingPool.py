import concurrent.futures
import time

start = time.perf_counter()

def sleep(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f"done sleeping {seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    sec = [5, 4, 5, 3, 1]
    results = [executor.submit(sleep, sec) for sec in sec]

    # возвращает результаты потоков в том порядке, в котором они были запущены
    # results = executor.map(sleep, sec)
    # for result in results:
    #     print(result)

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(start-finish)