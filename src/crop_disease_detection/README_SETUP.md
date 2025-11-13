# Crop Disease Detection - Setup Instructions

## 🚀 Quick Start

### 1. Install Python Dependencies

```bash
cd src/crop_disease_detection
pip install -r requirements.txt
```

### 2. Run the Python FastAPI Server

```bash
# Make sure you're in the crop_disease_detection directory
python -m uvicorn app:app --reload --port 8000
```

The server will start on: **http://localhost:8000**

### 3. Run the React Frontend

Open another terminal:

```bash
# From project root
npm run dev
```

The React app will run on: **http://localhost:5173**

## 📋 How It Works

1. **Python Backend** (Port 8000):
   - FastAPI server with crop disease detection model
   - Uses ResNet9 architecture with PyTorch
   - Trained on 38 plant disease classes
   - Model weights loaded from HuggingFace

2. **React Frontend** (Port 5173):
   - User uploads crop image
   - Image sent to Python backend via API
   - Results displayed with treatment and prevention info

## 🔗 API Endpoints

- `POST /api/predict` - Upload image and get disease prediction (JSON)
- `POST /predict` - Upload image via HTML form
- `GET /` - HTML interface
- `GET /about` - API information

## 🧪 Testing

1. Start Python server: `uvicorn app:app --reload --port 8000`
2. Start React app: `npm run dev`
3. Navigate to Crop Disease Detection page in the React app
4. Upload a crop/plant image
5. Click "Analyze Image"
6. View results!

## 🔧 Troubleshooting

**Error: "Could not connect to AI model"**
- Make sure Python server is running on port 8000
- Check CORS is enabled in `app.py`
- Verify `requirements.txt` packages are installed

**Error: Model loading failed**
- Check internet connection (model downloads from HuggingFace)
- Verify HuggingFace repo: `kritimbista/my-model-weights`

## 📦 Dependencies

- Python 3.8+
- FastAPI
- PyTorch
- torchvision
- Pillow
- huggingface-hub
- uvicorn

## 🌿 Supported Crops & Diseases

- Apple (Scab, Black rot, Cedar rust, Healthy)
- Blueberry (Healthy)
- Cherry (Powdery mildew, Healthy)
- Corn (Leaf spot, Rust, Blight, Healthy)
- Grape (Black rot, Esca, Leaf blight, Healthy)
- Orange (Citrus greening)
- Peach (Bacterial spot, Healthy)
- Pepper (Bacterial spot, Healthy)
- Potato (Early blight, Late blight, Healthy)
- Tomato (Multiple diseases, Healthy)
- And more...

## 📝 Notes

- Model provides disease descriptions and remedies in Nepali
- Confidence scores are percentage-based
- Severity is automatically determined based on disease type
- For serious issues, always consult agricultural experts
