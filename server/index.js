const { response } = require('express');
const express = require('express');
const app = express();

//listen for incoming requests
app.listen(3000, () => console.log('Listening at 3000'));
//server index.html
app.use(express.static('public'));
//set json limits
app.use(express.json({ limit: '1mb' }));
//recieve post requests to /api
app.post('/api', (req, res) => {
    console.log('New request!');
    console.log(req.body);
    const data = req.body;
    //return data with success status
    res.json({
        status: 'success',
        num1: data.testNum1,
        num2: data.testNum2
    });
});
