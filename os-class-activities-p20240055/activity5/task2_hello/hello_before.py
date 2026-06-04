import threading
import time
import random
import sys

def process_1():
    time.sleep(random.uniform(0.01, 0.05))
    sys.stdout.write("H")
    sys.stdout.write("E")
    sys.stdout.flush()

def process_2():
    for _ in range(2):
        time.sleep(random.uniform(0.01, 0.05))
        sys.stdout.write("L")
        sys.stdout.flush()

def process_3():
    time.sleep(random.uniform(0.01, 0.05))
    sys.stdout.write("O")
    sys.stdout.flush()

def main():
    print("Task 2A Output: ", end="")
    t1 = threading.Thread(target=process_1)
    t2 = threading.Thread(target=process_2)
    t3 = threading.Thread(target=process_3)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print()

if __name__ == "__main__":
    main()