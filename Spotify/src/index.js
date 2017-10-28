import Speaker from 'speaker';
import {Decoder} from 'lame';
import Consumer from 'sqs-consumer';
import {config as configEnv} from 'dotenv';
import request from 'request';
import Spotify from 'spotify-web-api-node';

const store = {};
const getToken = () => {
  return store.Token;
};
const setToken = (token) => {
  store.Token = token;
};

// Setup the config files
configEnv();
if (
  !process.env.SPOTIFY_CLIENT_ID ||
  !process.env.SPOTIFY_CLIENT_SECRET ||
  !process.env.AWS_SECRET_ACCESS_KEY ||
  !process.env.AWS_ACCESS_KEY_ID ||
  !process.env.AWS_REGION ||
  !process.env.AWS_QUEUE_URL
) throw new Error('No AWS Credentials Supplied');

const spotifyInstance = new Spotify({
  clientId: process.env.SPOTIFY_CLIENT_ID,
  clientSecret: process.env.SPOTIFY_CLIENT_SECRET,
});

const appHandler = (message, done) => {
  if (!message.Body) {
    throw new Error('Message did not contain body');
  }

  spotifyInstance.clientCredentialsGrant().then((data) => {
    setToken(data.body['access_token']);
    const body = JSON.parse(message.Body);
    if (!body.song) throw new Error('Song not attached to body');
    console.log(`Received job: ${body.song}`);

    const speaker = new Speaker({
      channels: 2,
      bitDepth: 16,
      sampleRate: 44100,
    });
    const decoder = new Decoder();
    request(body.song)
      .pipe(decoder)
      .pipe(speaker);

    done();
  });
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
