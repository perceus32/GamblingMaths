const path = require("path");
const fs = require("fs");

const express = require("express");

const app = express();

app.use(express.static(path.join(__dirname, "public")));

app.set("view engine", "ejs");
app.set("views", "views");

// const websiteroutes = require("./routes/user");

app.use(express.urlencoded({ extended: false }));

app.use(websiteroutes);
app.listen(process.env.PORT || 5000);
