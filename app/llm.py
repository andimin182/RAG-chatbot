from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
import os
from app.vector_db import Storage

# Instantiate the llm model from hugging face
hf_token = os.getenv("HF_TOKEN")


class RAG():
    def __init__(self, model: str = "Qwen/Qwen2.5-Coder-32B-Instruct", storage: Storage = Storage()):
        self.model = model
        self.index = storage.index_data()
        self.llm = HuggingFaceInferenceAPI(
            model_name=self.model,
            temperature=0.3,
            max_tokens=100,
            token=hf_token,
            provider="auto",
            system_prompt="You are a jop application assistant and you have expertise in Recrutement."
        )
        # Init the retrievers (in this case only one) with the choosen llm
        self.query_engine = self.index.as_query_engine(llm=self.llm)

    def query(self, query: str):
        return self.query_engine.query(query)
