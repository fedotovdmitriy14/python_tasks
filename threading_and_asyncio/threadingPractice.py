import threading
import time

start = time.perf_counter()

def sleep(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    print("Done")

threads = []

for _ in range(10):
    t = threading.Thread(target=sleep, args=[1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(start-finish)