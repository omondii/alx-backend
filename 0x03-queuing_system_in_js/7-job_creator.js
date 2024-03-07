/**
 * Create a jobs queue from the jobs array 
 */
const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

const kue = require('kue');
const queue = kue.createQueue();

jobs.forEach(job => {
    const newJob = queue.create('push_notification_code_2', job).save((err) => {
        if(!err){
            console.log(`Notification job created: ${newJob.id}`);
        }
    }).on('completed', () => {
        console.log(`Notification job ${newJob.id} completed`);
    }).on('failure', (error) => {
        console.log(`Notification job ${newJob.id} failed: ${error}`);
    }).on('progress', (progress, data) =>{
        const percentage = Math.round(progress * 100)
        console.log(`Notification job ${newJob.id} ${percentage}%`)
    })
})