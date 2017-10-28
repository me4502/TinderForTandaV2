import {config as configEnv} from 'dotenv';
import express from 'express';
import morgan from 'morgan';
import bodyParser from 'body-parser';
import Spotify from 'spotify-web-api-node';
import Producer from 'sqs-producer';
import uuid from 'uuid/v4';

const store = {};
const getToken = () => {
  return store.Token;
};
const setToken = (token) => {
  store.Token = token;
};

// Immediately load any environmental variables
configEnv();
if (
  !process.env.SPOTIFY_CLIENT_ID ||
  !process.env.SPOTIFY_CLIENT_SECRET ||
  !process.env.AWS_SECRET_ACCESS_KEY ||
  !process.env.AWS_ACCESS_KEY_ID ||
  !process.env.AWS_REGION ||
  !process.env.AWS_QUEUE_URL
) throw new Error('Double check environmental variables');

const spotifyInstance = new Spotify({
  clientId: process.env.SPOTIFY_CLIENT_ID,
  clientSecret: process.env.SPOTIFY_CLIENT_SECRET,
});

const producer = Producer.create({
  queueUrl: process.env.AWS_QUEUE_URL,
  region: process.env.AWS_REGION,
});

if (!process.env.PORT) {
  process.env.PORT = (process.env.NODE_ENV === 'production')
    ? '80'
    : '5000';
}

// Setup an Express Instance
const app = express();
if (process.env.NODE_ENV === 'development') {
  app.use(morgan('dev'));
} else {
  app.use(morgan('combined'));
}
app.use(bodyParser.json());

// Setup Express Routes
app.post('/play', async (req, res) => {
  if (!req.body || !req.body.query) {
    res.status(400).json({
      msg: 'Please supply a json body with: query',
    });
  }
  try {
    const spotifyResult = await spotifyInstance.searchTracks(req.body.query);
    console.log(`Searched Spotify for ${req.body.query}`);

    if (spotifyResult.body.tracks.items[0].preview_url) {
      const payload = {
        song: spotifyResult.body.tracks.items[0].preview_url,
      };

      producer.send({
        id: uuid(),
        body: JSON.stringify(payload),
      }, (err) => {
        if (err) console.error(err);
      });
    } else {
      producer.send(JSON.stringify({
        song: 'https://p.scdn.co/mp3-preview/2e7e8462ffe37b05496c015505aabda332b9f884?cid=2bafe74b3e144b54a78db4f734c714ea',
      }))
    }

    res.status(200).json({
      name: spotifyResult.body.tracks.items[0].name,
      artists: spotifyResult.body.tracks.items[0].artists.map(data => data.name),
      previewUrl: spotifyResult.body.tracks.items[0].preview_url,
      spotifyUrl: spotifyResult.body.tracks.items[0].href,
    });
  } catch (e) {
    return res.status(400).json({spotifyError: e});
  }
});

// Get API Token
export const spotifyServer = () => spotifyInstance.clientCredentialsGrant().then((data) => {
  setToken(data.body['access_token']);
  spotifyInstance.setAccessToken(getToken());
  console.log(`Set Spotify Token to: ${getToken()}`);
  // Boot Up Express
  app.listen(parseInt(process.env.PORT, 10), () =>
    console.log(`WebApp has started on ${process.env.PORT}`),
  );
});


