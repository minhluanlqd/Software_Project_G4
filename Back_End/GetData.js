var express=require('express');
var bodyParser = require('body-parser')
var index=[]
var app=express();

var MongoClient = require('mongodb').MongoClient;
// url of database
var url = "mongodb+srv://ducnguyen:13111999@cluster0-vs5zx.mongodb.net/test?retryWrites=true&w=majority";

var urlencodedParser = bodyParser.urlencoded({ extended: false })

//set localhost:3001/signup to grab the data from the signup
app.set('view engine','ejs');
app.use('/css',express.static('css'))
// signup

app.get('/signup',function(req,res){
  //create the sign up page
  res.render('signup')
})
checkpass: // to confirm pass
app.post('/signup', urlencodedParser,function(req, res) {
  //get data at req.body

  console.log(req.body)
  //take cvv number
  console.log(req.body.cvv);
  //take creditnumber
  console.log(req.body.creditnum);
  // make connection with database
  //open
  MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    //mydb= table
    var dbo = db.db("mydb");
    //insert
    // customers = collection
    dbo.collection("customers").insertOne(req.body, function(err, res) {
      if (err) throw err;
      console.log("Sign up success");
      // close
      db.close();
    });
  });
  res.render('signup');
})

// signin
app.get('/signin',function(req,res)
{
  res.render('signin');
})
app.post('/signin',urlencodedParser,function(req,res){
  console.log(req.body.Username);
  res.render('signin');
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

app.listen('3001');
