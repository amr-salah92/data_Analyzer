from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict(data: dict):
    # Placeholder for prediction logic
    return {"prediction": "result"}