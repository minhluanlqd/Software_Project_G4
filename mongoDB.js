var MongoClient = require('mongodb').MongoClient;
//var url = "mongodb://localhost:27017/"; local

//mongodb+srv://tanngo:<password>@cluster0-nyi9f.mongodb.net/test?retryWrites=true&w=majority

var url = "mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority";

//var url="mongodb+srv://ducnguyen:13111999@cluster0-vs5zx.mongodb.net/test?retryWrites=true&w=majority";

MongoClient.connect(url,{useUnifiedTopology: true }, function (err, db) {
    if (err) throw err;
    console.log("Database connected");

    exports.insertSignUpData = data => {
        var dbo = db.db("parkinglot");
        //var dbo = db.db("mydb");
        //var myobj = JSON.parse(data);
        dbo.collection("customers").find({ username: data.username}, function (err, res) {
            if (err) throw err;
            console.log(res._id);
            if (res._id == undefined){
                console.log("Signing up ");
                // increase coutner "conut" by 1 when about to insert
                  dbo.collection("UserCount").findOneAndUpdate({'myId':"my"},{$inc: {"count" : 1}}, function (err, res3) {
                      if (err) throw err;
                  });
                  dbo.collection("UserCount").findOne({'myId':"my"}, function(err,result){
                    if (err) throw err;
                    // assgin "count"=user_id
                    data.user_id=result.count;
                    dbo.collection("customers").insertOne(data, function (err, res) {
                        if (err) throw err;
                        console.log("Sign up success");
                      });
                  });

                }
            else{
                console.log("username already exit");
            }

        });
    }

    exports.getUserId = data => {
        var dbo = db.db("parkinglot");
        dbo.collection("customers").findOne({ username: data.username, password: data.password }, function (err, res) {
            if (err) throw err;
            console.log(res.username);
            if (res !== undefined){
                console.log("Sign in success");
                //store user_id= currentId to database and get that object when want to use with user_id
                dbo.collection("UserCount").findOneAndUpdate({'myId':"my"},{$set:{currentId : res.user_id}}, function (err, res3) {
                    if (err) throw err;
                });
            }
            else{
                console.log("failed");
            }
            });
        }

        exports.getSize = () =>{
            var dbo = db.db("parkinglot");
            dbo.collection("customers").count({}, (err, res) =>{
              if (err) console.log(err);
            //  console.log(res);
            //  var t = res;
            //  console.log("t= " + t);
              return res;
            });

        }







    // db.close();


    // exports.insertReservationData = data => {}
});
