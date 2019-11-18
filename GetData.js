var express=require('express');
var bodyParser = require('body-parser')
var index=[]
var app=express();

var urlencodedParser = bodyParser.urlencoded({ extended: false })

//set localhost:3001/signup to grab the data from the signup
app.use('/css',express.static('css'))
app.use('/images',express.static('images'))

app.get('/',function(req,res)
{
  res.sendFile(__dirname+'/index.html');
})

app.get('/index.html',function(req,res)
{
  res.sendFile(__dirname+'/index.html');
})

app.get('/signuptest_2.html',function(req,res){
  //create the sign up page
  res.sendFile(__dirname+'/signuptest_2.html');
})
app.post('/signuptest_2', urlencodedParser,function(req, res) {
  //get data at req.body

  console.log(req.body)
  //take cvv number
  console.log(req.body.username)
  res.sendFile(__dirname+'/index.html');
})

app.get('/walk_in_signup.html',function(req,res){
  //create  a server for the reserved page
  res.sendFile(__dirname+'/walk_in_signup.html');
})
app.post('/walk_in_signup.html', urlencodedParser,function(req, res) {
  //get data at req.body
  console.log(req.body);
  // link with the reservation page
  res.sendFile(__dirname+'/walk_in_signup.html');

})

app.get('/sign_in_2.html',function(req,res)
{
  res.sendFile(__dirname+'/sign_in_2.html');
})
app.post('/sign_in_2',urlencodedParser,function(req,res){
  console.log(req.body)
  res.sendFile(__dirname+'/index.html');
})
app.listen('3000');
