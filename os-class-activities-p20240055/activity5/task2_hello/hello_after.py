import threading
import sys

start_h = threading.Semaphore(1)  
after_e = threading.Semaphore(0)  
after_l1 = threading.Semaphore(0) 
after_l2 = threading.Semaphore(0) 

def process_1():
    start_h.acquire()
    sys.stdout.write("H")
    sys.stdout.write("E")
    sys.stdout.flush()
    after_e.release()

def process_2():
    after_e.acquire()
    sys.stdout.write("L")
    sys.stdout.flush()
    after_l1.release()
    
    after_l1.acquire()
    sys.stdout.write("L")
    sys.stdout.flush()
    after_l2.release()

def process_3():
    after_l2.acquire()
    sys.stdout.write("O")
    sys.stdout.flush()

def main():
    print("Task 2B Output: ", end="")
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