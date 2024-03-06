/**
 * implements the Publish messaging paradigm.
 * 
 */
import { createClient } from 'redis';
const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', () => {
    console.log(`Redis client not connected to the server: ${err}`);
});

const channel = 'holberton school channel';
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
    }, time);
    client.publish(channel, message)
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
