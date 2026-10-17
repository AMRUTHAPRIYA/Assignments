# list_manager.py
# A simple menu-driven program to manage a list of numbers safely

def manage_list():
    # Create an empty list to store our numbers
    numbers = []
    
    # Use a while loop to keep showing the menu until the user quits
    while True:
        print("\n--- List Manager Menu ---")
        print("(a) Add a number")
        print("(b) Remove a number")
        print("(c) Display the list")
        print("(d) Quit")
        
        # Get the user's choice and convert it to lowercase
        choice = input("Choose an option (a/b/c/d): ").strip().lower()
        
        # Option A: Add a number to the list
        if choice == 'a':
            try:
                # Ask user for a number and turn it into an integer
                val = int(input("Enter an integer to add: "))
                numbers.append(val)
                print(f"Successfully added {val}.")
            except ValueError:
                # Catch the error if they type letters instead of numbers
                print("Error: Please enter a valid integer.")
                
        # Option B: Remove a number by index
        elif choice == 'b':
            if not numbers:
                print("The list is currently empty. Nothing to remove.")
                continue
            try:
                # Ask user for the index position they want to delete
                index = int(input(f"Enter index to remove (0 to {len(numbers)-1}): "))
                removed = numbers.pop(index)
                print(f"Successfully removed {removed} from index {index}.")
            except ValueError:
                print("Error: Please enter a valid integer for the index.")
            except IndexError:
                print("Error: Invalid index! That position doesn't exist in the list.")
                
        # Option C: Show the current list
        elif choice == 'c':
            print(f"Current List: {numbers}")
            
        # Option D: Exit the program
        elif choice == 'd':
            print("Exiting List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 'a', 'b', 'c', or 'd'.")

if __name__ == "__main__":
    manage_list()