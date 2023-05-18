from fastapi import FastAPI
from transformers import AutoFeatureExtractor, AutoModelForObjectDetection

app = FastAPI()

extractor = AutoFeatureExtractor.from_pretrained("TahaDouaji/detr-doc-table-detection")

model = AutoModelForObjectDetection.from_pretrained("TahaDouaji/detr-doc-table-detection")


@app.post("/predict/")
def predict():
    # Code to handle the prediction logic using TahaDouaji/detr-doc-table-detection model
    # ...
    # Return the prediction response
    return {"result": "Prediction result"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
