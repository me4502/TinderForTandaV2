import Speaker from 'speaker';
import {Decoder} from 'lame';
import Consumer from 'sqs-consumer';
import {config as configEnv} from 'dotenv';
import request from 'request';

// Setup the config files
configEnv();
if (
  !process.env.AWS_SECRET_ACCESS_KEY ||
  !process.env.AWS_ACCESS_KEY_ID ||
  !process.env.AWS_REGION ||
  !process.env.AWS_QUEUE_URL
) throw new Error('No AWS Credentials Supplied');


const appHandler = (message, done) => {
  if (!message.Body) {
    throw new Error('Message did not contain body');
  }
  const body = JSON.parse(message.Body);
  if (!body.song) throw new Error('Song not attached to body');

  const speaker = new Speaker({
    channels: 2,
    bitDepth: 16,
    sampleRate: 44100,
  });
  const decoder = new Decoder();
  request(body.song).pipe(decoder).pipe(speaker);
  done();
};

const app = Consumer.create({
  queueUrl: process.env.AWS_QUEUE_URL,
  handleMessage: appHandler,
  region: process.env.AWS_REGION,
});

app.on('error', (err) => {
  console.log(err.message);
});

console.log('Starting consumer for Song Player');
app.start();
