from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from model import load_model, predict

# -------------------------------
# FastAPI app setup
# -------------------------------
app = FastAPI(title="Plant Disease Detection")

# Add CORS middleware to allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Load model
model = load_model()


# -------------------------------
# Routes
# -------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with clean state - no results"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": None,
        "error": None,
        "image_path": None
    })


@app.post("/predict", response_class=HTMLResponse)
async def predict_disease(request: Request, file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        upload_dir = "static/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Predict
        with open(file_path, "rb") as img_file:
            result = predict(img_file.read(), model)

        # Prepare context for HTML
        context = {
            "request": request,
            "result": result,
            "image_path": "/" + file_path.replace("\\", "/"),
            "error": None
        }
        return templates.TemplateResponse("index.html", context)

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": None,
            "error": str(e),
            "image_path": None
        })


@app.post("/api/predict")
async def predict_disease_api(file: UploadFile = File(...)):
    """JSON API endpoint for React frontend"""
    try:
        # Read file content
        content = await file.read()
        
        # Predict
        result = predict(content, model)
        
        # Return JSON response
        return JSONResponse({
            "label": result["label"],
            "confidence": result["confidence"],
            "description": result["description"],
            "remedy": result["remedy"]
        })
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e), "message": "Failed to process image"}
        )


@app.get("/about")
async def about():
    return {"message": "Plant Disease Detection API with FastAPI"}
