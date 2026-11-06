"""Assessment 3.2 - Dynamic LINKED LIST program (Last name: DELA CRUZ)"""

LAST_NAME = "DELA CRUZ"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        print(f"Inserted {data}")

    def delete_head(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        print(f"Deleted {self.head.data}")
        self.head = self.head.next

    def delete_value(self, value):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        if self.head.data == value:
            self.delete_head()
            return
        cur = self.head
        while cur.next and cur.next.data != value:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
            print(f"Deleted {value}")
        else:
            print(f"{value} not found.")

    def display(self):
        if self.head is None:
            print("EMPTY")
            return
        parts, cur = [], self.head
        while cur:
            parts.append(cur.data)
            cur = cur.next
        print(" -> ".join(parts) + " -> NULL")


def demo(ll):
    print(f"\n--- Inserting letters of {LAST_NAME} at tail ---")
    for ch in LAST_NAME.replace(" ", ""):
        ll.insert_tail(ch)
    ll.display()
    print("\n--- Deleting from head ---")
    while ll.head:
        ll.delete_head()
    ll.display()


def main():
    ll = LinkedList()
    while True:
        print("\n===== LINKED LIST MENU =====")
        print("1. Insert at tail")
        print("2. Delete from head")
        print("3. Delete by value")
        print("4. Display list")
        print("5. Run demo (DELA CRUZ)")
        print("6. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            value = input("Enter value: ").strip().upper()
            if value:
                ll.insert_tail(value)
        elif choice == "2":
            ll.delete_head()
        elif choice == "3":
            ll.delete_value(input("Enter value to delete: ").strip().upper())
        elif choice == "4":
            ll.display()
        elif choice == "5":
            demo(ll)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
