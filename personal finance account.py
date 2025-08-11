def load_history():
    try:
        with open("finance.txt", "r") as file:
            return [line.strip().split(",") for line in file]
    except FileNotFoundError:
        return []

def save_history(history):
    with open("finance.txt", "w") as file:
        for item in history:
            file.write(",".join(item) + "\n")

def add_money(history, amount, note):
    history.append(["add", str(amount), note])
    save_history(history)

def spend_money(history, amount, note):
    history.append(["spend", str(amount), note])
    save_history(history)

def view_total(history):
    total = 0.0
    for entry in history:
        if entry[0] == "add":
            total += float(entry[1])
        elif entry[0] == "spend":
            total -= float(entry[1])
    print(f"\n Total Money: {total:.2f}")

def view_history(history):
    if not history:
        print("\nNo transaction history.")
        return
    print("\n Transaction History:")
    for i, entry in enumerate(history, 1):
        type_str = "Added" if entry[0] == "add" else "Spent"
        print(f"{i}. {type_str} {entry[1]} - {entry[2]}")

def main():
    history = load_history()
    while True:
        print("\n Personal Finance Account ")
        print("1. Add Money")
        print("2. Local Cost")
        print("3. View Total Money")
        print("4. View History")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to add: "))
                note = input("Enter note: ")
                add_money(history, amount, note)
                print("Money added successfully.")
            except ValueError:
                print(" Invalid amount.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to spend: "))
                note = input("Enter note: ")
                spend_money(history, amount, note)
                print(" Expense recorded.")
            except ValueError:
                print(" Invalid amount.")
        elif choice == "3":
            view_total(history)
        elif choice == "4":
            view_history(history)
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
