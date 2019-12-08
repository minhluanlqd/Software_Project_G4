var MongoClient = require('mongodb').MongoClient;
//var url = "mongodb://localhost:27017/"; local

//mongodb+srv://tanngo:<password>@cluster0-nyi9f.mongodb.net/test?retryWrites=true&w=majority

var url = "mongodb+srv://tanngo:trtan!605@cluster0-nyi9f.mongodb.net/parkinglot?retryWrites=true&w=majority";

//var url="mongodb+srv://ducnguyen:13111999@cluster0-vs5zx.mongodb.net/test?retryWrites=true&w=majority";
var costModel = require('./costModel');
var garage = require('./garage');
var fs = require('fs');

MongoClient.connect(url, { useUnifiedTopology: true }, function (err, db) {
    if (err) throw err;
    console.log("Database connected");

    exports.insertSignUpData = data => {
        var dbo = db.db("parkinglot");
        //var dbo = db.db("mydb");
        //var myobj = JSON.parse(data);
        dbo.collection("customers").find({ username: data.username }, function (err, res) {
            if (err) throw err;
            console.log(res._id);
            if (res._id == undefined) {
                console.log("Signing up ..");
                // increase coutner "conut" by 1 when about to insert
                dbo.collection("UserCount").findOneAndUpdate({ 'myId': "my" }, { $inc: { "count": 1 } }, function (err, res3) {
                    if (err) throw err;
                });
                dbo.collection("UserCount").findOne({ 'myId': "my" }, function (err, result) {
                    if (err) throw err;
                    // assgin "count"=user_id
                    data.user_id = result.count;
                    dbo.collection("customers").insertOne(data, function (err, res) {
                        if (err) throw err;
                        console.log("Sign up success");
                    });
                });
            }
            else {
                console.log("username already exit");
            }

        });
    }

    exports.getUserId = data => {
        var dbo = db.db("parkinglot");
        dbo.collection("customers").findOne({ username: data.username, password: data.password }, function (err, res) {
            if (err) throw err;
            // console.log(res.username);
            if (res !== null) {
                console.log("Signing in ..");
                //store user_id= currentId to database and get that object when want to use with user_id
                dbo.collection("UserCount").findOneAndUpdate({ 'myId': "my" }, { $set: { currentId: res.user_id } }, function (err, res3) {
                    if (err) throw err;
                    console.log("User_id: " + res.user_id);
                    console.log("Sign in success");
                });
            }
            else {


                console.log("failed");

            }
        });


    }
    exports.logOut = () => {
        var dbo = db.db("parkinglot");
        console.log("Signing out...");
        dbo.collection("UserCount").findOneAndUpdate({ 'myId': "my" }, { $set: { currentId: 0 } }, (err, res) => {
            if (err) throw err;
            console.log("Sign out success");
        })

    }

    exports.pay = data => {
        var dbo = db.db("parkinglot");
        //var dbo = db.db("mydb");
        //var myobj = JSON.parse(data);
        dbo.collection("UserCount").findOne({ 'myId': "my" }, function (err, res) {
            if (err) throw err;
            if (res.currentId != 0) {
                dbo.collection("customers").findOneAndUpdate({ 'user_id': res.currentId }, {
                    $set: {
                        NameOnCard: data.NameOnCard,
                        CardNumber: data.CardNumber,
                        cvv: data.cvv,
                        ExpiryDate: data.ExpiryDate
                    }
                }, function (err, res2) {
                    if (err) throw err;
                    console.log("Add payment success");
                });

            }
            else {
                console.log("User doesn't SignIn");

            }
        });
    }

    exports.insertReservation = data => { //add id, add email, add cost, add slot, add DL plate
        var dbo = db.db("parkinglot");
        dbo.collection("UserCount").findOne({ 'myId': "my" }, (err, res) => {
            if (err) throw err;
            var id = res.currentId;
            if (id !== 0) {
                data.user_id = id;
                dbo.collection("customers").findOne({ 'user_id': id }, (err2, customer) => {
                    if (err2) throw err;
                    data.email = customer.email;
                    data.drivinglicensenumber = customer.drivinglicensenumber;
                    data.slot = garage.assignSlot('car');
                    data.cost =- costModel.getNormalCostByShape('car', data.startTime, data.endTime);
                    dbo.collection("UserCount").findOneAndUpdate({ 'myId': "my" }, { $inc: { "transCount": 1 } }, (err3, res1) => {
                        if (err3) throw err3;
                        dbo.collection("UserCount").findOne({ 'myId': "my" }, (err, result) => {
                            data.transId = result.transCount;
                            console.log("Order: ");
                            console.log(data);
                            dbo.collection("garage").insertOne(data, (err, res4) => {
                                if (err) throw err;
                            })
                        })
                    })

                })
            }
            else console.log('User does not sign in');
        })
    };

    exports.insertReservationWalkIn = data => { //add id, add email, add cost, add slot, add DL plate
        var dbo = db.db("parkinglot");
        data.slot = garage.assignSlot('truck');
        data.cost = -costModel.getWalkinCostByShape('truck', data.startTime, data.endTime);
        dbo.collection("UserCount").findOneAndUpdate({ 'myId': "my" }, { $inc: { "transCount": 1 } }, (err3, res1) => {
            if (err3) throw err3;
            dbo.collection("UserCount").findOne({ 'myId': "my" }, (err, result) => {
                data.transId = result.transCount;
                dbo.collection("garage").insertOne(data, (err1, res4) => {
                    if (err1) throw err;
                })
            })
        })

    };

    exports.CancelReservation= () =>{
      // the customer can only cancel latest transaction and already login
      var dbo = db.db("parkinglot");
      dbo.collection("UserCount").findOne({'myId': "my"}, (err,result1)=> {
        if(err) throw err;
        if(result1.currentId != 0){
          // transId :-1 means descending , 1 means ascending
          dbo.collection("garage").find({'user_id': result1.currentId}).sort({ transId : -1}).toArray((err1,result)=> {
            if(err1) throw err1;
            //0 means latest transaction
            console.log("Lastest transaction: ");
            console.log(result[0]);
            var refund= result[0];
            refund.cost= -result[0].cost;
            refund._id=null;
            dbo.collection("UserCount").findOneAndUpdate({ 'myId': "my" }, { $inc: { "transCount": 1 } }, (err3, res1) => {
                if (err3) throw err3;
            })
            dbo.collection("UserCount").findOne({ 'myId': "my" }, (err, res) => {
                if (err) throw err;
                refund.transId = res.transCount;
                console.log("Refund transaction:");
                console.log(refund);
                dbo.collection("garage").insertOne(refund, (err1, res1) => {
                    if (err1) throw err;
                })
            })
          })
        }else
        console.log('User does not sign in');
      })
    };

    exports.editReservation= data =>{
      module.exports.CancelReservation();
      module.exports.insertReservation(data);
    }

})










        // db.close();


        // exports.insertReservationData = data => {}
