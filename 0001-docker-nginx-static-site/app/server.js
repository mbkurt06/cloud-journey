const http = require("http");

console.log("Server is starting...");

const server = http.createServer((req, res) => {
  console.log("Request received:", req.method, req.url);
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Backend is running\n");
});

server.listen(3000, "0.0.0.0", () => {
  console.log("Server is listening on port 3000");
});