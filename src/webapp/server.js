// server.js
// load the things we need
var express = require('express');
var app = express();

// set the view engine to ejs
app.set('view engine', 'ejs');
app.use('/public', express.static(__dirname + '/public'))

// use res.render to load up an ejs view file

// index page 
app.get('/', function(req, res) {
    res.render('pages/index');
});


app.get('/sample', function (req, res) {
    res.json({"mil": "teste"});
});

app.get('/suggestions', function (req, res) {
    res.json({"suggestions": ["comida 1", "comida 2", "comida 3"]});
});
             
// about page 
// app.get('/about', function(req, res) {
//     res.render('pages/about');
// });

app.listen(8080);
console.log('8080 is the magic port');
