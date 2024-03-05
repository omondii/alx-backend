/**
 * connects to redis server on local machine
 */
const redis = require('redis');
import { createClient } from 'redis';
const client = createClient({host: 'localhost', port: 6379});

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

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, value) => {
        if (err) {
            console.log(err)
        } else {
            console.log(`${value}`)
        }
    });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
