// var express = require('express');
// var app = express();


// middleware

// app.use(function (req, res, next) {
//     console.log("hello from middleware");
//     next();
// })


// for params and for routing 
// app.get('/', function (req, res) {
//     res.send("<h1>This is HomePage</h1>")
// })

// app.get('/profile', function (req, res) {
//     res.send("<h1>This is Profile Page</h1>")
// })

// app.get('/profile/:username', function (req, res) {
//     res.send(`Hello From ${req.params.username}`);
// })


// basic dump

// app.get('/rohan', function (req, res) {
//     res.send("<h1>Rohan Bro How u doin'?</h1>")
// })
// app.get('/varun', function (req, res) {
//     res.send("<h1>Varun is noob programmer</h1>")
// })

// app.get('/divyansh', function (req, res) {
//     res.send("<h1>divyansh Bro How u doin'?</h1>")
// })

// app.get('/rishi', function (req, res) {
//     res.send("<h1>Rishi Bro How u doin'?</h1>")
// })

// app.get('/prashant', function (req, res) {
//     res.send("<h1>Prashant Bro How u doin'?</h1>")
// })

// app.get('/jatin', function (req, res) {
//     res.send("<h1>Jatin Bro How u doin'?</h1>")
// })

// app.get('/login', function (req, res) {
//     res.send("<h1><form><label>First name:</label><br><input><br><label>Last name:</label><br><input> </form></h1>")
// })

// var host = app.listen(3000);
// console.log('server is listening at :https://varunsingh.com/', host);

// setup EJS
// 1) install EJS
// npm i EJS
// 2) configure EJS
// app.set("view engine", "ejs")
// 3) make folder as "views"
// 4) write.ejs file inside views
// 5) write send as render

var express = require('express');
var app = express();

app.set('view engine', 'ejs');
app.get('/', function (req, res) {
    res.send("This Is Main Page...");
})

app.get('/loginpage', function (req, res) {
    res.render("index");
})

app.get('/home', function (req, res) {
    res.render("home");
})
app.get('/contact', function (req, res) {
    res.render("contact");
})


var host = app.listen(3000);
console.log('server is listening at :https://varunsingh.com/', host);