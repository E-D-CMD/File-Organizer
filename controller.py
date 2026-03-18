from model import Organizer
from views import view

class controller:
    def __init__(self, directory):
        self.model = Organizer(directory)
        self.view = view()

    def show_files(self):
        files = self.model.list_files()
        self.view.display_file(files)

    def organizer_files(self):
        self.model.organizer_files()
        self.view.display_message("Files have been organised.")

