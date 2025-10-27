from app.loader_pdf import Loader
from pathlib import Path
import os
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage

PERSIST_DIR = str(Path(__file__).resolve().parent.parent / "storage")


class Storage():
    def __init__(self, dir_store: str = PERSIST_DIR, emded_model: str = "BAAI/bge-small-en-v1.5"):
        self.dir_store = dir_store
        self.embed_model = HuggingFaceEmbedding(model_name=emded_model)

    def index_data(self):
        if not os.path.exists(self.dir_store):
            # load the documents and create the index
            loader = Loader()
            documents = loader.documents
            # Create the index
            index = VectorStoreIndex.from_documents(
                documents, embed_model=self.embed_model)
            # store it for later
            index.storage_context.persist(persist_dir=self.dir_store)
            print("Index created from documents!")
        else:
            # load the existing index
            print("Loading existing index...")
            storage_context = StorageContext.from_defaults(
                persist_dir=self.dir_store)
            index = load_index_from_storage(
                storage_context, embed_model=self.embed_model)
            print("Finish!")
        return index


if __name__ == "__main__":
    print(PERSIST_DIR)
