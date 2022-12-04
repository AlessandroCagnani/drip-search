const express = require("express");
const path = require("path");
const cors = require("cors");
const axios = require("axios");
const bodyParser = require("body-parser");
const app = express();
const SolrNode = require("solr-node");

var client = new SolrNode({
  host: "localhost",
  port: "8983",
  collection: "drip",
  protocol: "http",
});

app.use(cors({ origin: "*" }));
app.use(express.urlencoded({ extended: false })); // parse application/x-www-form-urlencoded
app.use(express.json({ limit: "4MB" })); // parse application/json
app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.json());

///////////////////////////////////////////////
/////////////       ROUTES       //////////////
///////////////////////////////////////////////

app.get("/search", (req, res) => {
  const q = req.query.q;
  console.log("q: ", q);

//   let body = {
//     q: q,
//     qf: "title^3.0 category^3.0 description^1.5 color^0.5",
//     defType: "edismax",
//     mm: "2",
//   };

  let qf = "title^3.0 category^3.0 description^1.5 color^0.5";
  let defType = "edismax";
  let mm = "2";

  axios({
    method: "get",
    url: `http://localhost:8983/solr/drip/query?q=${q}&qf=${qf}&defType=${defType}&mm=${mm}`,
    // headers: {},
    // data: body,
  })
    .then((response) => {
      console.log("response: ", response.data);
      res.status(200).json(response.data);
    })
    .catch((error) => {
      console.log("error: ", error);
      res.status(500).send("error");
    });
});

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
