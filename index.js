const { response } = require('express');
const express = require('express');
const app = express();

app.listen(3000, () => console.log('Listening at 3000'));
app.use(express.static('public'));
app.use(express.json({ limit: '1mb' }));
app.post('/api', (req, res) => {
    console.log('New request!');
    console.log(req.body);
    const data = req.body;
    res.json({
        status: 'success',
        num1: data.testNum1,
        num2: data.testNum2
    });
});
