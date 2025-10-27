#!/bin/bash

# -------------------------------
# Configuration
BACKEND_MODULE="backend.api:app"       # your FastAPI module
BACKEND_PORT=8000
FRONTEND_SCRIPT="frontend/ui.py" # your Streamlit script
FRONTEND_PORT=8501

# -------------------------------
# Run FastAPI backend
echo "Starting FastAPI backend on http://127.0.0.1:$BACKEND_PORT..."
uvicorn $BACKEND_MODULE --reload --port $BACKEND_PORT &

# Save the backend PID to kill later if needed
BACKEND_PID=$!

# Wait a few seconds to make sure backend is up
sleep 3

# -------------------------------
# Run Streamlit frontend
echo "Starting Streamlit frontend on http://127.0.0.1:$FRONTEND_PORT..."
streamlit run $FRONTEND_SCRIPT &

# Save frontend PID
FRONTEND_PID=$!

# -------------------------------
# Wait for processes
echo "Both backend and frontend are running."
echo "Press Ctrl+C to stop."

# Wait for both processes to finish
wait $BACKEND_PID $FRONTEND_PID
