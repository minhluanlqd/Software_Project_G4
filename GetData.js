var express=require('express');
var bodyParser = require('body-parser')
var index=[]
var app=express();

var urlencodedParser = bodyParser.urlencoded({ extended: false })

var MongoClient = require('mongodb').MongoClient;
// url of database
var url = "mongodb+srv://ducnguyen:13111999@cluster0-vs5zx.mongodb.net/test?retryWrites=true&w=majority";

//set localhost:3000/signup to grab the data from the signup
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
//////////////////////////////////////////////////
app.get('/signuptest_2.html',function(req,res){
  //create the sign up page
  res.sendFile(__dirname+'/signuptest_2.html');
})
app.post('/signuptest_2.html', urlencodedParser,function(req, res) {
  //get data at req.body
  console.log(req.body)
  //take cvv number
  console.log(req.body.username)
  // make connection with database
  //open
  MongoClient.connect(url,{ useUnifiedTopology: true }, function(err, db) {
    if (err) throw err;
    console.log("database connected");
    //mydb= table
    var dbo = db.db("mydb");
    //insert
    // customers = collection
    dbo.collection("customers").find(req.body, function(err, res) {
      if (err) throw err;
      console.log("Sign up success");
      // close
      db.close();
      console.log("database closed");
    });
  });

  res.sendFile(__dirname+'/index.html');
})
////////////////////////////////////////////////////////////
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
//////////////////////////////////////////////////////////////
app.get('/sign_in_2.html',function(req,res)
{
  res.sendFile(__dirname+'/sign_in_2.html');
})
app.post('/sign_in_2.html',urlencodedParser,function(req,res){
  console.log(req.body)
  // make connection with database
  //open
  MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    console.log("database connected");
    //mydb= table
    var dbo = db.db("mydb");
    //insert
    // customers = collection
    dbo.collection("customers").find({username: req.body.username, password: req.body.password}, function(err, res) {
      if (err) throw err;
      console.log(res._id);
      console.log("Sign in success");
      // close
      db.close();
      console.log("database closed");
    });
  });
  res.sendFile(__dirname+'/index.html');
})
app.listen('3000');
