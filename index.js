
const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('.'));

app.listen(port, '0.0.0.0', () => {
  console.log(`Servidor corriendo en http://0.0.0.0:${port}`);
});
