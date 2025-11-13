const express = require('express');
const router = express.Router();
const axios = require('axios');

// Kalimati API endpoint for daily prices in English
const KALIMATI_API_URL = 'https://kalimatimarket.gov.np/api/daily-prices/en';

router.get('/market-prices', async (req, res) => {
  const market = req.query.market;
  if (market !== 'kalimati') {
    return res.status(400).json({ message: 'Only kalimati market is supported.' });
  }
  try {
    // Fetch from Kalimati API
    const response = await axios.get(KALIMATI_API_URL);
    // Only return the 'prices' array to the frontend
    res.json(response.data.prices);
  } catch (err) {
    res.status(500).json({ message: 'Failed to fetch market prices', error: err.message });
  }
});

module.exports = router;
