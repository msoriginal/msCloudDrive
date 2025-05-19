const { exec } = require("child_process");
const fs = require("fs");
const path = require("path");

const SUBDOMAIN = "msclouddrive";
const PORT = 8000;
const RETRY_INTERVAL = 5000; // milliseconds
const LOG_FILE = path.join(__dirname, "lt-log.txt");

function logToFile(message) {
  const timestamp = new Date().toISOString();
  fs.appendFileSync(LOG_FILE, `[${timestamp}] ${message}\n`);
}

function startTunnel() {
  console.log(`\n[INFO] Starting localtunnel on subdomain: ${SUBDOMAIN}...`);
  logToFile(`[INFO] Attempting to start localtunnel with subdomain: ${SUBDOMAIN}`);

  const cmd = `lt --port ${PORT} --subdomain ${SUBDOMAIN}`;
  const tunnelProcess = exec(cmd);

  tunnelProcess.stdout.on("data", (data) => {
    process.stdout.write(`[lt stdout] ${data}`);
    logToFile(`[lt stdout] ${data.toString().trim()}`);
  });

  tunnelProcess.stderr.on("data", (data) => {
    process.stderr.write(`[lt stderr] ${data}`);
    logToFile(`[lt stderr] ${data.toString().trim()}`);
  });

  tunnelProcess.on("exit", (code, signal) => {
    const message = `[WARN] LocalTunnel exited (code: ${code}, signal: ${signal}). Retrying in ${RETRY_INTERVAL / 1000}s...`;
    console.warn(message);
    logToFile(message);
    setTimeout(startTunnel, RETRY_INTERVAL);
  });

  tunnelProcess.on("error", (err) => {
    const message = `[ERROR] Failed to start LocalTunnel: ${err.message}. Retrying in ${RETRY_INTERVAL / 1000}s...`;
    console.error(message);
    logToFile(message);
    setTimeout(startTunnel, RETRY_INTERVAL);
  });
}

startTunnel();