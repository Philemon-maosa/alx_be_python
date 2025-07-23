shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display list")
    print("4. Quit")
def add_item(item):
    shopping_list.append(item)
    print(f'"{item}" has been added to your shopping list.')

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'"{item}" has been removed from your shopping list.')
    else:
        print(f'"{item}" is not in your shopping list.')

def display_list():
    if shopping_list:
        print("Your shopping list:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is currently empty.")

# Example usage with a menu
while True:
    print("\nChoose an option:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display list")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == '2':
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == '3':
        display_list()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
