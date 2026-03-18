import os
import shutil

class Organizer:
    def __init__(self, dictionary):
        self.directory = dictionary

    def list_files(self):
        return os.listdir(self.directory)

    def move_file(self, file_name, target_directory):
        source_path = os.path.join(self.directory, file_name)

        target_path = os.path.join(target_directory, file_name)
        shutil.move(source_path, target_path)

    def organizer_files(self):
        for file_name in self.list_files():
            if file_name.endswith("txt"):
               self.move_file(file_name, os.path.join(self.directory, "TextFiles"))
            elif file_name.endswith(".jpg"):
                 self.move_file(file_name, os.path.join(self.directory, "Images"))

        
