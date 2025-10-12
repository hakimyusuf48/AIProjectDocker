#!/usr/bin/env node
const http = require('http');
const port = process.env.PORT || 8080;
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ service: 'react_app', status: 'ok' }));
});
server.listen(port, '0.0.0.0', () => {
  console.log(`react_app placeholder listening on ${port}`);
});
