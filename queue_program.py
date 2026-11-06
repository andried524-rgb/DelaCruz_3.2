"""Assessment 3.2 - Dynamic QUEUE (FIFO) program (Last name: DELA CRUZ)"""

from collections import deque

LAST_NAME = "DELA CRUZ"


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, value):
        self.items.append(value)
        print(f"Enqueued {value}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty (underflow).")
            return None
        value = self.items.popleft()
        print(f"Dequeued {value}")
        return value

    def front(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f"Front: {self.items[0]}")

    def display(self):
        if self.is_empty():
            print("EMPTY")
        else:
            print("FRONT -> " + " -> ".join(self.items) + " <- REAR")


def demo(q):
    print(f"\n--- Enqueuing letters of {LAST_NAME} ---")
    for ch in LAST_NAME.replace(" ", ""):
        q.enqueue(ch)
    q.display()
    print("\n--- Dequeuing until empty ---")
    while not q.is_empty():
        q.dequeue()
    q.display()


def main():
    q = Queue()
    while True:
        print("\n===== QUEUE MENU (FIFO) =====")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Show front")
        print("4. Display queue")
        print("5. Run demo (DELA CRUZ)")
        print("6. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            value = input("Enter value: ").strip().upper()
            if value:
                q.enqueue(value)
        elif choice == "2":
            q.dequeue()
        elif choice == "3":
            q.front()
        elif choice == "4":
            q.display()
        elif choice == "5":
            demo(q)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
