"""Assessment 3.2 - Dynamic STACK (LIFO) program (Last name: DELA CRUZ)"""

LAST_NAME = "DELA CRUZ"


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, value):
        self.items.append(value)
        print(f"Pushed {value}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty (underflow).")
            return None
        value = self.items.pop()
        print(f"Popped {value}")
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print(f"Top: {self.items[-1]}")

    def display(self):
        if self.is_empty():
            print("EMPTY")
        else:
            print("Top to bottom:", ", ".join(reversed(self.items)))


def demo(st):
    print(f"\n--- Pushing letters of {LAST_NAME} ---")
    for ch in LAST_NAME.replace(" ", ""):
        st.push(ch)
    st.display()
    print("\n--- Popping until empty ---")
    while not st.is_empty():
        st.pop()
    st.display()


def main():
    st = Stack()
    while True:
        print("\n===== STACK MENU (LIFO) =====")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display (top to bottom)")
        print("5. Run demo (DELA CRUZ)")
        print("6. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            value = input("Enter value: ").strip().upper()
            if value:
                st.push(value)
        elif choice == "2":
            st.pop()
        elif choice == "3":
            st.peek()
        elif choice == "4":
            st.display()
        elif choice == "5":
            demo(st)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
