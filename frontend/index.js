// import fetch from 'node-fetch';
// import cors from 'cors';
import express from "express";


import 'dotenv/config';
const app = express();

app.use(express.static('public'));

app.use(express.json());
app.use(express.urlencoded({
    extended: true
}));

// Enable CORS for all routes
// app.use(cors());

// const port = process.env.PORT || 3000;
// const environment = process.env.ENVIRONMENT || 'sandbox';
// const client_id = process.env.CLIENT_ID;
// const client_secret = process.env.CLIENT_SECRET;
// const endpoint_url = environment === 'sandbox' ? 'https://api-m.sandbox.paypal.com' : 'https://api-m.paypal.com';

app.post('/create_order', (req, res) => {
    
});



// Helper / Utility functions

//Servers the index.html file
app.get('/signup', (req, res) => {
    res.sendFile(process.cwd() + '/views/signUp.html');
});
app.get('/login', (req, res) => {
    res.sendFile(process.cwd() + '/views/login.html');
});

//Servers the style.css file
app.get('/style.css', (req, res) => {
    res.sendFile(process.cwd() + '/style.css');
});
//Servers the script.js file
app.get('/script.js', (req, res) => {
    res.sendFile(process.cwd() + '/script.js');
});


app.listen(3000, () => {
    console.log(`Server listening at http://localhost:3000`)
})
