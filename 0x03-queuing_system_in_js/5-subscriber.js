#!/usr/bin/yarn dev
import { createClient } from 'redis';

const client = createClient();
const EXIT_MSG = "KILL_SERVER";

client.on("error", (error) => {
  console.log("Redis client not connected to the server:", err.toString());
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
})

client.subscribe("holberton school channel");

client.on("message", (_error, msg) => {
  console.log(msg);
  if (msg === EXIT_MSG) {
    client.unsubscribe();
    client.quit();
  }
});
