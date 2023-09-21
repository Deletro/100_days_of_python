class File:
    def __init__(self, filename, extension):
        self.filename = filename
        self.extension = extension

    def show_file(self):
        print(f"{self.filename}.{self.extension} - (file)")

    def rename_file(self, new_filename):
        self.filename = new_filename
        print(f"File renamed to: '{self.filename}'.")
