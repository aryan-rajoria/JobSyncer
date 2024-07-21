const express = require('express');
const fs = require('fs').promises;
const path = require('path');
const cors = require('cors');  // You may need to install this: npm install cors
const app = express();
const port = process.env.PORT || 5000;

app.use(cors());  // Enable CORS for all routes
app.use(express.json());

app.post('/api/save-data', async (req, res) => {
    try {
        const { data } = req.body;
        const filePath = path.join(__dirname, 'newData.json');
        
        await fs.writeFile(filePath, JSON.stringify({ data }, null, 2));
        res.send('File saved successfully');
    } catch (error) {
        console.error('Error writing file:', error);
        res.status(500).send('Error saving file');
    }
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});