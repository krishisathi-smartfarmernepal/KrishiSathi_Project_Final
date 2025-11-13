# KrishiSathi Project Final

A modern, AI-powered agriculture platform designed to empower farmers and streamline crop management. KrishiSathi combines advanced plant disease detection, real-time farmer support, and robust admin tools into a single, easy-to-use solution. Harnessing the power of machine learning and cloud technologies, KrishiSathi helps users diagnose crop issues, access expert advice, and manage agricultural activities efficiently—all through a beautiful, intuitive web interface.

---

## Features

- Crop disease detection using AI (FastAPI + PyTorch)
- Farmer dashboard, scan history, and chatbot
- Admin dashboard for managing farmers, issues, subsidies, and market prices
- Secure authentication (JWT)
- Image upload and preview
- Modern UI with Tailwind CSS

---

## Project Structure

```
project final/
│
├── backend/                # Node.js/Express API (MongoDB)
│   ├── models/             # Mongoose models
│   ├── routes/             # API routes (auth, farmer, admin, etc.)
│   ├── uploads/            # Uploaded images
│   ├── server.js           # Express server entry
│   └── package.json        # Backend dependencies
│
├── src/
│   ├── components/         # React components
│   ├── contexts/           # React context providers
│   ├── pages/              # React pages (farmer, admin, auth)
│   ├── crop_disease_detection/ # Python FastAPI AI backend
│   │   ├── app.py, main.py, model.py, disease_info.py
│   │   ├── requirements.txt, Dockerfile
│   │   ├── static/uploads/ # Sample images
│   │   └── templates/      # Jinja2 HTML templates
│   ├── App.tsx, main.tsx   # React app entry
│   └── index.css           # Global styles
│
├── package.json            # Frontend dependencies
├── tailwind.config.js      # Tailwind CSS config
├── vite.config.ts          # Vite config
└── README.md               # Project documentation
```

---

## Prerequisites

- Node.js (v18+ recommended)
- Python 3.10+
- MongoDB (local or cloud)
- (Optional) Docker for Python backend

---

## Setup & Run Instructions

### 1. Backend (Node.js/Express)

```bash
cd backend
npm install
# Create a .env file with your MongoDB URI:
# MONGO_URI=mongodb://localhost:27017/krishisathi
npm run dev
```
Server runs on `http://localhost:5000`

---

### 2. Frontend (React)

```bash
npm install
npm run dev
```
Frontend runs on `http://localhost:5173`

---

### 3. AI Crop Disease Detection (Python/FastAPI)

#### Option A: Local Python

```bash
cd src/crop_disease_detection
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```
API runs on `http://localhost:8000/api/predict`

#### Option B: Docker

```bash
cd src/crop_disease_detection
docker build -t crop-disease-ai .
docker run -p 8000:8000 crop-disease-ai
```

---

## Usage

- Register/login as a farmer or admin
- Farmers can upload crop images for disease detection, view scan history, and chat
- Admins can manage farmers, issues, subsidies, and market prices

---

## Contributing

Feel free to open issues or pull requests for improvements!