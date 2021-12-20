class File_manager:
    def read_file(self, file):
        return file.read()

    def add_to_file(self, file, data):
        if not data or type(data) != str:
            raise ValueError("Data must be a string")
        file.write(data)

    def delete_from_file(self, file, data):
        if not data or type(data) != str:
            raise ValueError("Data must be a string")
        file.write(file.read().replace(data, ""))
