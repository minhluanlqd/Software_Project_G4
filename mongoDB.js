var MongoClient = require('mongodb').MongoClient;
//var url = "mongodb://localhost:27017/"; local

//mongodb+srv://tanngo:<password>@cluster0-nyi9f.mongodb.net/test?retryWrites=true&w=majority

var url = "mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority";


MongoClient.connect(url,{useUnifiedTopology: true }, function (err, db) {
    if (err) throw err;
    console.log("Database connected");
    exports.insertSignUpData = data => {
        var dbo = db.db("parkinglot");
        //var myobj = JSON.parse(data);
        dbo.collection("customers").insertOne(data, function (err, res) {
            if (err) throw err;
            console.log("1 document inserted");
            db.close();
        });
    }

    exports.findUserName = data => {
        var dbo = db.db("parkinglot");
        dbo.collection("customers").find({ username: data.username, password: data.password }, function (err, res) {
            if (err) throw err;
            console.log(res._id);
            if (res != null){
                console.log("Sign in success");
                return true;
            }
            else{
                console.log("failed");
                return false;
            }
            });


        }





    // db.close();


    // exports.insertReservationData = data => {}
});
