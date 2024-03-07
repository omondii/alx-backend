/**
 * implements the Subscribe messaging paradigm.
 * This creates a redis-based queuing system, the subscriber.js processes
 * a job created by publisher.js
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

const channelName = 'holberton school channel';

// Subscribe to a channel
client.subscribe(channelName, (err, count) => {
});

// Listen for messages in subd channel
client.on('message', (channel, message) => {
    console.log(`${message}`);
    if (message === 'KILL_SERVER') {
        client.unsubscribe(channel);
        process.exit(0)
    }
});