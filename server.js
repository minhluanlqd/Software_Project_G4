const dotenv = require('dotenv');
const app = require('./GetData');
//const myDB = require('./mongoDB');

dotenv.config({ path: './config.env' });

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`App running on port ${port}...`);
});