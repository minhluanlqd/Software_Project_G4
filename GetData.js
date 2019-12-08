var express = require('express');
var bodyParser = require('body-parser')
var index = [];
var myDB = require('./mongoDB');
var app = express();
var fs = require('fs');

var urlencodedParser = bodyParser.urlencoded({ extended: false })

var cus_id;

//set localhost:3000/signup to grab the data from the signup
app.use('/css', express.static('css'));

app.use('/images', express.static('images'));

app.get('/', function (req, res) {
  // console.log(fs.readFileSync('./loginError.txt','utf-8'));
  res.sendFile(__dirname + '/Index.html');
})

app.get('/Index.html', function (req, res) {
  myDB.logOut();
  res.sendFile(__dirname + '/Index.html');

})
/////////////////////////////////////SignUp
app.get('/SignUp.html', function (req, res) {
  //create the sign up page
  res.sendFile(__dirname + '/SignUp.html');
})
app.post('/SignUp.html', urlencodedParser, function (req, res) {
  //get data at req.body
  console.log(req.body)
  //take cvv number
  console.log(req.body.username)
  myDB.insertSignUpData(req.body);
  res.sendFile(__dirname + '/Index.html');
})
///////////////////////////////////////Payment
app.get('/payment.html', function (req, res) {
  //create  a server for the reserved page
  res.sendFile(__dirname + '/payment.html');
})
app.post('/payment.html', urlencodedParser, function (req, res) {
  //get data at req.body
  console.log(req.body);
  // link with the reservation page
  myDB.pay(req.body);
  res.sendFile(__dirname + '/SuccessSignIn.html');

})
///////////////////////////////////////Walk-in
app.get('/Walkin.html', function (req, res) {
  //create  a server for the reserved page
  res.sendFile(__dirname + '/Walkin.html');
})
app.post('/Walkin.html', urlencodedParser, function (req, res) {
  //get data at req.body
  console.log(req.body);
  // link with the reservation page
  myDB.insertReservationWalkIn(req.body);
  res.sendFile(__dirname + '/Index.html');

})

/////////////////////////////Online Customer
app.get('/SignIn.html', function (req, res) {
  res.sendFile(__dirname + '/SignIn.html');
})
app.post('/SignIn.html', urlencodedParser, function (req, res) {
  console.log(req.body)
  myDB.getUserId(req.body);

  res.sendFile(__dirname + '/SuccessSignIn.html');
})





app.get('/SuccessSignIn.html', function (req, res) {
  res.sendFile(__dirname + '/SuccessSignIn.html');
})



app.get('/ReservationForm.html', function (req, res) {
  //create  a server for the reserved page
  res.sendFile(__dirname + '/ReservationForm.html');
})
app.post('/ReservationForm.html', urlencodedParser, function (req, res) { //log in reservation
  //get data at req.body

  // link with the reservation page
  myDB.insertReservation(req.body);
  res.sendFile(__dirname + '/SuccessSignIn.html');

})

app.get('/EditReservation.html', function (req, res) {
  //create  a server for the reserved page
  res.sendFile(__dirname + '/EditReservation.html');
})
app.post('/EditReservation.html', urlencodedParser, function (req, res) {
  //get data at req.body //
  console.log(req.body);
  // link with the reservation page
  //myDB.editReservation();
  res.sendFile(__dirname + '/SuccessSignIn.html');

})
/////////////////////////////////////////////////////Cancel
app.get('/CancelReservation.html', function (req, res) {
  //create  a server for the reserved page
  res.sendFile(__dirname + '/CancelReservation.html');
})
app.post('/CancelReservation.html', urlencodedParser, function (req, res) {
  //get data at req.body
  console.log(req.body);
  // link with the reservation page
  res.sendFile(__dirname + '/CancelSuccess.html');

})

app.get('/CancelSuccess.html', function (req, res) {
  res.sendFile(__dirname + '/CancelSuccess.html');
})




module.exports = app;
