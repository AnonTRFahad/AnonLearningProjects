nid_numbers = [1111111111, 2222222222, 3333333333, 4444444444, 5555555555, 6666666666, 7777777777, 8888888888, 9999999999]


def add_number(nid_number):
    try:
        if nid_number not in nid_numbers:
            if len(str(nid_number)) == 10:
                nid_numbers.append(nid_number)
                print("NID number added successfully.")
            else:
                print("NID number must be exactly 10 digits long.")
        else:
            print("NID number already exists.")
    except Exception as e:
        print("An error occurred:", e)


def remove_number(nid_number):
    try:
        if nid_number in nid_numbers:
            nid_numbers.remove(nid_number)
            print("NID number removed successfully.")
        else:
            print("NID number not found.")
    except Exception as e:
        print("An error occurred:", e)


def display_all_numbers():
    try:
        if nid_numbers:
            print("All NID numbers:")
            for nid_number in nid_numbers:
                print(nid_number)
        else:
            print("No NID numbers found.")
    except Exception as e:
        print("An error occurred:", e)


def update_number(old_nid_number, new_nid_number):
    try:
        if old_nid_number in nid_numbers:
            index = nid_numbers.index(old_nid_number)
            nid_numbers[index] = new_nid_number
            print("NID number updated successfully.")
        else:
            print("NID number not found.")
    except Exception as e:
        print("An error occurred:", e)


# Main program
while True:
    try:
        print("\nNID Management System")
        print("1. Add NID number")
        print("2. Remove NID number")
        print("3. Display all NID numbers")
        print("4. Update NID number")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            nid_number = int(input("Enter NID number to add: "))
            add_number(nid_number)
        elif choice == '2':
            nid_number = int(input("Enter NID number to remove: "))
            remove_number(nid_number)
        elif choice == '3':
            display_all_numbers()
        elif choice == '4':
            old_nid_number = int(input("Enter old NID number: "))
            new_nid_number = int(input("Enter new NID number: "))
            update_number(old_nid_number, new_nid_number)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print("An error occurred:", e)
