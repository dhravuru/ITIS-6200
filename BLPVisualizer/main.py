

from blpModel import BLPSystem


def setup_system():

    system = BLPSystem()

    system.add_subject("Alice", "S", "U")
    system.add_subject("Bob", "C", "C")
    system.add_subject("Eve", "U", "U")

    system.add_object("pub.txt", "U")
    system.add_object("emails.txt", "C")
    system.add_object("username.txt", "S")
    system.add_object("password.txt", "TS")


    print("[System] Initalizing Default State...")

    return system


while True:

    print("\n===================================")
    print("Bell-LaPadula (BLP) Simulator CLI")
    print("===================================\n")


    print("\nOptions:")
    print("  [1-18] Run a specific test case (1 to 18)")
    print("  [A] Run all test cases sequentially")
    print("  [Q] Quit\n")


    menu_choice = input("Enter choice: ")
    menu_choice = menu_choice.strip()

    # Test cases

    if (menu_choice == "1"):
        print("\n========== CASE 1 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")

    elif (menu_choice == "2"):
        print("\n========== CASE 2 ==========\n")
        system = setup_system()
        system.read("Alice", "password.txt")

    elif (menu_choice == "3"):
        print("\n========== CASE 3 ==========\n")
        system = setup_system()
        system.read("Eve", "pub.txt")

    elif (menu_choice == "4"):
        print("\n========== CASE 4 ==========\n")
        system = setup_system()
        system.read("Eve", "emails.txt")

    elif (menu_choice == "5"):
        print("\n========== CASE 5 ==========\n")
        system = setup_system()
        system.read("Bob", "password.txt")

    elif (menu_choice == "6"):
        print("\n========== CASE 6 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")
        system.write("Alice", "pub.txt")

    elif (menu_choice == "7"):
        print("\n========== CASE 7 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")
        system.write("Alice", "password.txt")

    elif (menu_choice == "8"):
        print("\n========== CASE 8 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")
        system.write("Alice", "emails.txt")
        system.read("Alice", "username.txt")
        system.write("Alice", "emails.txt")

    elif (menu_choice == "9"):
        print("\n========== CASE 9 ==========\n")
        system = setup_system()
        system.read("Alice", "username.txt")
        system.write("Alice", "emails.txt")
        system.read("Alice", "password.txt")
        system.write("Alice", "password.txt")

    elif (menu_choice == "10"):
        print("\n========== CASE 10 ==========\n")
        system = setup_system()
        system.read("Alice", "pub.txt")
        system.write("Alice", "emails.txt")
        system.read("Bob", "emails.txt")

    elif (menu_choice == "11"):
        print("\n========== CASE 11 ==========\n")
        system = setup_system()
        system.read("Alice", "pub.txt")
        system.write("Alice", "username.txt")
        system.read("Bob", "username.txt")

    elif (menu_choice == "12"):
        print("\n========== CASE 12 ==========\n")
        system = setup_system()
        system.read("Alice", "pub.txt")
        system.write("Alice", "password.txt")
        system.read("Bob", "password.txt")

    elif (menu_choice == "13"):
        print("\n========== CASE 13 ==========\n")
        system = setup_system()
        system.read("Alice", "pub.txt")
        system.write("Alice", "emails.txt")
        system.read("Eve", "emails.txt")

    elif (menu_choice == "14"):
        print("\n========== CASE 14 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")
        system.write("Alice", "pub.txt")
        system.read("Eve", "pub.txt")

    elif (menu_choice == "15"):
        print("\n========== CASE 15 ==========\n")
        system = setup_system()
        system.subjects["Alice"].set_level("S")
        system.read("Alice", "username.txt")

    elif (menu_choice == "16"):
        print("\n========== CASE 16 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")
        system.subjects["Alice"].set_level("U")
        system.write("Alice", "pub.txt")
        system.read("Eve", "pub.txt")

    elif (menu_choice == "17"):
        print("\n========== CASE 17 ==========\n")
        system = setup_system()
        system.read("Alice", "username.txt")
        system.subjects["Alice"].set_level("C")
        system.write("Alice", "emails.txt")
        system.read("Eve", "emails.txt")

    elif (menu_choice == "18"):
        print("\n========== CASE 18 ==========\n")
        system = setup_system()
        system.read("Eve", "pub.txt")
        system.read("Eve", "emails.txt")

    elif (menu_choice.upper() == "A"):
        print("\n========== CASE 1 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")

        print("\n========== CASE 2 ==========\n")
        system = setup_system()
        system.read("Alice", "password.txt")

        print("\n========== CASE 3 ==========\n")
        system = setup_system()
        system.read("Eve", "pub.txt")

        print("\n========== CASE 4 ==========\n")
        system = setup_system()
        system.read("Eve", "emails.txt")

        print("\n========== CASE 5 ==========\n")
        system = setup_system()
        system.read("Bob", "password.txt")

        print("\n========== CASE 6 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")
        system.write("Alice", "pub.txt")

        print("\n========== CASE 7 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")
        system.write("Alice", "password.txt")

        print("\n========== CASE 8 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")
        system.write("Alice", "emails.txt")
        system.read("Alice", "username.txt")
        system.write("Alice", "emails.txt")

        print("\n========== CASE 9 ==========\n")
        system = setup_system()
        system.read("Alice", "username.txt")
        system.write("Alice", "emails.txt")
        system.read("Alice", "password.txt")
        system.write("Alice", "password.txt")

        print("\n========== CASE 10 ==========\n")
        system = setup_system()
        system.read("Alice", "pub.txt")
        system.write("Alice", "emails.txt")
        system.read("Bob", "emails.txt")

        print("\n========== CASE 11 ==========\n")
        system = setup_system()
        system.read("Alice", "pub.txt")
        system.write("Alice", "username.txt")
        system.read("Bob", "username.txt")

        print("\n========== CASE 12 ==========\n")
        system = setup_system()
        system.read("Alice", "pub.txt")
        system.write("Alice", "password.txt")
        system.read("Bob", "password.txt")

        print("\n========== CASE 13 ==========\n")
        system = setup_system()
        system.read("Alice", "pub.txt")
        system.write("Alice", "emails.txt")
        system.read("Eve", "emails.txt")

        print("\n========== CASE 14 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")
        system.write("Alice", "pub.txt")
        system.read("Eve", "pub.txt")

        print("\n========== CASE 15 ==========\n")
        system = setup_system()
        system.subjects["Alice"].set_level("S")
        system.read("Alice", "username.txt")

        print("\n========== CASE 16 ==========\n")
        system = setup_system()
        system.read("Alice", "emails.txt")
        system.subjects["Alice"].set_level("U")
        system.write("Alice", "pub.txt")
        system.read("Eve", "pub.txt")

        print("\n========== CASE 17 ==========\n")
        system = setup_system()
        system.read("Alice", "username.txt")
        system.subjects["Alice"].set_level("C")
        system.write("Alice", "emails.txt")
        system.read("Eve", "emails.txt")

        print("\n========== CASE 18 ==========\n")
        system = setup_system()
        system.read("Eve", "pub.txt")
        system.read("Eve", "emails.txt")


    elif (menu_choice.upper() == "Q"):
        print("Exiting BLP Visualizer...")
        break

    else:
        print("Invalid input. Please try again.")