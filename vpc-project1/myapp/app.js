const http = require('http');

http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('<h1>Hello from EC2 Server!</h1><p>Application deployed successfully.</p>');
}).listen(3000, '0.0.0.0');

console.log("Running on port 3000");
