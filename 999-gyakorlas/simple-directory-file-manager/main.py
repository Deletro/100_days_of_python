from maindrive import MainDrive

maindrive = MainDrive()

while True:
    print("Welcome to the File Manager 2000")
    print("-------------------------")
    user_choice = input(
        "Create Library - 'CL'\nCreate File - 'CF'\nList Libraries - 'LL'\nList Libraries and Files - 'LE'\nOpen Library - 'OL'\nRename Library - 'RL'\nExit - 'X'\n-------------------------\n: "
    ).lower()
    print("-------------------------")
    if user_choice == "x":
        print("Closing File Manager 2000...........")
        break
    elif user_choice == "rl":
        lib_name = input("Which library?: ")
        print("-------------------------")
        exist_lib = maindrive.library_checker(lib_name)
        if exist_lib:
            new_lib_name = input("New Library name?: ")
            print("-------------------------")
            another_exist_lib = maindrive.library_checker(new_lib_name)
            if another_exist_lib:
                print(f"This Library name is already exists: '{new_lib_name}'")
                print("-------------------------")
            else:
                renaming_lib = maindrive.founded_library(lib_name)
                renaming_lib.rename_library(new_lib_name)
        else:
            print(f"Unexistant library: '{lib_name}'")
            print("-------------------------")
    elif user_choice == "le":
        print("Libraries and their associated files:")
        maindrive.list_libs_and_files()
        print("-------------------------")
    elif user_choice == "cl":
        lib_name = input("Library name?: ")
        print("-------------------------")
        exist_lib = maindrive.library_checker(lib_name)
        if exist_lib != True:
            maindrive.create_library(lib_name)
            print(f"Library '{lib_name}' created.")
            print("-------------------------")
        else:
            print(f"This Library is already exists: '{lib_name}'")
            print("-------------------------")
    elif user_choice == "cf":
        lib_name = input("In which library?: ")
        print("-------------------------")
        library = maindrive.library_checker(lib_name)
        if library:
            exist_lib = maindrive.founded_library(lib_name)
            filename = input("Name of the file?\n: ")
            print("-------------------------")
            extension = input("Extension?\n: ")
            print("-------------------------")
            exist_file = exist_lib.create_file(filename, extension)
            if exist_file != True:
                exist_lib.create_file(filename, extension)
            else:
                print(f"This File is already exists: '{filename}'")
                print("-------------------------")
        else:
            print(f"Unexistant library: '{lib_name}'")
            print("-------------------------")
    elif user_choice == "ll":
        does_lib_exist = maindrive.no_library_checker()
        if does_lib_exist:
            print("Libraries:")
            maindrive.list_libraries()
            print("-------------------------")
        else:
            print("There is no Library yet.")
            print("-------------------------")
    elif user_choice == "ol":
        lib_name = input("Which library?: ")
        print("-------------------------")
        if maindrive.library_checker(lib_name):
            library = maindrive.founded_library(lib_name)
            while True:
                print(f"Opened library: '{library.library_name}'")
                print("-------------------------")
                user_input = input(
                    "List Files - 'LF'\nCreate File - 'CF'\nRename File - 'RF'\nDelete File - 'DF'\nExit - 'X'\n-------------------------\n: "
                ).lower()
                if user_input == "x":
                    break
                elif user_input == "lf":
                    print("-------------------------")
                    print(f"Lifst of files in '{library.library_name}':")
                    library.list_files()
                    print("-------------------------")
                elif user_input == "cf":
                    filename = input("Name of the file?\n: ")
                    print("-------------------------")
                    extension = input("Extension?\n: ")
                    print("-------------------------")
                    exist_file = library.create_file(filename, extension)
                    if exist_file != True:
                        library.create_file(filename, extension)
                    else:
                        print(f"This File is already exists: '{filename}'")
                        print("-------------------------")
                elif user_input == "rf":
                    filename = input("Name of the file?\n: ")
                    print("-------------------------")
                    file = library.file_searcher(filename)
                    if file != False:
                        new_filename = input("New name of the file?\n: ")
                        print("-------------------------")
                        file.rename_file(new_filename)
                    else:
                        print(f"Unexistant file: '{filename}'")
                        print("-------------------------")
                elif user_input == "df":
                    filename = input("Name of the file you want to delete?\n: ")
                    print("-------------------------")
                    removed_file = library.file_remover(filename)

        else:
            print(f"Unexistant library: '{lib_name}'")
            print("-------------------------")
    else:
        print("Command Not Found")
        print("-------------------------")
