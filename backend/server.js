const express = require("express");
const path = require("path");
const cors = require("cors");
const axios = require("axios");
const bodyParser = require("body-parser");
const app = express();

// import functions from helper.js
const helper = require("./helper.js");

app.use(cors({ origin: "*" }));
app.use(express.urlencoded({ extended: false })); // parse application/x-www-form-urlencoded
app.use(express.json({ limit: "4MB" })); // parse application/json
app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.json());


///////////////////////////////////////////////
/////////////       ROUTES       //////////////
///////////////////////////////////////////////



///////////////////////////////////////////////
////////////     END ROUTES       /////////////
///////////////////////////////////////////////

// listener for
app.set("port", process.env.PORT || 8888);

var server = require("http").createServer(app);

server.on("listening", function () {
  console.log("Express server listening on port " + server.address().port);
});

server.listen(app.get("port"));
