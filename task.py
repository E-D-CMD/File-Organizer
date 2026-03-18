from controller import controller

def main():
    directory = input("Enter the directory to organize: ")
    ctrl = controller(directory)

    print("1: list_files")
    print("2: Organise_files")
    choice = input("Choose an option: ")

    if choice == "1":
        ctrl.show_files()
    elif choice == "2":
        ctrl.organizer_files()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
