from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model import load_model, predict  # Changed: import predict instead of get_prediction_from_path
import shutil
import os
import logging
from fastapi.middleware.cors import CORSMiddleware

# -------------------------------
# App Setup
# -------------------------------
app = FastAPI(title="Plant Disease Detection API")

# Logger (define early so startup logs can use it)
logger = logging.getLogger("uvicorn")

# Add CORS middleware for development (allow frontend dev server)
app.add_middleware(
    CORSMiddleware,
    # During local development allow all origins to avoid CORS issues from dev servers.
    # For production, replace with specific allowed origins instead of ['*']
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Log CORS configuration at startup (helps verify running process has middleware)
logger.info("CORS middleware configured: allow_origins=[*], allow_methods=[*], allow_headers=[*]")

# Mount static and templates directories
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Upload directory (inside static folder for serving)
UPLOAD_DIR = os.path.join("static", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}


# -------------------------------
# Helper function to validate files
# -------------------------------
def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

try:
    hf_token = os.getenv("HF_TOKEN")  # optional for private HF repo
    model = load_model(token=hf_token)
    logger.info("Model loaded successfully at startup")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    model = None

# -------------------------------
# Routes
# -------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict_disease(request: Request, file: UploadFile = File(...)):
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPG, JPEG, PNG allowed.")
    
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded. Try again later.")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    try:
        # Save uploaded file to static/uploads directory
        with open(file_path, "wb") as buffer:       
            shutil.copyfileobj(file.file, buffer)

        # Get prediction using the predict function from model.py
        with open(file_path, "rb") as img_file:
            result = predict(img_file.read(), model)
        
        # Extract label and confidence from result
        label = result["label"]
        confidence = result["confidence"]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")

    # Return template with prediction and confidence (file stays in static/uploads)
    return templates.TemplateResponse(
    "index.html",
    {
        "request": request,
        "result": {
            "label": label,
            "confidence": confidence,
            "description": result.get("description", ""),
            "remedy": result.get("remedy", "")
        },
        "image_path": f"/static/uploads/{file.filename}"
    }
)

# JSON API endpoint for React/frontend
@app.post("/api/predict")
async def predict_disease_api(file: UploadFile = File(...)):
    if not allowed_file(file.filename):
        return JSONResponse(status_code=400, content={"error": "Invalid file type. Only JPG, JPEG, PNG allowed."})
    if model is None:
        return JSONResponse(status_code=500, content={"error": "Model is not loaded. Try again later."})
    try:
        content = await file.read()
        result = predict(content, model)
        return JSONResponse({
            "label": result["label"],
            "confidence": result["confidence"],
            "description": result.get("description", ""),
            "remedy": result.get("remedy", "")
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e), "message": "Failed to process image"})
