require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const authRoutes = require('./routes/auth');
const farmerRoutes = require('./routes/farmer');
const passwordRoutes = require('./routes/password');
const adminRoutes = require('./routes/admin');
const issueRoutes = require('./routes/issues');
const subsidyRoutes = require('./routes/subsidy');
const chatRoutes = require('./routes/chat');
const marketRoutes = require('./routes/market');
const diseaseRoutes = require('./routes/disease');
const app = express();
app.use(cors());
app.use(express.json({ limit: '20mb' }));
app.use(express.urlencoded({ limit: '20mb', extended: true }));

mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error(err));

// Serve uploaded files
app.use('/uploads', express.static(require('path').join(__dirname, 'uploads')));



app.use('/api/auth', authRoutes);
app.use('/api/farmer', farmerRoutes);
app.use('/api/password', passwordRoutes);
app.use('/api/admin', adminRoutes);
app.use('/api/issues', issueRoutes);
app.use('/api/subsidy', subsidyRoutes);
app.use('/api/chat', chatRoutes);
app.use('/api/disease', diseaseRoutes);
app.use('/api', marketRoutes);

// Error-handling middleware: logs errors and returns JSON responses
app.use((err, req, res, next) => {
  console.error('Unhandled error:', err);
  // Multer file upload errors
  if (err && err.name === 'MulterError') {
    return res.status(400).json({ message: err.message });
  }
  // Specific rejection from our fileFilter
  if (err && typeof err.message === 'string' && err.message.includes('Only image files are allowed')) {
    return res.status(400).json({ message: err.message });
  }
  const status = err && err.status ? err.status : 500;
  const message = err && err.message ? err.message : 'Internal Server Error';
  res.status(status).json({ message });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
