var express = require('express');
var app = express();
app.set('view engine', 'ejs');

const bodyParser = require("body-parser");
var user = "hello";
app.use(bodyParser.urlencoded({
    extended: true
}));

app.post("/", function (req, res) {
   user = req.body.hihi;
    console.log(req.body)
res.render('index', { user_name: user });
});

// route pages
app.get('/', function (req, res) {
  res.render('index', { user_name: user });
});

// what port to run server on
app.listen(3001, function () {
  console.log('server started on port 3001');
});