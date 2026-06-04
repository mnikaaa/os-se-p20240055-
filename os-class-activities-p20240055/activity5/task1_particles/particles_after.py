import threading
import time
import random
import sys

BUFFER_CAPACITY = 100 
buffer = []
produced_counter = 0
packaged_counter = 0
running = True

# Semaphores protect the spaces, items, and array adjustments
empty_pairs = threading.Semaphore(50) 
full_pairs = threading.Semaphore(0)   
mutex = threading.Semaphore(1)        

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

        empty_pairs.acquire()
        mutex.acquire()

        buffer.append(p1)
        buffer.append(p2)
        produced_counter += 1

        mutex.release()
        full_pairs.release()
        time.sleep(random.uniform(0.01, 0.05))

def consumer():
    global packaged_counter, running
    while running:
        full_pairs.acquire()
        mutex.acquire()

        p1 = buffer.pop(0)
        p2 = buffer.pop(0)

        if p1.machine_id != p2.machine_id or p1.pair_id != p2.pair_id:
            print("Pairs are incorrect")
            running = False
            mutex.release()
            sys.exit(1)

        packaged_counter += 1
        print(f"Produced pairs: {produced_counter} | Packaged pairs: {packaged_counter} | Buffer particles: {len(buffer)}")
        
        mutex.release()
        empty_pairs.release()
        time.sleep(random.uniform(0.01, 0.02))

def main():
    print("Starting Task 1B: After Semaphores (Press Ctrl+C to stop)...")
    try:
        for i in range(3):
            t = threading.Thread(target=producer, args=(i+1,))
            t.daemon = True
            t.start()
        c_thread = threading.Thread(target=consumer)
        c_thread.daemon = True
        c_thread.start()
        while running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()