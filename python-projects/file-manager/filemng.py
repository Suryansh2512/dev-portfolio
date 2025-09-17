import os

def filemngr():
    while True:
        print("\nFile Manager Menu:")
        print("1. Change Directory")
        print("2. List Files")
        print("3. Create Directory")
        print("4. Remove Directory")
        print("5. Exit")
        try:
            todo = int(input("Enter your selection: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if todo == 1:
            x = input("Change directory to?: ").strip()
            m = os.getcwd()
            if x == m:
                print("Already in the same directory.")
            else:
                try:
                    os.chdir(x)
                    print(f"Changed directory to {x}")
                except Exception as e:
                    print(f"Error: {e}")
        elif todo == 2:
            print("Files and directories:", os.listdir())
        elif todo == 3:
            y = input("Enter name of directory to be created: ").strip()
            try:
                os.makedirs(y)
                print(f"Directory '{y}' created.")
            except Exception as e:
                print(f"Error: {e}")
        elif todo == 4:
            z = input("Enter name of directory to be removed: ").strip()
            try:
                os.rmdir(z)
                print(f"Directory '{z}' removed.")
            except Exception as e:
                print(f"Error: {e}")
        elif todo == 5:
            print("Exiting File Manager.")
            break
        else:
            print('Wrong selection')

        v = input("Want to do more? (Y/N): ").strip().upper()
        if v != "Y":
            print("Exiting File Manager.")
            break