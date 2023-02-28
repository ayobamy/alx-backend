import redis from 'redis';
import { createClient } from 'redis';

// r = redis.Redis()

const client = redis.createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

setNewSchool((schoolName, value) => {
  client.set([schoolName, value], redis.print);
});

displaySchoolValue ((schoolName) => {
  const val = client.get([schoolName])
  console.log(`${val}`);
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
