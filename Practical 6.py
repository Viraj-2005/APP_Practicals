import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1: {i}")
        time.sleep(1)

def print_letters():
    for letters in 'abcde':
        print(f"Thread 2: {letters}")
        time.sleep(1.5)

if __name__ == "__main__":
    # Creating threads for each task
    thread1 = threading.Thread(target=print_numbers())
    thread2 = threading.Thread(target=print_letters())

    # Starting the threads
    thread1.start()
    thread2.start()

    # Waiting for both threads to finish
    thread1.join()
    thread2.join()

    print("All tasks completed.")




