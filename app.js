//Import Package
const express = require('express');
const {spawn} = require('child_process');
const bodyParser = require('body-parser');
const exphbs = require('express-handlebars');
const path = require('path');
const ejs=require('ejs');

var mongoose = require("mongoose");


mongoose.connect("mongodb://localhost:27017/kuchbhi", { useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true }).then(()=>{
    console.log("connected")
});







//Set Package
const app = express();
app.use(express.static('html'));








app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())


app.get("/users", async (req, res) => {
    const users = await User.find();
    res.json(users);
  });

  app.get('/', (req, res) => {
 
    var dataToSend;
    // spawn new child process to call the python script
    const python = spawn('python', ['scrapper1.py']);
    // collect data from script
    python.stdout.on('data', function (data) {
     console.log('Pipe data from python script ...');
     dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    res.send(dataToSend)
    });
    
   })


//Post Emaul Request

    

app.listen(8081, () => console.log("Server Started..."));



  