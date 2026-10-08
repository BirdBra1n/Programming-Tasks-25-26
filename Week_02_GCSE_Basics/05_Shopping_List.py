"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def create_shopping_list():
    shopping_list = []
    print("Enter items to add to your shopping list (Type 'DONE' when finished):")
    
    while True:
        item = input("> ").strip()
        if item.upper() == "DONE":
            print("\n")
            break
        
        if item != "":
            shopping_list.append(item)
        else:
            print("Item cannot be blank.")
            
    return shopping_list


def display_list(shopping_list):
    if not shopping_list:
        print("[Your list is currently empty]")
        return
        
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
    print("-" * 28)
    print("\n")


def edit_shopping_list(shopping_list):
    if not shopping_list:
        return shopping_list

    display_list(shopping_list)
    edit_choice = input("Would you like to edit any item? (y/n): ").strip().lower()
    
    if edit_choice in ["yes", "y"]:
        try:
            item_num = int(input("Enter the number of the item you want to change: "))
            python_index = item_num - 1
            
            if 0 <= python_index < len(shopping_list):
                old_item = shopping_list[python_index]
                new_item = input(f"Enter new name for '{old_item}': ").strip()
                
                if new_item != "":
                    shopping_list[python_index] = new_item
                    print(f"Updated: from '{old_item}' to '{new_item}'.")
                else:
                    print("Invalid input, New name cannot be blank.")
            else:
                print("Invalid item number.")
                
        except ValueError:
            print("Invalid input, enter a valid numerical item number.")
            
    return shopping_list

def main():
    my_list = create_shopping_list()
    display_list(my_list)
    my_list = edit_shopping_list(my_list)
    display_list(my_list)

if __name__ == "__main__":
    main()
