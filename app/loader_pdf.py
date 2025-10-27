from pathlib import Path
import os
from llama_index.readers.file import UnstructuredReader

data_path = str(Path(__file__).resolve().parent.parent / "data/")


class Loader():
    """ This class used to load the PDF files contained in a folder"""

    def __init__(self, folder_path: str = data_path):
        self.folder_path = folder_path
        self.file_list = os.listdir(data_path)
        self.documents = []
        self.load_data()

    def load_data(self):
        loader = UnstructuredReader()
        for file in self.file_list:
            pdf_file = loader.load_data(
                file=(self.folder_path+"/"+file), split_documents=False)

            self.documents.extend(pdf_file)


if __name__ == "__main__":
    print(data_path)
