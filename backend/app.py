from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Pharmacy Backend Running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
