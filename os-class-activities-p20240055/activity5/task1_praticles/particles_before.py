import threading
import time
import random
import sys

BUFFER_CAPACITY = 100
buffer = []
produced_counter = 0
packaged_counter = 0
running = True

class Particle:
    def __init__(self, machine_id, pair_id, type_str):
        self.machine_id = machine_id
        self.pair_id = pair_id
        self.type_str = type_str

    def __str__(self):
        return f"M{self.machine_id}-{self.pair_id}-{self.type_str}"

def producer(machine_id):
    global produced_counter, running
    pair_id = 0
    while running:
        pair_id += 1
        p1 = Particle(machine_id, pair_id, "P1")
        p2 = Particle(machine_id, pair_id, "P2")

        if len(buffer) + 2 > BUFFER_CAPACITY:
            print("\nThe producing machine is broken")
            running = False
            sys.exit(1)

        buffer.append(p1)
        time.sleep(random.uniform(0.001, 0.005)) # Forces a race condition crack
        buffer.append(p2)
        
        produced_counter += 1
        time.sleep(random.uniform(0.01, 0.05))

def consumer():
    global packaged_counter, running
    while running:
        if len(buffer) < 2:
            print("\nThe packaging machine is broken")
            running = False
            sys.exit(1)

        p1 = buffer.pop(0)
        time.sleep(random.uniform(0.001, 0.005))
        p2 = buffer.pop(0)

        if p1.machine_id != p2.machine_id or p1.pair_id != p2.pair_id:
            print(f"\nPairs are incorrect. Discovered: {p1} + {p2}")
            print("Pairs are incorrect")
            running = False
            sys.exit(1)

        packaged_counter += 1
        print(f"Produced pairs: {produced_counter} | Packaged pairs: {packaged_counter} | Buffer particles: {len(buffer)}")
        time.sleep(random.uniform(0.01, 0.03))

def main():
    print("Starting Task 1A: Before Semaphores...")
    threads = []
    for i in range(3):
        t = threading.Thread(target=producer, args=(i+1,))
        threads.append(t)
        t.start()
    c_thread = threading.Thread(target=consumer)
    threads.append(c_thread)
    c_thread.start()

if __name__ == "__main__":
    main()