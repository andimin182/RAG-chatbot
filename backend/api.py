from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.llm import RAG


app = FastAPI(title="Chatbot Agent")

# Initialize your RAG class
rag_agent = RAG()


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
async def query_rag(request: QueryRequest):
    try:
        # Use index to query
        response = rag_agent.query(request.query)
        return {"answer": str(response)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
