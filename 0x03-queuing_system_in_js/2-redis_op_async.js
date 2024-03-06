/**
 * Displays same results as 1-redis_op.js using promisify
 */
const redis = require('redis');
import { createClient } from 'redis';
const util = require('util');

const client = createClient({host: 'localhost', port: 6379});
var getAsync = util.promisify(client.get).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', err => {
    console.log(`Redis client not connected to the server: ${err}`);
});


function setNewSchool(schoolName, Value) {
    client.set(schoolName, Value, (err, reply) => {
        if(err){
            console.log(err);
        } else {
            redis.print(`Reply: ${reply}`);
        }
    });
}

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(`${value}`);
    } catch (error) {
        console.log(error);
    }
}



displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');