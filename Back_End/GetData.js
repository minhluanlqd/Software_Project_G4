var express=require('express');
var bodyParser = require('body-parser')
var index=[]
var app=express();

var urlencodedParser = bodyParser.urlencoded({ extended: false })

//set localhost:3001/signup to grab the data from the signup
app.set('view engine','ejs');
app.use('/css',express.static('css'))


app.get('/signup',function(req,res){
  //create the sign up page
  res.render('signup')
})
app.post('/signup', urlencodedParser,function(req, res) {
  //get data at req.body

  console.log(req.body)
  //take cvv number
  console.log(req.body.cvv);
  //take creditnumber
  console.log(req.body.creditnum);
  res.render('signup');
})

app.get('/ReservationForm',function(req,res){
  //create  a server for the reserved page
  res.render('ReservationForm')
})
app.post('/ReservationForm', urlencodedParser,function(req, res) {
  //get data at req.body
  console.log(req.body);
  // link with the reservation page
  res.render()
  res.render('ReservationForm');

})

app.get('/signin',function(req,res)
{
  res.render('signin');
})
app.post('/signin',urlencodedParser,function(req,res){
  console.log(req.body.Username);
  res.render('signin');
})
app.listen('3001');
