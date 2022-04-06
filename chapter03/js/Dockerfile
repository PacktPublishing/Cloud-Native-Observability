FROM node:15
WORKDIR /app

COPY package.json ./

RUN npm install

COPY ./* ./

ENTRYPOINT ["node", "/app/brokentelephone.js"]