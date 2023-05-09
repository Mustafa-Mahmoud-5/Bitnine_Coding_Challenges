const pool = require("./db");
 
// After editing the pg driver source code, using the default pool.query or even client.query,will return the result in this json format {status_code: 200, data: [{row1},{row2}]}

pool.query("SELECT * FROM user_table")
.then(result => {
  console.log("RESULT: ", result);
})
.catch(error => console.error(error));

pool.end();


