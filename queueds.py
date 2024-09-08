class Queue:
    def __init__(self):
        self.queue = []

   
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to the queue.")

    
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            item = self.queue.pop(0)
            print(f"Dequeued {item} from the queue.")

   
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue:", self.queue)

def queue_operations():
    q = Queue()
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = int(input("Enter the value to enqueue: "))
            q.enqueue(item)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            print("Exiting Queue operations.")
            break
        else:
            print("Invalid choice. Please try again.")


queue_operations()
