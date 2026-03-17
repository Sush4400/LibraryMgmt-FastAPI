from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": True,
        "message": "Libary Management Backend is Running..."
    }