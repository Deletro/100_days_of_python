from file import File


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.list_of_files = []

    def show_library(self):
        print(f"{self.library_name} - (lib)")

    def list_files(self):
        for file in self.list_of_files:
            file.show_file()

    def create_file(self, filename, extension):
        file_exist = self.file_searcher(filename)
        if file_exist == False:
            self.list_of_files.append(File(filename, extension))
        else:
            return True

    def file_searcher(self, filename):
        for file in self.list_of_files:
            if file.filename == filename:
                return file
        return False

    def file_remover(self, filename):
        file = self.file_searcher(filename)
        if file != False:
            self.list_of_files.remove(file)
            print(f"Deleted file: '{filename}'")
        else:
            print(f"Unexistant file: '{filename}'")

    def rename_library(self, new_library_name):
        self.library_name = new_library_name
        print(f"Library renamed to: '{self.library_name}'.")
