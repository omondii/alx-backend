/**
 * An array of blacklisted numbers that shouldn't be done by the processor
 */
const kue = require('kue');
import { createQueue } from 'kue';
const queue = kue.createQueue();

const blacked = [4153518780, 4153518781]

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    if (blacked.includes(phoneNumber)) {
        done(Error(`Phone number ${phoneNumber}, with message: ${message}`));
        return;
    }
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('push_notification_code_2', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
