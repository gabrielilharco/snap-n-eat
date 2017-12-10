var express = require('express');
var request = require("request")

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
    
    calories = req.query.calories;
    cholesterol = req.query.cholesterol;
    carbohydrates = req.query.carbohydrates;
    fat = req.query.fat;
    fiber = req.query.fiber;
    proteins = req.query.proteins;
    
    var suggestions_url = "http://127.0.0.1:5002";

    request({
        method: 'POST',
        url: suggestions_url,
        json: true,
        form: {"calories" : calories,
               "cholesterol" : cholesterol,
               "carbohydrates":carbohydrates,
               "fat" : fat,
               "fiber": fiber,
               "proteins": proteins}
    }, function(error, response, body) {
        if (!error && response.statusCode === 200) {
            console.log(body); // Print the json response
            res.json(body);
        }
    });

});
             

app.listen(8080);
console.log('8080 is the magic port');
