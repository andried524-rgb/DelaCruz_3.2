"""Assessment 3.2 - Dynamic ARRAY program (Last name: DELA CRUZ)"""

LAST_NAME = "DELA CRUZ"


def display(arr):
    print("Array:", arr if arr else "[] (empty array)")


def insert(arr, value):
    arr.append(value)
    print(f"Appended {value}")


def delete(arr, value=None):
    if not arr:
        print("Array is empty. Nothing to remove.")
        return
    if value is None:  # remove last element
        print(f"Removed {arr.pop()}")
    elif value in arr:
        arr.remove(value)
        print(f"Removed {value}")
    else:
        print(f"{value} not found in the array.")


def demo(arr):
    letters = LAST_NAME.replace(" ", "")
    print(f"\n--- Inserting letters of {LAST_NAME} ---")
    for ch in letters:
        insert(arr, ch)
    display(arr)
    print("\n--- Removing letters one by one ---")
    while arr:
        print(f"Removed {arr.pop(0)}")
    display(arr)


def main():
    arr = []
    while True:
        print("\n===== ARRAY MENU =====")
        print("1. Insert (append) an element")
        print("2. Delete an element (by value)")
        print("3. Delete last element")
        print("4. Display array")
        print("5. Run demo (DELA CRUZ)")
        print("6. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            value = input("Enter value: ").strip().upper()
            if value:
                insert(arr, value)
        elif choice == "2":
            delete(arr, input("Enter value to remove: ").strip().upper())
        elif choice == "3":
            delete(arr)
        elif choice == "4":
            display(arr)
        elif choice == "5":
            demo(arr)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
