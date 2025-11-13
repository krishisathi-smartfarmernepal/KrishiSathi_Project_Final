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

- **Node.js** (v18+ recommended)
- **Python** 3.10+
- **MongoDB** (local installation with MongoDB Compass or cloud via MongoDB Atlas)
- **Docker** (optional, for containerizing the AI service)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/krishisathi-smartfarmernepal/KrishiSathi_Project_Final.git
cd krishi_sathi
```

### 2. Set Up MongoDB Database

#### Option A: Local MongoDB with Compass (Recommended for Development)

1. **Download and Install MongoDB Community Server**:
   - Go to [MongoDB Download Center](https://www.mongodb.com/try/download/community)
   - Select your OS (Windows) and download the MSI installer
   - Run the installer and follow the setup wizard
   - Choose "Complete" installation

2. **Download and Install MongoDB Compass**:
   - Go to [MongoDB Compass Download](https://www.mongodb.com/try/download/compass)
   - Download and install the GUI tool for managing MongoDB

3. **Start MongoDB Service**:
   - Open Command Prompt as Administrator
   - Run: `net start MongoDB` (or use Windows Services to start it)
   - MongoDB will run on `mongodb://localhost:27017`

4. **Create Database (Optional)**:
   - Open MongoDB Compass
   - Connect to `mongodb://localhost:27017`
   - The database `krishi-sathi-DB` will be created automatically when you first run the app
   - Collections (tables) for farmers, admins, etc. will also be created automatically

#### Option B: MongoDB Atlas (Cloud Database)

1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create a free account and cluster
3. Get your connection string from the "Connect" button
4. It will look like: `mongodb+srv://username:password@cluster.mongodb.net/krishi-sathi-DB`

### 3. Backend Setup

```bash
cd backend
npm install
# Create a .env file with your MongoDB URI:
# MONGO_URI=mongodb://localhost:27017/krishi-sathi-DB
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

## Environment Variables

### Backend (.env in backend/ directory)
Create a `.env` file in the `backend` folder with the following variables:

```env
MONGO_URI=mongodb://localhost:27017/krishi-sathi-DB
JWT_SECRET=your_jwt_secret_here
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_email_password
PORT=5000
```

- `MONGO_URI`: MongoDB connection string (local or Atlas)
- `JWT_SECRET`: Secret key for JWT token generation
- `EMAIL_USER`: Email address for sending notifications
- `EMAIL_PASS`: Email password or app password
- `PORT`: Server port (default: 5000)

### Frontend (.env in root/ directory)
Create a `.env` file in the root directory with:

```env
VITE_CHATBOT_API_KEY=your_chatbot_api_key_here
```

- `VITE_CHATBOT_API_KEY`: API key for the chatbot service (starts with VITE_ for Vite to expose it)

---

## Usage

- Register/login as a farmer or admin
- Farmers can upload crop images for disease detection, view scan history, and chat
- Admins can manage farmers, issues, subsidies, and market prices

---

## Contributing

Feel free to open issues or pull requests for improvements!