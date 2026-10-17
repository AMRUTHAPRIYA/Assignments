# list_manager.py

def manage_list():
    numbers = []
    
    while True:
        print("\n--- List Manager Menu ---")
        print("(a) Add a number")
        print("(b) Remove a number by index")
        print("(c) Display the list")
        print("(d) Quit")
        
        choice = input("Choose an option (a/b/c/d): ").strip().lower()
        
        if choice == 'a':
            try:
                val = int(input("Enter an integer to add: "))
                numbers.append(val)
                print(f"Successfully added {val}.")
            except ValueError:
                print("Error: Please enter a valid integer.")
                
        elif choice == 'b':
            if not numbers:
                print("The list is currently empty. Nothing to remove.")
                continue
            try:
                index = int(input(f"Enter index to remove (0 to {len(numbers)-1}): "))
                removed = numbers.pop(index)
                print(f"Successfully removed {removed} from index {index}.")
            except ValueError:
                print("Error: Please enter a valid integer for the index.")
            except IndexError:
                print("Error: Invalid index! Index out of range for this list.")
                
        elif choice == 'c':
            print(f"Current List: {numbers}")
            
        elif choice == 'd':
            print("Exiting List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 'a', 'b', 'c', or 'd'.")

if __name__ == "__main__":
    manage_list()
    