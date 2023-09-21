from library import Library


class MainDrive:
    def __init__(self):
        self.list_of_libraries = []

    def create_library(self, lib_name):
        self.list_of_libraries.append(Library(lib_name))

    def list_libraries(self):
        for lib in self.list_of_libraries:
            lib.show_library()

    def founded_library(self, lib_name):
        lib_true = self.library_checker(lib_name)
        if lib_true:
            for lib in self.list_of_libraries:
                if lib.library_name == lib_name:
                    return lib

    def library_checker(self, lib_name):
        for lib in self.list_of_libraries:
            if lib.library_name == lib_name:
                return True
        return False

    def no_library_checker(self):
        for lib in self.list_of_libraries:
            if lib == self.list_of_libraries[0]:
                return True
        return False

    def list_libs_and_files(self):
        for lib in self.list_of_libraries:
            lib.show_library()
            for file in lib.list_of_files:
                file.show_file()
